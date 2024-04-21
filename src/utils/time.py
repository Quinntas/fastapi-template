import datetime as dt

import pytz


def now(timezone: str = 'UTC'):
    """
    Get the current date and time.

    :param timezone: Optional parameter specifying the timezone. Default is 'UTC'.
    :type timezone: str
    :return: The current date and time.
    :rtype: datetime.datetime
    """
    return dt.datetime.now(pytz.timezone(timezone))


def dt_to_iso(_dt: dt.datetime, timezone: str) -> str:
    """
    Convert a datetime object to ISO 8601 format with the specified timezone.

    :param _dt: A datetime object to be converted.
    :param timezone: A string representing the timezone to convert to.
    :return: A string representing the datetime object in ISO 8601 format with the specified timezone.
    """
    return pytz.timezone('UTC').localize(_dt).astimezone(pytz.timezone(timezone)).isoformat()
