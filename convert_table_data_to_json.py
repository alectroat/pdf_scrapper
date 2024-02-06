import json
from array import array
from typing import List, Dict
from TextCoordinate import Item
from convert_table_data_to_excel import ConvertTableDataToExcel


class ConvertTableDataToJson:
    def __init__(self, column_names: List[str], row_data: List[Item]):
        self.row_data = row_data
        self.column_names = column_names

    def _format_table(self) -> List[dict]:
        item_rows = []

        current_row = []
        row_count = 0
        for row in self.row_data:
            if row.column == 1:
                if row_count > 0:
                    item_rows.append(self.to_object(current_row))
                    current_row.clear()

                row_count += 1
            current_row.append(row.text)

        item_rows.append(self.to_object(current_row))
        return item_rows

    def to_json(self):
        formatted_table = self._format_table()
        return json.dumps(formatted_table)

    def to_excel(self, filename: str) -> None:
        formatted_table = self._format_table()
        converter = ConvertTableDataToExcel(self.column_names, formatted_table)
        converter.to_excel('extracted_table_excel', filename)

    def to_object(self, current_row):
        new_dict = {}
        for column_name, item in zip(self.column_names, current_row):
            new_dict[column_name] = item.strip()
        return new_dict
