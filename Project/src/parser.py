import pandas as pd


class Parser:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_cells(self, sheet_name):
        """
        Get cells from an Excel file.

        Args:
            sheet_name (str): The name of the sheet to read.

        Returns:
            A Pandas DataFrame containing the cells from the specified range.
        """

        # Read the Excel file into a Pandas DataFrame.
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)

        df.fillna(-1, inplace=True)

        return df
