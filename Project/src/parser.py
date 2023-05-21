from typing import Union

from constants import EOD_TEXT, HUB_TEXT, WGU_ADDRESS, WGU_ZIPCODE
import datetime
from typing import Optional


class Parser:
    """
    A class for parsing data from an Excel file.
    """

    def __init__(self, file_path: Optional[str] = None) -> None:
        """
        Initializes a new Parser object.

        Args:
            file_path: The path to the Excel file to parse.
        """
        self.file_path = file_path

    def sanitize_hub_names(
            self,
            cell: str,
            cell_index: int
    ) -> Union[str, int]:
        """
        Sanitizes the hub name.

        Args:
            cell (str): cell containing hub information.
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

    def validate_delivery_time_from_cell(
            self,
            cell: str
    ) -> datetime:
        """
        Validates the delivery time.

        Args:
            cell: The delivery time.

        Returns:
            The validated delivery time.
        """

        if isinstance(cell, str) and cell == EOD_TEXT:
            return datetime.time(17, 0)
        else:
            return (datetime.datetime.strptime(cell, "%I:%M %p")).time()
