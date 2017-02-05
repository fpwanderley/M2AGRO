from copy import deepcopy

ROWS = 100000
COLUMNS = 100000
MARK = 'X'
NO_MARK = ' '
FILE = 'LogicFile.txt'

# Initiating the matrix and the reference row.
matrix = []
clean_row = [NO_MARK for i in range(COLUMNS)]


def populate_row(row, total_columns, row_position):
    """
        Populates a row according to its position in the matrix and the total of columns.

    :param row: List with the row to be populated.
    :param total_columns: Integer with the total of columns.
    :param row_position: Integer with the row position.
    :return: List with the modified row.
    """

    new_row = deepcopy(row)

    new_row[row_position] = MARK
    new_row[-1 - row_position] = MARK

    return new_row


def fill_file(matrix, file_name):
    """
        Prints a matrix into a file.

    :param matrix: List of Lists of strings.
    :param file_name: String with the file name.
    :return: None.
    """

    with open(file_name, 'w') as logic_file:

        # Prints the generated matrix into the file.
        for row in matrix:
            logic_file.write(''.join(row) + '\n')


# Insert the first row.
reference_index = int(ROWS/2)
first_row = populate_row(clean_row, COLUMNS, reference_index)
matrix.append(first_row)

# If even, it has to have two identical lines in the middle.
if ROWS % 2 == 0:
    new_row = deepcopy(first_row)
    matrix.append(new_row)
    reference_index -= 1

# The loop runs for half the remaining row and inserts identical copies both at
# the beggining and end of the matrix.
for index in range(reference_index - 1, -1, -1):

    new_row = populate_row(clean_row, COLUMNS, index)
    matrix = [new_row] + matrix + [new_row]

# Prints the matrix into the FILE.
fill_file(matrix, file_name=FILE)

