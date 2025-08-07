import jdatetime  # type: ignore
from datetime import datetime


def get_date_year() -> str:
    now = jdatetime.date.today()
    first_day_of_day = datetime(year=now.year, month=1, day=1)
    date_year = first_day_of_day.strftime('%Y-%m-%d')
    return date_year


def convert(date_input: str) -> list:
    if '-' in date_input:
        return date_input.split('-')
    elif '/' in date_input:
        return date_input.split('/')
    elif '\\' in date_input:
        return date_input.split('\\')
    elif '.' in date_input:
        return date_input.split('.')


def miladiToShamsi(date_input: str) -> str:
    data = convert(date_input)
    y, m, d = int(data[0]), int(data[1]), int(data[2])
    return jdatetime.date.fromgregorian(day=d, month=m, year=y)


def ShamsiToMiladi(date_input: str) -> str:
    data = convert(date_input)
    y, m, d = int(data[0]), int(data[1]), int(data[2])
    return jdatetime.date(day=d, month=m, year=y).togregorian()


def convertToYMD(date_input: str) -> str:
    try:
        obj = datetime.strptime(date_input, "%m/%d/%Y")
    except Exception:
        obj = date_input
    result = obj.strftime("%Y-%m-%d")
    return result


def convertToMDY(date_input: str) -> str:
    try:
        obj = datetime.strptime(date_input, "%Y-%m-%d")
    except Exception:
        obj = date_input
    result = obj.strftime("%m/%d/%Y")
    return result


def convertToYMD_datetime(date_input: datetime) -> str:
    result = date_input.strftime("%Y-%m-%d")
    return result


def try_again(func, data):
    try:
        return func()
    except Exception:
        result = data
        return result
