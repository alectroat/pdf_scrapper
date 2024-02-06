from linq import Query
from TextCoordinate import TextCoordinate, ItemCoordinate, HeaderList, Item, HeaderCollection, TableRegion
from library import Main
from helper import Helper
from convert_table_data_to_json import ConvertTableDataToJson
import os


Item_list: list = []
table_list: list = []
item = None
data_storage: list = []
formatted_data = []
formatted_clean_data = []

# pdf_path = "Sample documents/New folder/123 Ink.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "QUANTITY", [ItemCoordinate(144, 1076, 380, 1111)]),
#     HeaderList(2, "SKU", [ItemCoordinate(373, 1063, 673, 1108)]),
#     HeaderList(3, "DESCRIPTION", [ItemCoordinate(673, 1063, 1646, 1111)]),
#     HeaderList(4, "VAT", [ItemCoordinate(1659, 1063, 1843, 1105)]),
#     HeaderList(5, "UNIT PRICE", [ItemCoordinate(1846, 1066, 2091, 1111)]),
#     HeaderList(6, "TOTAL", [ItemCoordinate(2091, 1063, 2339, 1101)])
# ]

# pdf_path = "Sample documents/New folder/ACP Limited.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "Quality", [ItemCoordinate(128, 1249, 357, 1339)]),
#     HeaderList(2, "Description", [ItemCoordinate(360, 1243, 1278, 1336)]),
#     HeaderList(3, "Unit Price", [ItemCoordinate(1301, 1246, 1684, 1333)]),
#     HeaderList(4, "Net Amt", [ItemCoordinate(1694, 1243, 1935, 1336)]),
#     HeaderList(5, "VAT %", [ItemCoordinate(1945, 1246, 2167, 1336)]),
#     HeaderList(6, "VAT", [ItemCoordinate(2177, 1249, 2360, 1339)])
# ]

pdf_path = "Sample documents/New folder/M. KELLIHER 1998 Ltd. 3 Page.pdf"
mandatory_column = 1
ColumnList = [
    HeaderList(1, "Item Number", [ItemCoordinate(109, 1554, 467, 1620)]),
    HeaderList(2, "Config No.", [ItemCoordinate(477, 1557, 712, 1617)]),
    HeaderList(3, "Description", [ItemCoordinate(712, 1561, 1289, 1620)]),
    HeaderList(4, "Qty", [ItemCoordinate(1295, 1567, 1395, 1617)]),
    HeaderList(5, "Net selling price", [ItemCoordinate(1398, 1464, 1597, 1617)]),
    HeaderList(6, "Unit", [ItemCoordinate(1607, 1534, 1769, 1617)]),
    HeaderList(6, "VAT", [ItemCoordinate(1783, 1551, 1938, 1614)]),
    HeaderList(6, "WEEE", [ItemCoordinate(1952, 1554, 2131, 1617)]),
    HeaderList(6, "Net Total", [ItemCoordinate(2134, 1557, 2326, 1614)]),
]

# pdf_path = "Sample documents/New folder/AccurA Diamond Tools Ltd.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "Qty", [ItemCoordinate(135, 1265, 251, 1326)]),
#     HeaderList(2, "Code", [ItemCoordinate(280, 1259, 560, 1317)]),
#     HeaderList(3, "Product Description", [ItemCoordinate(570, 1259, 1307, 1314)]),
#     HeaderList(4, "Unit Price", [ItemCoordinate(1333, 1265, 1732, 1314)]),
#     HeaderList(5, "Net Amount", [ItemCoordinate(1742, 1268, 2064, 1314)]),
#     HeaderList(6, "VAT Amount", [ItemCoordinate(2087, 1259, 2373, 1317)])
# ]

# pdf_path = "Sample documents/New folder/Thomas Archer (Ballina) 2 Page.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "Item Code", [ItemCoordinate(74, 1198, 354, 1307)]),
#     HeaderList(2, "Description", [ItemCoordinate(376, 1201, 1101, 1310)]),
#     HeaderList(3, "Quantity", [ItemCoordinate(1095, 1198, 1326, 1304)]),
#     HeaderList(4, "UOM", [ItemCoordinate(1320, 1198, 1516, 1304)]),
#     HeaderList(5, "Unit Price", [ItemCoordinate(1516, 1198, 1710, 1304)]),
#     HeaderList(6, "Amount", [ItemCoordinate(1713, 1194, 1955, 1304)]),
#     HeaderList(7, "Dis %", [ItemCoordinate(1955, 1198, 2106, 1310)]),
#     HeaderList(8, "Line Total", [ItemCoordinate(2109, 1198, 2383, 1310)])
# ]

# pdf_path = "Sample documents/New folder/Chadwicks 2 Page.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "ITEM", [ItemCoordinate(67, 1285, 238, 1398)]),
#     HeaderList(2, "QTY", [ItemCoordinate(244, 1285, 412, 1401)]),
#     HeaderList(3, "UNIT", [ItemCoordinate(422, 1285, 586, 1395)]),
#     HeaderList(4, "DESCRIPTION", [ItemCoordinate(589, 1285, 1598, 1391)]),
#     HeaderList(5, "EXCL. VAT", [ItemCoordinate(1601, 1285, 1833, 1391)]),
#     HeaderList(6, "EXCL. VAT", [ItemCoordinate(1836, 1282, 2071, 1395)]),
#     HeaderList(7, "INCL.VAT", [ItemCoordinate(2075, 1282, 2300, 1398)]),
#     HeaderList(8, "CODE", [ItemCoordinate(2303, 1288, 2423, 1398)])
# ]

# pdf_path = "Sample documents/New folder/PF 3 Page.pdf"
# mandatory_column = 1
# ColumnList = [
#     HeaderList(1, "Item", [ItemCoordinate(115, 1059, 357, 1162)]),
#     HeaderList(2, "Name", [ItemCoordinate(357, 1059, 1732, 1156)]),
#     HeaderList(3, "Quantity", [ItemCoordinate(1732, 1062, 1974, 1156)]),
#     HeaderList(4, "Price", [ItemCoordinate(1977, 1059, 2174, 1162)]),
#     HeaderList(5, "Total", [ItemCoordinate(2177, 1066, 2367, 1156)])
# ]

classObject = Main("abc.pdf")
HelperObject = Helper()
pdf_raw_data: [] = classObject.ExtractDataFromPdf(pdf_path)

TableHeaderCoordinate = ItemCoordinate(0, 0, 0, 0)
TableFooterCoordinate = ItemCoordinate(0, 0, 0, 0)
EndOfTableCoordinate = ItemCoordinate(0, 0, 0, 0)
HeaderCoordinateList = []


def read_table_data():
    data_storage.clear()
    adjustment_height = 45

    # for obj in pdf_raw_data:
    #     classObject.PrintData(obj)

    coord: ItemCoordinate = HelperObject.table_header_area(ColumnList)
    TableHeaderCoordinate = ItemCoordinate(coord.x1, coord.y1, coord.x2, coord.y2)
    HeaderCoordinateList: [] = HelperObject.repeating_table_headers(pdf_raw_data, TableHeaderCoordinate, ColumnList,
                                                                    mandatory_column)

    table_header_width = TableHeaderCoordinate.x2 - TableHeaderCoordinate.x1
    table_header_height = TableHeaderCoordinate.y2 - TableHeaderCoordinate.y1 - adjustment_height

    for index in range(len(HeaderCoordinateList)):
        HeaderCoordinateList[index].coordinate.x2 = HeaderCoordinateList[index].coordinate.x1 + table_header_width
        if index == 0:
            HeaderCoordinateList[index].coordinate.y2 = HeaderCoordinateList[index].coordinate.y1 + table_header_height
            pass
        else:
            HeaderCoordinateList[index].coordinate.y2 = HeaderCoordinateList[index].coordinate.y1
            pass

        EndOfTableCoordinate.y1 = end_of_table_y1(HeaderCoordinateList[index].pageNo)
        table_region: TableRegion = TableRegion(ItemCoordinate(HeaderCoordinateList[index].coordinate.x1,
                                                               HeaderCoordinateList[index].coordinate.y1,
                                                               HeaderCoordinateList[index].coordinate.x2,
                                                               HeaderCoordinateList[index].coordinate.y2),
                                                ItemCoordinate(EndOfTableCoordinate.x1,
                                                               EndOfTableCoordinate.y1,
                                                               EndOfTableCoordinate.x2,
                                                               EndOfTableCoordinate.y2)
                                                )
        collect_table_data(HeaderCoordinateList[index].pageNo, table_region)

    store_in_data_structure()
    make_data_readable()
    prepare_formatted_clean_data()
    HelperObject.print_separator()
    HelperObject.print_clean_data(formatted_clean_data)
    pass


def collect_table_data(page_no, table_region):
    row: list = []
    row_separator = ""
    print(page_no, " ", table_region.top.y2)
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
        column_len = len(ColumnList)
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
                ref_header_x = ColumnList[column_index].coordinateList[0].x1

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
    coordinate = HelperObject.mandatory_column_coordinate(ColumnList, mandatory_column)
    MandatoryColumnCoordinate = ItemCoordinate(coordinate.x1, coordinate.y1, coordinate.x2, coordinate.y2)
    end_of_page = HelperObject.end_of_page(pdf_raw_data, page_no, MandatoryColumnCoordinate)
    return HelperObject.end_of_table_coord(page_no, pdf_raw_data, end_of_page,
                                           MandatoryColumnCoordinate,
                                           EndOfTableCoordinate)
    pass


read_table_data()
filename_without_ext = os.path.splitext(os.path.basename(pdf_path))[0]
xlsx_filename = filename_without_ext + ".xlsx"
convert_table_data_to_json = ConvertTableDataToJson([header.text for header in ColumnList],
                                                    formatted_clean_data)
convert_table_data_to_json.to_excel(os.path.basename(xlsx_filename))
