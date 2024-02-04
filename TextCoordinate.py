class TextCoordinate:
    def __init__(self, text, pageNo, lineNo, x1, y1, x2, y2):
        self.text = text
        self.pageNo = pageNo
        self.lineNo = lineNo
        self.extracted = False
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class ItemCoordinate:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class HeaderList:
    def __init__(self, item_id, text, coordinate_list):
        self.itemId = item_id
        self.text = text
        self.coordinateList = coordinate_list


class Item:
    def __init__(self, row, column, data):
        self.row = row
        self.column = column
        self.coordinate = ItemCoordinate(0, 0, 0, 0)
        self.data = data
        self.text = ""
        self.extracted = False
        self.deleted = False


class HeaderCollection:
    def __init__(self, pageNo):
        self.pageNo = pageNo
        self.coordinate = ItemCoordinate(0, 0, 0, 0)


class TableRegion:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
