
START_YEAR = 1990
FINAL_YEAR = 2050


def is_valid_month(month_number):
    """
        Checks if 'month_number' is a valid month number.

    :param month_number: Integer.
    :return: Boolean.
    """

    if (type(month_number) == int) and (1 <= month_number <= 12):
        return True

    return False


def is_valid_year(year_number):
    """
        Checks if 'year_number' is a valid year number.

    :param year_number: Integer.
    :return: Boolean.
    """

    if (type(year_number) == int) and (START_YEAR <= year_number <= FINAL_YEAR):
        return True

    return False
