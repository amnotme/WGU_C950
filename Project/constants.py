from datetime import date, time
from typing import List

# Loader constants
DISTANCES_DATA_FILE: str = 'data/Distances.xlsx'
DISTANCES_DATA_SHEET: str = 'distances'
PACKAGES_DATA_FILE: str = 'data/Packages.xlsx'
PACKAGES_DATA_SHEET: str = 'packages'

# Hubs constants. Row and column numbers to access hub data in Distances.xlsx
HUBS_ROWS_START: int = 0
HUBS_ROWS_END: int = 27
HUBS_COLUMNS_START: int = 0
HUBS_COLUMNS_END: int = 2

# Distances constants. Row and column numbers
# to access distance data in Distances.xlsx
DISTANCES_ROWS_START: int = 0
DISTANCES_ROWS_END: int = 27
DISTANCES_COLUMNS_START: int = 2
DISTANCES_COLUMNS_END: int = 29

# Parser constants. Other literal strings that should be treated as constants.
HUB_TEXT: str = "HUB"
EOD_TEXT: str = "EOD"
WGU_ADDRESS: str = "4001 South 700 East"
WGU_ZIPCODE: int = 84107

# Hashmap constants
AT_HUB_TEXT: str = "AT HUB"
DEFAULT_MAXIMUM_NUMBER_OF_PACKAGES: int = 40

# Truck / Dispatch constants
MAX_TRUCK_SPEED_PER_HOUR: float = 18.0  # mph
MAX_TRUCK_DISTANCE_PER_SECOND: float = MAX_TRUCK_SPEED_PER_HOUR / 3600.0  # mps
MAX_NUMBER_OF_TRUCKS_TO_DISPATCH: int = 3
MAX_NUMBER_OF_PACKAGES_TO_DELIVER: int = 40
MAX_TRUCK_CAPACITY: int = 16

# Truck constants
TRUCK_ONE_PACKAGES: List[int] = [1, 7, 8, 13, 14, 15, 16, 19, 20, 29, 30, 34, 37, 39, 40]
TRUCK_TWO_PACKAGES: List[int] = [2, 3, 9, 12, 17, 18, 27, 33, 35, 36, 38]
TRUCK_THREE_PACKAGES: List[int] = [4, 5, 6, 10, 11, 21, 22, 23, 24, 25, 28, 32, 26, 31]

# Time constants
DELIVERY_DATE: date = date.today()
DELAYED_START_TIME: time = time(hour=9, minute=5)  # 9:05 am
DEFAULT_DELIVERY_START_TIME: time = time(hour=8, minute=0)  # 8:00 am
DEFAULT_DELIVERY_END_TIME: time = time(hour=17, minute=0)  # 5:00 pm

# Business rules constants
BR_TIME_FOR_NEW_ADDRESS_FOR_PACKAGE_NINE: time = time(hour=10, minute=20)  # 10:20 am
BR_ONLY_IN_TRUCK_TWO: str = "Can only be on truck 2"
BR_WRONG_ADDRESS: str = "Wrong address listed"
BR_RIGHT_ADDRESS: str = "410 S State St"
BR_DELAYED_UNTIL_NINE_FIVE: str = "Delayed on flight---will not arrive to depot until 9:05 am"
BR_MUST_BE_DELIVERED_WITH_ONE: str = "Must be delivered with 13, 15"
BR_MUST_BE_DELIVERED_WITH_TWO: str = "Must be delivered with 13, 19"
BR_MUST_BE_DELIVERED_WITH_THREE: str = "Must be delivered with 15, 19"
BR_MUST_BE_DELIVERED: List[str] = [
    BR_MUST_BE_DELIVERED_WITH_ONE,
    BR_MUST_BE_DELIVERED_WITH_TWO,
    BR_MUST_BE_DELIVERED_WITH_THREE
]

# Main Menu Constants
MM_ONE_DISPLAY_OVERALL_SUMMARY: str = "[1] Display report at end-of-day"
MM_TWO_DISPLAY_SPECIFIC_TIME_SUMMARY: str = "[2] Display summary report for a given time"
MM_THREE_DISPLAY_PACKAGE_STATUS: str = "[3] Display status for a given package"
MM_EXIT_PROGRAM: str = "[Q] Exit dispatch tracking"
MM_USER_MENU: List[str] = [
    MM_ONE_DISPLAY_OVERALL_SUMMARY,
    MM_TWO_DISPLAY_SPECIFIC_TIME_SUMMARY,
    MM_THREE_DISPLAY_PACKAGE_STATUS,
    MM_EXIT_PROGRAM
]
