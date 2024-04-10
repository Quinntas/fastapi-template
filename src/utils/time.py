import datetime as dt

import pytz


def now(timezone: str = 'UTC'):
    return dt.datetime.now(pytz.timezone(timezone))


def dt_to_iso(_dt: dt.datetime, timezone: str) -> str:
    return pytz.timezone('UTC').localize(_dt).astimezone(pytz.timezone(timezone)).isoformat()
