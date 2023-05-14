
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

# Truck / Dispatch constatns
MAX_TRUCK_SPEED_PER_HOUR: float = 18.0 # mph
MAX_TRUCK_DISTANCE_PER_MINUTE: float = MAX_TRUCK_SPEED_PER_HOUR / 60.0 # mpm
MAX_NUMBER_OF_TRUCKS_TO_DISPATCH: int = 3
MAX_NUMBER_OF_PACKAGES_TO_DELIVER: int = 40
MAX_TRUCK_CAPACITY = 16