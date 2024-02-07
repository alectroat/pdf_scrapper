from linq import Query
from operator import attrgetter

from TextCoordinate import ItemCoordinate, HeaderCollection, GapCollection


class Helper:
    def __init__(self, pdf_raw_data):
        self.word_frequency = 8
        self.empty_string = ""
        self.first_page = 1
        self.pdf_raw_data = pdf_raw_data
        pass

    def end_of_table_when_text_under_table(self, page_no, end_of_page, mandatory_column_coord):
        dada_inside_certain_height = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: (
                        x.pageNo == page_no
                        and mandatory_column_coord.y2 < x.y1 < end_of_page
                        and x.text != self.empty_string
                )
            )
            .select(lambda x: x)
            .to_list()
        )

        end_of_table = next(
            (item.y1 for item in dada_inside_certain_height if item.x1 < mandatory_column_coord.x2 < item.x2),
            0,
        )

        return end_of_table

    def end_of_table_when_blank_under_table(self, page_no, end_of_page, mandatory_column_coord):
        row_gap_allowed = 45
        end_of_table = 0

        data_source = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == page_no
                and mandatory_column_coord.y2 < x.y1 < end_of_page
            )
            .select(lambda x: x)
            .to_list()
        )

        for index, item in enumerate(data_source):
            if index == 0 and item.text == self.empty_string:
                continue

            if item.text == self.empty_string:
                row_gap = data_source[index].y1 - data_source[index - 1].y2

                if row_gap > row_gap_allowed:
                    end_of_table = data_source[index - 1].y2
                    break

        return end_of_table

    def end_of_table_coord(self, page_no, end_of_page, mandatory_column_coord):
        end_of_table_1 = self.end_of_table_when_text_under_table(page_no, end_of_page,
                                                                 mandatory_column_coord) or end_of_page
        end_of_table_2 = self.end_of_table_when_blank_under_table(page_no, end_of_page,
                                                                  mandatory_column_coord) or end_of_page
        end_of_table = min(end_of_table_1, end_of_table_2)
        return end_of_table

    def end_of_page(self, page_no):
        bottom_of_page = Query(self.pdf_raw_data).where(
            lambda
                x: x.pageNo == page_no).select(
            lambda x: x.y2).order(lambda x: x,
                                  descending=1).first_or_none()
        return bottom_of_page

    def mandatory_column_coordinate(self, column_list, mandatory_column):
        mandatory_column_coord = ItemCoordinate(0, 0, 0, 0)

        column_len = len(column_list)
        for column_index in range(column_len + 1):
            if (column_index + 1) == mandatory_column:
                mandatory_column_coord.x1 = column_list[column_index].coordinateList[0].x1
                mandatory_column_coord.x2 = column_list[column_index].coordinateList[0].x2
                mandatory_column_coord.y1 = column_list[column_index].coordinateList[0].y1
                mandatory_column_coord.y2 = column_list[column_index].coordinateList[0].y2

        return mandatory_column_coord

    def table_header_area(self, column_list):
        x1_list = [column.coordinateList[0].x1 for column in column_list]
        y1_list = [column.coordinateList[0].y1 for column in column_list]
        x2_list = [column.coordinateList[0].x2 for column in column_list]
        y2_list = [column.coordinateList[0].y2 for column in column_list]

        x1 = min(x1_list, default=None)
        y1 = min(y1_list, default=None)
        x2 = max(x2_list, default=None)
        y2 = max(y2_list, default=None)

        return ItemCoordinate(x1, y1, x2, y2)

    def repeating_table_headers(self, table_header_coord: ItemCoordinate, column_list, mandatory_column):
        table_header_items = (
            Query(self.pdf_raw_data)
            .select(lambda x: x)
            .where(
                lambda x: (
                        table_header_coord.y1 <= x.y1
                        and x.y2 <= table_header_coord.y2
                        and len(x.text) >= 3
                        and x.pageNo == self.first_page
                )
            )
            .to_list()
        )

        header_label_list = [obj.text for obj in table_header_items]
        header_coord_list = []

        total_page = (
            Query(self.pdf_raw_data)
            .select(lambda x: x.pageNo)
            .order(lambda x: x, descending=1)
            .first_or_none()
        )

        for index in range(total_page):
            page_no = index + 1

            page_data_without_space = (
                Query(self.pdf_raw_data)
                .select(lambda x: x)
                .where(
                    lambda x: x.pageNo == page_no and x.text != self.empty_string
                )
                .to_list()
            )

            total_word = len(page_data_without_space)
            for idx in range(total_word - 2):
                if (
                        page_data_without_space[idx].text == header_label_list[0]
                        and page_data_without_space[idx + 1].text == header_label_list[1]
                        and page_data_without_space[idx + 2].text == header_label_list[2]
                ):
                    header_item = HeaderCollection(page_no)
                    header_item.coordinate = ItemCoordinate(
                        page_data_without_space[idx].x1,
                        page_data_without_space[idx].y1,
                        page_data_without_space[idx].x2,
                        page_data_without_space[idx].y2,
                    )
                    header_coord_list.append(header_item)
                    break

            found = (
                Query(header_coord_list)
                .select(lambda x: x)
                .where(lambda x: x.pageNo == page_no)
                .first_or_none()
            )

            if found is None:
                mandatory_coord = self.mandatory_column_coord(column_list, mandatory_column)

                query_data = (
                    Query(self.pdf_raw_data)
                    .select(lambda x: x)
                    .where(
                        lambda x: (
                                x.pageNo == page_no
                                and x.x1 > mandatory_coord.x1
                                and x.x2 < mandatory_coord.x2
                        )
                    )
                    .order(lambda x: x.y1, descending=0)
                    .to_list()
                )

                top_y1 = self.find_top_y1(query_data, page_no, column_list)
                if top_y1 != 0:
                    header_item = HeaderCollection(page_no)
                    header_item.coordinate = ItemCoordinate(
                        page_data_without_space[idx].x1,
                        top_y1,
                        page_data_without_space[idx].x2,
                        top_y1,
                    )
                    header_coord_list.append(header_item)

        return header_coord_list
        pass

    def find_top_y1(self, query_data, page_no, column_list):
        sorted_list = []

        for item in query_data:
            limit_top_y1 = item.y1 - 2
            limit_bottom_y1 = item.y1 + 2

            query_data2 = (
                Query(self.pdf_raw_data)
                .select(lambda x: x)
                .where(
                    lambda x: (
                            x.pageNo == page_no
                            and limit_top_y1 <= x.y1 <= limit_bottom_y1
                            and x.text != self.empty_string
                    )
                )
                .order(lambda x: x.y1, descending=0)
                .to_list()
            )

            if len(query_data2) < self.word_frequency:
                continue

            passed = all(
                any(
                    column.coordinateList[0].x1 <= item2.x1 <= column.coordinateList[0].x2
                    for column in column_list
                )
                for item2 in query_data2
            )

            if passed:
                sorted_list.append(item)

        top = (
            Query(sorted_list)
            .select(attrgetter("y1"))
            .order(lambda x: x, descending=0)
            .first_or_none()
        )

        return top - 10 if top is not None else 0

    def mandatory_column_coord(self, column_list, mandatory_column):
        for index in range(len(column_list)):
            if index + 1 == mandatory_column:
                x1 = column_list[index].coordinateList[0].x1
                y1 = column_list[index].coordinateList[0].y1
                x2 = column_list[index].coordinateList[0].x2
                y2 = column_list[index].coordinateList[0].y2
                return ItemCoordinate(x1, y1, x2, y2)
            pass
        pass

    def find_gaps(self, column_list):
        gap_list = []

        for index in range(1, len(column_list)):
            x1 = column_list[index - 1].coordinateList[0].x2
            x2 = column_list[index].coordinateList[0].x1

            if x2 - x1 < 10:
                x2 += 5
                x1 -= 5

            gap_list.append(ItemCoordinate(x1, 0, x2, 0))

        return gap_list

    def print_separator(self, separator=""):
        print("")
        print(separator)
        print("***********************************")
        print("")

    def print_clean_data(self, formatted_clean_data):
        for row in formatted_clean_data:
            if row.column == 1:
                print("")
            print(row.text)
