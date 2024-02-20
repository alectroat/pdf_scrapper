from linq import Query
from operator import attrgetter
from TextCoordinate import ItemCoordinate, HeaderCollection, TextCoordinate, HeaderItemAttribute


class Helper:
    def __init__(self, pdf_raw_data):
        self.word_frequency = 0
        self.row_gap = 0
        self.allowed_row_gap = 0
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
        end_of_table = 0

        data_source = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == page_no
                          and mandatory_column_coord.y2 < x.y1 < end_of_page
                          and x.text != self.empty_string
            )
            .select(lambda x: x)
            .to_list()
        )

        for index, item in enumerate(data_source):
            row_gap = data_source[index].y1 - data_source[index - 1].y2

            if row_gap > self.row_gap:
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
                                  descending=True).first_or_none()
        return bottom_of_page

    def get_table_header_items(self, table_header_coord: ItemCoordinate):
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
        return table_header_items

    def pdf_page_size(self):
        total_page = (
            Query(self.pdf_raw_data)
            .select(lambda x: x.pageNo)
            .order(lambda x: x, descending=True)
            .first_or_none()
        )
        return total_page

    def pdf_page_data_without_space(self, page_no):
        page_data_without_space = (
            Query(self.pdf_raw_data)
            .select(lambda x: x)
            .where(
                lambda x: x.pageNo == page_no and x.text != self.empty_string
            )
            .to_list()
        )
        return page_data_without_space

    def data_inside_mandatory_column_coordinate(self, page_no, mandatory_column_coord):
        query_data = (
            Query(self.pdf_raw_data)
            .select(lambda x: x)
            .where(
                lambda x: (
                        x.pageNo == page_no
                        and x.x1 > mandatory_column_coord.x1
                        and x.x2 < mandatory_column_coord.x2
                )
            )
            .order(lambda x: x.y1, descending=False)
            .to_list())

        return query_data
        pass

    def table_header_bottom(self, y1):
        bottom = (
            Query(self.pdf_raw_data)
            .select(lambda x: x)
            .where(
                lambda x: (
                        x.y1 < (y1 - 15)
                        and x.text != self.empty_string
                )
            )
            .order(lambda x: x.y1, descending=True)
            .first_or_none())

        return bottom.y1 if bottom is not None else 0
        pass

    def repeating_table_headers(self, table_header_coord: ItemCoordinate, column_list, mandatory_column):
        table_header_items = self.get_table_header_items(table_header_coord)
        header_label_list = [obj for obj in table_header_items]
        total_page = self.pdf_page_size()
        header_coord_list = []

        for index in range(total_page):
            page_no = index + 1

            page_data_without_space = self.pdf_page_data_without_space(page_no)
            total_word = len(page_data_without_space)

            if len(header_label_list) == 0:
                header_item = HeaderCollection(page_no)
                header_item.coordinate = table_header_coord
                header_coord_list.append(header_item)
                continue

            elif len(header_label_list) == 2:
                for idx in range(total_word - 1):
                    if (
                            header_label_list[0].text in page_data_without_space[idx].text
                            and header_label_list[1].text in page_data_without_space[idx + 1].text
                    ):
                        header_item = HeaderCollection(page_no)

                        y1 = header_label_list[0].y1
                        y2 = header_label_list[0].y2

                        header_item.headerItemAttribute = HeaderItemAttribute(y2 - y1, table_header_coord.y2 - y2)

                        header_item.coordinate = ItemCoordinate(
                            page_data_without_space[idx].x1,
                            page_data_without_space[idx].y1,
                            page_data_without_space[idx].x2,
                            page_data_without_space[idx].y2,
                        )
                        header_coord_list.append(header_item)
                        break
                pass
            else:
                for idx in range(total_word - 2):
                    if (
                            header_label_list[0].text in page_data_without_space[idx].text
                            and header_label_list[1].text in page_data_without_space[idx + 1].text
                            and header_label_list[2].text in page_data_without_space[idx + 2].text
                    ):
                        header_item = HeaderCollection(page_no)

                        y1 = header_label_list[0].y1
                        y2 = header_label_list[0].y2

                        header_item.headerItemAttribute = HeaderItemAttribute(y2 - y1, table_header_coord.y2 - y2)

                        header_item.coordinate = ItemCoordinate(
                            page_data_without_space[idx].x1,
                            page_data_without_space[idx].y1,
                            page_data_without_space[idx].x2,
                            page_data_without_space[idx].y2,
                        )
                        header_coord_list.append(header_item)
                        break
                pass

            if Helper.check_for_table_header_by_page(header_coord_list, page_no) is None:

                mandatory_column_coordinate = Helper.mandatory_column_coordinate(column_list, mandatory_column)
                mandatory_column_data = self.data_inside_mandatory_column_coordinate(page_no,
                                                                                     mandatory_column_coordinate)
                top_left_y = self.find_top_left_y(mandatory_column_data, page_no, column_list)

                if top_left_y != 0:
                    header_item = HeaderCollection(page_no)
                    header_item.coordinate = ItemCoordinate(
                        page_data_without_space[idx].x1,
                        top_left_y,
                        page_data_without_space[idx].x2,
                        top_left_y,
                    )
                    header_coord_list.append(header_item)

        return header_coord_list

    def data_in_a_line(self, page_no, limit_top_y1, limit_bottom_y1):
        query_data = (
            Query(self.pdf_raw_data)
            .select(lambda x: x)
            .where(
                lambda x: (
                        x.pageNo == page_no
                        and limit_top_y1 <= x.y1 <= limit_bottom_y1
                        and x.text != self.empty_string
                )
            )
            .order(lambda x: x.y1, descending=False)
            .to_list()
        )
        return query_data

    def get_data_that_satisfy(self, mandatory_column_data, page_no, column_list):
        sorted_list = []

        for item in mandatory_column_data:
            limit_top_y1 = item.y1 - 2
            limit_bottom_y1 = item.y1 + 2

            data_in_a_line = self.data_in_a_line(page_no, limit_top_y1, limit_bottom_y1)

            if len(data_in_a_line) < self.word_frequency:
                continue

            passed = all(
                any(
                    column.coordinateList[0].x1 <= item.x1 <= column.coordinateList[0].x2
                    for column in column_list
                )
                for item in data_in_a_line
            )

            if passed:
                sorted_list.append(item)
        return sorted_list

    def find_top_left_y(self, mandatory_column_data, page_no, column_list):
        sorted_list = self.get_data_that_satisfy(mandatory_column_data, page_no, column_list)

        top = (
            Query(sorted_list)
            .select(attrgetter("y1"))
            .order(lambda x: x, descending=False)
            .first_or_none()
        )

        return top - 10 if top is not None else 0

    def find_bottom_right_y(self, mandatory_column_data, page_no, column_list):
        sorted_list = self.get_data_that_satisfy(mandatory_column_data, page_no, column_list)

        top = (
            Query(sorted_list)
            .select(attrgetter("y2"))
            .order(lambda x: x, descending=True)
            .first_or_none()
        )

        return top + 10 if top is not None else 0

    def table_bottom_by_page(self, page_no, column_list, coordinate):
        data_source = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == page_no
                          and coordinate.y1 < x.y1
                          and x.text != self.empty_string
            )
            .select(lambda x: x)
            .order(lambda x: x.y1, descending=False)
            .to_list()
        )

        item_ = None

        for index, item in enumerate(data_source):
            if not Helper.check_item_inside_table(item, column_list) or (
                    item_ and (item.y1 - item_.y2) > self.row_gap):
                break
            else:
                item_ = item

        data_source = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == page_no
                          and item_.y1 > x.y1
                          and x.text == self.empty_string
            )
            .select(lambda x: x)
            .order(lambda x: x.y1, descending=True)
            .first_or_none()
        )

        return data_source.y2 if data_source is not None else 0

    def calculate_allowed_gap(self, header_coordinate):
        # maximum_allowed_row_gap = 145
        first_row_first_word = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == 1
                          and x.y1 > header_coordinate.y2
                          and x.text != self.empty_string
            )
            .select(lambda x: x)
            .order(lambda x: x.y1, descending=False)
            .first_or_none()
        )

        second_row_first_word = (
            Query(self.pdf_raw_data)
            .where(
                lambda x: x.pageNo == 1
                          and x.y1 > first_row_first_word.y2
                          and x.text != self.empty_string
            )
            .select(lambda x: x)
            .order(lambda x: x.y1, descending=False)
            .first_or_none()
        )

        if first_row_first_word is None or second_row_first_word is None or (
                second_row_first_word.y1 - first_row_first_word.y2) > self.allowed_row_gap:
            return 0
        return (second_row_first_word.y1 - first_row_first_word.y2) * 1 + 20

    @staticmethod
    def check_item_inside_table(item, column_list):
        passed = any(
            column.coordinateList[0].x1 <= item.x1 <= column.coordinateList[0].x2
            for column in column_list
        )
        return passed

    @staticmethod
    def check_item_inside_columns(item, column_list):
        passed = any(
            item.x1 >= column.coordinateList[0].x1 and item.x2 <= column.coordinateList[0].x2
            for column in column_list
        )
        return passed

    @staticmethod
    def mandatory_column_coordinate(column_list, mandatory_column):
        coordinate = ItemCoordinate(0, 0, 0, 0)

        column_len = len(column_list)
        for column_index in range(column_len + 1):
            if (column_index + 1) == mandatory_column:
                coordinate.x1 = column_list[column_index].coordinateList[0].x1
                coordinate.x2 = column_list[column_index].coordinateList[0].x2
                coordinate.y1 = column_list[column_index].coordinateList[0].y1
                coordinate.y2 = column_list[column_index].coordinateList[0].y2

        return coordinate

    @staticmethod
    def find_gaps(column_list):
        gap_list = []

        for index in range(1, len(column_list)):
            x1 = column_list[index - 1].coordinateList[0].x2
            x2 = column_list[index].coordinateList[0].x1

            if x2 - x1 < 10:
                x2 += 5
                x1 -= 5

            gap_list.append(ItemCoordinate(x1, 0, x2, 0))

        return gap_list

    @staticmethod
    def check_for_table_header_by_page(header_coord_list, page_no):
        found = (
            Query(header_coord_list)
            .select(lambda x: x)
            .where(lambda x: x.pageNo == page_no)
            .first_or_none()
        )
        return found

    @staticmethod
    def table_header_area(column_list):
        x1_list = [column.coordinateList[0].x1 for column in column_list]
        y1_list = [column.coordinateList[0].y1 for column in column_list]
        x2_list = [column.coordinateList[0].x2 for column in column_list]
        y2_list = [column.coordinateList[0].y2 for column in column_list]

        x1 = min(x1_list, default=None)
        y1 = min(y1_list, default=None)
        x2 = max(x2_list, default=None)
        y2 = max(y2_list, default=None)

        return ItemCoordinate(x1, y1, x2, y2)

    @staticmethod
    def build_coordinate(coordinate):
        return ItemCoordinate(coordinate.x1,
                              coordinate.y1,
                              coordinate.x2,
                              coordinate.y2)

    @staticmethod
    def calculate_y2_from_y1(header):
        y2 = (header.coordinate.y1 +
              header.headerItemAttribute.height +
              header.headerItemAttribute.padding_bottom)
        return y2

    @staticmethod
    def print_separator():
        print("***********************************")
        print("")

    @staticmethod
    def print_clean_data(formatted_clean_data):
        for row in formatted_clean_data:
            if row.column == 1:
                print("")
            # print(row.column, " ", row.text)
            print(row.text)

    @staticmethod
    def print_data(obj: TextCoordinate):
        print(f'{obj.text: <41}', f'{obj.pageNo: <5}',
              f'{obj.lineNo: <5}'
              , f'{obj.x1: <5}', f'{obj.y1: <5}', f'{obj.x2: <5}', f'{obj.y2: <5}')
