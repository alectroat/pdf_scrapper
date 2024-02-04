from linq import Query
from TextCoordinate import TextCoordinate, ItemCoordinate, HeaderList, Item, HeaderCollection, TableRegion


class Helper:
    def __init__(self):
        pass

    def end_of_table_coord(self, page_no, pdf_raw_data, end_of_page, MandatoryColumnCoordinate,
                           EndOfTableCoordinate):
        row_gap_allowed = 150
        empty_string = ""
        end_of_table_1 = 0
        end_of_table_2 = 0
        end_of_table = 0

        dada_inside_certain_height = Query(pdf_raw_data).where(
            lambda
                x: x.pageNo == page_no and MandatoryColumnCoordinate.y2 < x.y1 < end_of_page and x.text != empty_string).select(
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

        if end_of_table_1 < end_of_table_2:
            end_of_table = end_of_table_1
        else:
            end_of_table = end_of_table_2

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

    def table_header_area(self, ColumnList):
        x1_list = []
        y1_list = []
        x2_list = []
        y2_list = []
        for index in range(len(ColumnList)):
            x1_list.append(ColumnList[index].coordinateList[0].x1)
            y1_list.append(ColumnList[index].coordinateList[0].y1)
            x2_list.append(ColumnList[index].coordinateList[0].x2)
            y2_list.append(ColumnList[index].coordinateList[0].y2)
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

    def repeating_table_headers(self, pdf_raw_data, TableHeaderCoordinate: ItemCoordinate):

        table_header_items = Query(pdf_raw_data).select(lambda x: x).where(
            lambda x: TableHeaderCoordinate.y1 <= x.y1 and x.y2 <= TableHeaderCoordinate.y2 and len(
                x.text) >= 3 and x.pageNo == 1).to_list()

        headerLabelList = []
        HeaderCoordinateList = []
        empty_string = ""

        for obj in table_header_items:
            headerLabelList.append(obj.text)

        pdf_raw_data_without_space = Query(pdf_raw_data).select(lambda x: x).where(
            lambda x: x.text != empty_string).to_list()

        total_word = len(pdf_raw_data_without_space)

        for index in range(total_word):
            if index + 2 <= total_word:
                if pdf_raw_data_without_space[index].text == headerLabelList[0] and pdf_raw_data_without_space[
                    index + 1].text == headerLabelList[1] and \
                        pdf_raw_data_without_space[index + 2].text == headerLabelList[2]:
                    header_item = HeaderCollection(pdf_raw_data_without_space[index].pageNo)
                    header_item.coordinate = ItemCoordinate(pdf_raw_data_without_space[index].x1,
                                                            pdf_raw_data_without_space[index].y1,
                                                            pdf_raw_data_without_space[index].x2,
                                                            pdf_raw_data_without_space[index].y2)
                    HeaderCoordinateList.append(header_item)
                    pass
                pass
            pass

        return HeaderCoordinateList
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
