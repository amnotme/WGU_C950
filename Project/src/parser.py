import datetime
from typing import Union

import pandas as pd
from constants import EOD_TEXT, HUB_TEXT, WGU_ADDRESS, WGU_ZIPCODE
from pandas import DataFrame


class Parser:
    """
    A class for parsing data from an Excel file.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initializes a new Parser object.

        Args:
            file_path: The path to the Excel file to parse.
        """
        self.file_path = file_path

    def get_cells(
        self,
        sheet_name: str,
        filler: Union[str, int] = -1
    ) -> DataFrame:
        """
        Get cells from an Excel file.

        Args:
            sheet_name (str): The name of the sheet to read.
            filler Union(str, int): when encountering an nan in a
                Pandas dataframe cell we can fill it with this if provided.
                Default input is -1
        Returns:
            A Pandas DataFrame containing the cells from the specified range.
        """

        # Read the Excel file into a Pandas DataFrame.
        df: DataFrame = pd.read_excel(self.file_path, sheet_name=sheet_name)

        df.fillna(filler, inplace=True)

        return df

    def get_range_of_cells(
        self,
        sheet_name: str,
        start_row: int,
        end_row: int,
        start_col: int,
        end_col: int,
        filler: Union[str, int] = -1,
    ) -> DataFrame:
        """
        Get cells from an Excel file.

        Args:
            sheet_name (str): The name of the sheet to read.
            filler Union(str, int): when encountering an nan in a
                Pandas dataframe cell we can fill it with this
                if provided. Default input is -1
        Returns:
            A Pandas DataFrame containing the cells from the specified range.
        """

        # Read the Excel file into a Pandas DataFrame.
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)

        # Fill missing values with the specified filler.
        df.fillna(filler, inplace=True)

        # Return the specified range of cells.
        return df.iloc[start_row:end_row, start_col:end_col]

    def validate_delivery_time(
        self,
        cell: DataFrame
    ) -> datetime:
        """
        Validates the delivery time.

        Args:
            cell: The delivery time.

        Returns:
            The validated delivery time.
        """

        if isinstance(cell, str) and cell == EOD_TEXT:
            return datetime.time(20, 0)
        else:
            return cell

    def sanitize_hub_names(
        self,
        cell: DataFrame,
        cell_index: int
    ) -> Union[str, int]:
        """
        Sanitizes the hub name.

        Args:
            cell (DataFrame): cell containing hub information.
            cell_index: The index of the cell.

        Returns:
            The sanitized cell.
        """
        if cell_index == 1:
            if cell.strip() == HUB_TEXT:
                return WGU_ADDRESS
            return ((cell.strip().split("\n"))[0]).strip()
        elif cell_index == 2:
            if cell.strip() == HUB_TEXT:
                return WGU_ZIPCODE
            return int(((cell.strip().split("\n"))[1])[1:6])
