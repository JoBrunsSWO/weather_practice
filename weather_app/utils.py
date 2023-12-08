from datetime import datetime

DAY_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DAY_FORMAT = "%Y-%m-%d"

def convert_date(date):
    """
    Convert a date from the API Endpoint to a more readable format
    """
    # check for None
    if date is None:
        raise TypeError("Input date cannot be None")

    # Check for int
    if isinstance(date, int):
        raise TypeError("Input date cannot be an integer")

    try:
        converted_obj = datetime.strptime(date, DAY_TIME_FORMAT)
        converted_date = converted_obj.strftime("%d %b %Y, %H:%M")
        return converted_date
    except ValueError:
        pass  # The format DAY_TIME_FORMAT didn't match

    try:
        converted_obj = datetime.strptime(date, DAY_FORMAT)
        converted_date = converted_obj.strftime("%d %b %Y")
        return converted_date
    except ValueError:
        pass  # The format DAY_FORMAT didn't match

    raise ValueError("Incorrect date format, should be YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ")
  