import os
import pandas as pd
from typing import List


class ConvertTableDataToExcel:
    def __init__(self, column_names: List[str], row_data: List[dict]):
        self.row_data = row_data
        self.column_names = column_names

    def _format_table(self) -> List[dict]:
        return [{column_name: item.get(column_name, "").strip() for column_name in self.column_names}
                for item in self.row_data]

    def to_excel(self, folder_path="extracted_table_excel", file_name="result"):
        formatted_table = self._format_table()
        df = pd.DataFrame(formatted_table)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        df.to_excel(os.path.join(folder_path, file_name), index=False)