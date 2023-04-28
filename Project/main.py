from src.parser import Parser

DISTANCES_ROWS_START = 0
DISTANCES_ROWS_END = 28

DISTANCES_COLUMNS_START = 0
DISTANCES_COLUMNS_END = 27


parser = Parser('data/WGUPS Distance Table.xlsx')

cells = parser.get_cells(
        'distances'
    )


for cell in cells.itertuples():
    print(cell)
