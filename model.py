import os

from linq import Query

from TextCoordinate import ItemCoordinate, HeaderList, Item, TableRegion
from convert_table_data_to_json import ConvertTableDataToJson
from helper import Helper
from library import Main
from PdfCollection import PdfCollection
from scrap import Scrapper

Item_list: list = []
table_list: list = []
item = None
data_storage: list = []
formatted_data = []
formatted_clean_data = []

pdf_no = 10

pdf_property = PdfCollection().find_by_id(pdf_no)
pdf_path = pdf_property.pdf_path
mandatory_column = pdf_property.mandatory_column
column_list = pdf_property.column_list

print("")
print("***********************************")
print("")
print("")
print(pdf_path)

classObject = Main()
pdf_raw_data: [] = classObject.ExtractDataFromPdf(pdf_path)
HelperObject = Helper(pdf_raw_data)

table_end_coordinate = ItemCoordinate(0, 0, 0, 0)


def print_pdf_raw_data():
    for obj in pdf_raw_data:
        classObject.PrintData(obj)


def read_table_data():
    data_storage.clear()
    adjustment_height = 45

    # print_pdf_raw_data()

    coord: ItemCoordinate = HelperObject.table_header_area(column_list)
    table_header_coordinate = ItemCoordinate(coord.x1, coord.y1, coord.x2, coord.y2)
    header_coordinate_list: [] = HelperObject.repeating_table_headers(table_header_coordinate, column_list,
                                                                      mandatory_column)

    table_header_width = table_header_coordinate.x2 - table_header_coordinate.x1
    table_header_height = table_header_coordinate.y2 - table_header_coordinate.y1 - adjustment_height

    for index in range(len(header_coordinate_list)):
        header_coordinate_list[index].coordinate.x2 = header_coordinate_list[index].coordinate.x1 + table_header_width
        if index == 0:
            header_coordinate_list[index].coordinate.y2 = header_coordinate_list[
                                                              index].coordinate.y1 + table_header_height
            pass
        else:
            header_coordinate_list[index].coordinate.y2 = header_coordinate_list[index].coordinate.y1
            pass

        table_end_coordinate.y1 = end_of_table_y1(header_coordinate_list[index].pageNo)
        table_region: TableRegion = TableRegion(ItemCoordinate(header_coordinate_list[index].coordinate.x1,
                                                               header_coordinate_list[index].coordinate.y1,
                                                               header_coordinate_list[index].coordinate.x2,
                                                               header_coordinate_list[index].coordinate.y2),
                                                ItemCoordinate(table_end_coordinate.x1,
                                                               table_end_coordinate.y1,
                                                               table_end_coordinate.x2,
                                                               table_end_coordinate.y2)
                                                )
        collect_table_data(header_coordinate_list[index].pageNo, table_region)

    store_in_data_structure()
    make_data_readable()
    prepare_formatted_clean_data()
    HelperObject.print_separator()
    HelperObject.print_clean_data(formatted_clean_data)
    pass


def collect_table_data(page_no, table_region):
    row: list = []
    row_separator = ""
    row_wise_data_collection = Query(pdf_raw_data).select(lambda x: x).where(
        lambda x: x.pageNo == page_no and table_region.top.y2 < x.y1 <= table_region.bottom.y1).to_list()

    last_index_of_area = len(row_wise_data_collection) - 1

    for index in range(len(row_wise_data_collection)):
        if row_wise_data_collection[index].text == row_separator:
            row = []
        else:
            row.append(row_wise_data_collection[index])
            next_word_index = index + 1
            if (next_word_index <= last_index_of_area and row_wise_data_collection[
                next_word_index].text == row_separator) or (index == last_index_of_area):
                data_storage.append(row)

    pass


def store_in_data_structure():
    extracted: bool = True
    for row_index in range(len(data_storage)):
        column_len = len(column_list)
        item_list = []
        for column_index in range(column_len + 1):
            # First Iteration
            if column_index == 0:
                continue
            # Last Iteration
            # push to the list the remaining words
            elif column_index == column_len:
                item = Item(row_index, column_index, [])
                query_data = Query(data_storage[row_index]).select(lambda x: x).where(
                    lambda x: not x.extracted).to_list()

                for child_index in range(len(query_data)):
                    child = query_data[child_index]
                    child.extracted = extracted
                    item.data.append(child.text)
                    if child_index == 0:
                        item.coordinate = ItemCoordinate(child.x1, child.y1, child.x2, child.y2)
                item_list.append(item)
            # restrict words by coordinates
            else:
                item = Item(row_index, column_index, [])
                ref_header_x = column_list[column_index].coordinateList[0].x1

                query_data = Query(data_storage[row_index]).select(lambda x: x).where(
                    lambda x: x.x2 < ref_header_x and not x.extracted).to_list()

                for child_index in range(len(query_data)):
                    child = query_data[child_index]
                    child.extracted = extracted
                    item.data.append(child.text)
                    if child_index == 0:
                        item.coordinate = ItemCoordinate(child.x1, child.y1, child.x2, child.y2)
                item_list.append(item)
        table_list.append(item_list)


def make_data_readable():
    for obj in table_list:
        for data in obj:
            data.text = ""
            for text in data.data:
                data.text += " " + text


def remove_empty_text():
    empty_string = ""
    formatted_data.clear()
    for obj in table_list:
        for data in obj:
            if data.text != empty_string:
                formatted_data.append(data)
                pass


def prepare_formatted_clean_data():
    remove_empty_text()

    ref_row = 0
    for row in formatted_data:
        if row.row == 0:
            continue
        else:
            # check if mandatory column is missing
            query_data = Query(formatted_data).where(
                lambda x: x.row == row.row and x.column == mandatory_column).select(lambda x: x).to_list()

            if len(query_data) == 0:
                data = Query(formatted_data).where(
                    lambda x: x.row == ref_row and x.column == row.column).select(lambda x: x).first_or_none()
                if data is not None:
                    data.text += row.text
                    row.deleted = True
                pass
            else:
                ref_row = row.row
            pass
        pass
    pass

    for row in formatted_data:
        if not row.deleted:
            formatted_clean_data.append(row)

    pass


def end_of_table_y1(page_no=1):
    coordinate = HelperObject.mandatory_column_coordinate(column_list, mandatory_column)
    mandatory_column_coord = ItemCoordinate(coordinate.x1, coordinate.y1, coordinate.x2, coordinate.y2)
    end_of_page = HelperObject.end_of_page(page_no)
    return HelperObject.end_of_table_coord(page_no, end_of_page,
                                           mandatory_column_coord)
    pass


scrapper = Scrapper(10)
scrapper.read_table_data()

# read_table_data()
# filename_without_ext = os.path.splitext(os.path.basename(pdf_path))[0]
# xlsx_filename = filename_without_ext + ".xlsx"
# convert_table_data_to_json = ConvertTableDataToJson([header.text for header in column_list],
#                                                     formatted_clean_data)
# convert_table_data_to_json.to_excel(os.path.basename(xlsx_filename))
