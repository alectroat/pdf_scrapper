from linq import Query

from TextCoordinate import ItemCoordinate, HeaderCollection, GapCollection


class Helper:
    def __init__(self):
        self.word_frequency = 8
        self.empty_string = ""
        pass

    def end_of_table_coord(self, page_no, pdf_raw_data, end_of_page, MandatoryColumnCoordinate,
                           EndOfTableCoordinate):
        row_gap_allowed = 45
        end_of_table_1 = 0
        end_of_table_2 = 0

        dada_inside_certain_height = Query(pdf_raw_data).where(
            lambda
                x: x.pageNo == page_no and MandatoryColumnCoordinate.y2 < x.y1 < end_of_page and x.text != self.empty_string).select(
            lambda x: x).to_list()

        data_source = Query(pdf_raw_data).where(
            lambda
                x: x.pageNo == page_no and MandatoryColumnCoordinate.y2 < x.y1 < end_of_page).select(
            lambda x: x).to_list()

        for index in range(len(dada_inside_certain_height)):
            if dada_inside_certain_height[index].x1 < MandatoryColumnCoordinate.x2 < dada_inside_certain_height[
                index].x2:
                end_of_table_1 = dada_inside_certain_height[index].y1
                break

        for index in range(len(data_source)):
            if index == 0 and data_source[index].text == "":
                continue
            if data_source[index].text == "":
                row_gap = data_source[index].y1 - data_source[index - 1].y2
                if row_gap > row_gap_allowed:
                    end_of_table_2 = data_source[index - 1].y2
                    break

        end_of_table = min(end_of_table_1, end_of_table_2)

        if end_of_table == 0:
            end_of_table = end_of_page

        return end_of_table
        pass

    def end_of_page(self, pdf_raw_data, page_no, MandatoryColumnCoordinate):
        bottom_of_page = Query(pdf_raw_data).where(
            lambda
                x: x.pageNo == page_no).select(
            lambda x: x.y2).order(lambda x: x,
                                  descending=1).first_or_none()
        return bottom_of_page

    def mandatory_column_coordinate(self, ColumnList, mandatory_column):
        MandatoryColumnCoordinate = ItemCoordinate(0, 0, 0, 0)

        column_len = len(ColumnList)
        for column_index in range(column_len + 1):
            if (column_index + 1) == mandatory_column:
                MandatoryColumnCoordinate.x1 = ColumnList[column_index].coordinateList[0].x1
                MandatoryColumnCoordinate.x2 = ColumnList[column_index].coordinateList[0].x2
                MandatoryColumnCoordinate.y1 = ColumnList[column_index].coordinateList[0].y1
                MandatoryColumnCoordinate.y2 = ColumnList[column_index].coordinateList[0].y2

        return MandatoryColumnCoordinate

    def table_header_area(self, column_list):
        x1_list = []
        y1_list = []
        x2_list = []
        y2_list = []
        for index in range(len(column_list)):
            x1_list.append(column_list[index].coordinateList[0].x1)
            y1_list.append(column_list[index].coordinateList[0].y1)
            x2_list.append(column_list[index].coordinateList[0].x2)
            y2_list.append(column_list[index].coordinateList[0].y2)
            pass

        x1 = Query(x1_list).select(lambda x: x).order(lambda x: x,
                                                      descending=0).first_or_none()
        y1 = Query(y1_list).select(lambda x: x).order(lambda x: x,
                                                      descending=0).first_or_none()
        x2 = Query(x2_list).select(lambda x: x).order(lambda x: x,
                                                      descending=1).first_or_none()
        y2 = Query(y2_list).select(lambda x: x).order(lambda x: x,
                                                      descending=1).first_or_none()

        return ItemCoordinate(x1, y1, x2, y2)
        pass

    def repeating_table_headers(self, pdf_raw_data, table_header_coord: ItemCoordinate, column_list, mandatory_column):
        first_page = 1
        table_header_items = Query(pdf_raw_data).select(lambda x: x).where(
            lambda x: table_header_coord.y1 <= x.y1 and x.y2 <= table_header_coord.y2 and len(
                x.text) >= 3 and x.pageNo == first_page).to_list()

        header_label_list = []
        header_coord_list = []

        for obj in table_header_items:
            header_label_list.append(obj.text)

        total_page = Query(pdf_raw_data).select(lambda x: x.pageNo).order(lambda x: x,
                                                                          descending=1).first_or_none()
        for index in range(total_page):
            page_no = index + 1

            page_data_without_space = Query(pdf_raw_data).select(lambda x: x).where(
                lambda x: x.pageNo == page_no and x.text != self.empty_string).to_list()
            total_word = len(page_data_without_space)
            for idx in range(total_word):
                if idx + 2 <= total_word:
                    if page_data_without_space[idx].text == header_label_list[0] and page_data_without_space[
                        idx + 1].text == header_label_list[1] and \
                            page_data_without_space[idx + 2].text == header_label_list[2]:
                        header_item = HeaderCollection(page_no)
                        header_item.coordinate = ItemCoordinate(page_data_without_space[idx].x1,
                                                                page_data_without_space[idx].y1,
                                                                page_data_without_space[idx].x2,
                                                                page_data_without_space[idx].y2)
                        header_coord_list.append(header_item)
                        break
                    pass
                pass

            found = Query(header_coord_list).select(lambda x: x).where(
                lambda x: x.pageNo == page_no).first_or_none()

            if found is None:
                mandatory_coord = self.mandatory_column_coord(column_list, mandatory_column)

                query_data = pdf_raw_data
                query_data2 = Query(query_data).select(lambda x: x).where(
                    lambda x: x.pageNo == page_no and x.x1 > mandatory_coord.x1 and x.x2 < mandatory_coord.x2).order(
                    lambda x: x.y1,
                    descending=0).to_list()

                y1 = self.data_from_same_height(query_data2, pdf_raw_data, page_no, column_list)
                if y1 != 0:
                    header_item = HeaderCollection(page_no)
                    header_item.coordinate = ItemCoordinate(page_data_without_space[idx].x1,
                                                            y1,
                                                            page_data_without_space[idx].x2,
                                                            y1)
                    header_coord_list.append(header_item)
                    pass
        return header_coord_list
        pass

    def data_from_same_height(self, query_data, pdf_raw_data, page_no, column_list):

        sorted_list = []

        for index in range(len(query_data)):

            limit_top_y1 = query_data[index].y1 - 2
            limit_bottom_y1 = query_data[index].y1 + 2

            query_data2 = Query(pdf_raw_data).select(lambda x: x).where(
                lambda
                    x: x.pageNo == page_no and limit_top_y1 <= x.y1 <= limit_bottom_y1 and x.text != self.empty_string).order(
                lambda x: x.y1,
                descending=0).to_list()

            passed = False

            if len(query_data2) < self.word_frequency:
                continue

            for idx in range(len(query_data2)):
                passed = False
                for column_index in range(len(column_list)):
                    x1 = column_list[column_index].coordinateList[0].x1
                    x2 = column_list[column_index].coordinateList[0].x2
                    if query_data2[idx].x1 >= x1 and query_data2[idx].x2 <= x2:
                        passed = True
                        break
                    pass
                if not passed:
                    break

            if passed:
                sorted_list.append(query_data[index])

        top = Query(sorted_list).select(lambda x: x.y1).order(
            lambda x: x,
            descending=0).first_or_none()

        if top is None:
            y1 = 0
        else:
            y1 = top - 10
        print(" y1 ", y1)
        return y1
        pass

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
        column_len = len(column_list)
        gap_list = []
        print("")
        for index in range(column_len):
            if index == 0:
                pass
            else:
                x1 = column_list[index - 1].coordinateList[0].x2
                x2 = column_list[index].coordinateList[0].x1

                if x2 - x1 >= 10:
                    pass
                else:
                    x2 += 5
                    x1 -= 5
                    pass

                gap_list.append(ItemCoordinate(x1, 0, x2, 0))
                # print(" x1 : ", x1, " x2 : ", x2)
                pass
        return gap_list
        pass

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
