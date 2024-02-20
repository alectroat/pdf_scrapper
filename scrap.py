import os
from linq import Query
from TextCoordinate import ItemCoordinate, Item, TableRegion
from convert_table_data_to_json import ConvertTableDataToJson
from helper import Helper
from library import Main
from PdfCollection import PdfCollection


class Scrapper:
    library_object = Main()
    extracted: bool = True
    empty_string = ""

    def __init__(self, pdf_serial_no_):
        self.pdf_serial_no = pdf_serial_no_

        self.pdf_property = PdfCollection().find_by_id(self.pdf_serial_no)
        self.pdf_path = self.pdf_property.pdf_path
        self.mandatory_column = self.pdf_property.mandatory_column
        self.column_list = self.pdf_property.column_list

        self.pdf_raw_data = Scrapper.library_object.ExtractDataFromPdf(self.pdf_path)

        self.helper = Helper(self.pdf_raw_data)
        self.helper.row_gap = self.pdf_property.row_gap
        self.helper.allowed_row_gap = self.pdf_property.allowed_row_gap
        self.helper.word_frequency = self.pdf_property.word_frequency

        self.table_list: list = []
        self.data_storage: list = []
        self.formatted_data = []
        self.formatted_clean_data = []

    def print_pdf_path(self):
        print("")
        print("***********************************")
        print(self.pdf_path)

    def print_pdf_raw_data(self):
        for obj in self.pdf_raw_data:
            Helper.print_data(obj)

    def read_table_data(self):
        self.data_storage.clear()

        # self.print_pdf_raw_data()

        table_header_coordinate = Helper.build_coordinate(Helper.table_header_area(self.column_list))
        table_headers: [] = self.helper.repeating_table_headers(table_header_coordinate, self.column_list,
                                                                self.mandatory_column)
        self.helper.row_gap = self.helper.calculate_allowed_gap(table_header_coordinate)

        for index in range(len(table_headers)):

            header_found = table_headers[index].coordinate.y1 != table_headers[index].coordinate.y2
            if header_found:
                table_headers[index].coordinate.y2 = Helper.calculate_y2_from_y1(table_headers[index])

            table_header_coordinate = Helper.build_coordinate(table_headers[index].coordinate)
            page_no = table_headers[index].pageNo
            end_of_page = self.helper.end_of_page(page_no)

            bottom1 = (self.helper.table_bottom_by_page(page_no, self.column_list, table_header_coordinate)
                       or end_of_page)
            bottom2 = self.helper.end_of_table_when_blank_under_table(page_no,
                                                                      end_of_page,
                                                                      table_header_coordinate) or end_of_page

            bottom = max(bottom1, bottom2)
            table_end_coordinate = ItemCoordinate(0, bottom, 0, 0)
            table_region: TableRegion = TableRegion(table_header_coordinate, table_end_coordinate)
            # print(" bottom1 ", bottom1, " bottom2 ", bottom2, " end ", end_of_page, " Y1 ",
            #       table_header_coordinate.y1, " Y2 ", bottom)

            self.collect_table_data(page_no, table_region)

        self.store_in_data_structure()
        self.make_data_readable()
        self.prepare_formatted_clean_data()
        Helper.print_separator()
        Helper.print_clean_data(self.formatted_clean_data)
        pass

    def collect_table_data(self, page_no, table_region):
        row: list = []

        row_wise_data_collection = Query(self.pdf_raw_data).select(lambda x: x).where(
            lambda x: x.pageNo == page_no
                      and table_region.top.y2 < x.y1 <= table_region.bottom.y1).to_list()

        # print("")
        # selected_column_data = []
        # for column in self.column_list:
        #     data = Query(row_wise_data_collection).select(lambda x: x).where(
        #         lambda x: x.pageNo == page_no
        #         and x.x1 >= column.coordinateList[0].x1 and x.x2 <= column.coordinateList[0].x2).to_list()
        #     for item in data:
        #         selected_column_data.append(item)
        #
        # row_wise_data_collection = selected_column_data

        last_index_of_area = len(row_wise_data_collection) - 1
        for index in range(len(row_wise_data_collection)):
            # if not self.helper.check_item_inside_columns(row_wise_data_collection[index], self.column_list):
            #     continue

            if row_wise_data_collection[index].text == Scrapper.empty_string:
                row = []
            else:
                row.append(row_wise_data_collection[index])
                next_word_index = index + 1
                if ((next_word_index <= last_index_of_area
                     and row_wise_data_collection[next_word_index].text == Scrapper.empty_string)
                        or (index == last_index_of_area)):
                    self.data_storage.append(row)
        pass

    def store_in_data_structure(self):
        for row_index, row_data in enumerate(self.data_storage):

            item_list = []
            column_len = len(self.column_list)

            for column_index in range(1, column_len + 1):
                if column_index == column_len:
                    query_data = Query(row_data).select(lambda x: x).where(
                        lambda x: not x.extracted).to_list()
                else:
                    ref_header_x = self.column_list[column_index].coordinateList[0].x1
                    query_data = Query(row_data).select(lambda x: x).where(
                        lambda x: x.x2 < ref_header_x and not x.extracted).to_list()

                item_list.append(self.create_item(row_index, column_index, query_data))

            self.table_list.append(item_list)

    @staticmethod
    def create_item(row_index, column_index, query_data):
        item = Item(row_index, column_index, [])
        for child_index, child in enumerate(query_data):
            child.extracted = Scrapper.extracted
            item.data.append(child.text)
            if child_index == 0:
                item.coordinate = ItemCoordinate(child.x1, child.y1, child.x2, child.y2)
        return item

    def make_data_readable(self):
        for obj in self.table_list:
            for data in obj:
                data.text = " ".join(data.data)

    def remove_empty_text(self):
        self.formatted_data = [data for obj in self.table_list for data in obj if data.text != Scrapper.empty_string]

    def prepare_formatted_clean_data(self):
        self.remove_empty_text()

        ref_row = 0
        for row in self.formatted_data:
            if row.row == 0:
                continue

            # check if mandatory column is missing
            query_data = Query(self.formatted_data).where(
                lambda x: x.row == row.row and x.column == self.mandatory_column).select(lambda x: x).to_list()

            if len(query_data) == 0:
                data = Query(self.formatted_data).where(
                    lambda x: x.row == ref_row and x.column == row.column).select(lambda x: x).first_or_none()

                if data is not None:
                    data.text += f" {row.text}"
                    row.deleted = True
                pass
            else:
                ref_row = row.row

        self.formatted_clean_data = [row for row in self.formatted_data if not row.deleted]

        pass

    def table_end(self, page_no):
        coordinate = Helper.mandatory_column_coordinate(self.column_list, self.mandatory_column)
        mandatory_column_coord = ItemCoordinate(coordinate.x1, coordinate.y1, coordinate.x2, coordinate.y2)
        end_of_page = self.helper.end_of_page(page_no)
        return self.helper.end_of_table_coord(page_no, end_of_page,
                                              mandatory_column_coord)
        pass

    def save_into_excel(self):
        filename_without_ext = os.path.splitext(os.path.basename(self.pdf_path))[0]
        xlsx_filename = filename_without_ext + ".xlsx"
        convert_table_data_to_json = ConvertTableDataToJson([header.text for header in self.column_list],
                                                            self.formatted_clean_data)
        convert_table_data_to_json.to_excel(os.path.basename(xlsx_filename))
        pass
