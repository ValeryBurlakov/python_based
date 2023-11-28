# високосность
__all__ = ['is_leap', 'valid_date']


def is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def valid_date(date: str) -> bool:
    day, month, year = (int(value) for value in date.split('.'))
    if not 0 < day < 32 and 0 < month < 13 and 0 < year < 10000:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2:
        if day > 29:
            return False
        elif day == 29 and not is_leap(year):
            return False
    return True


if __name__ == '__main__':
    print(valid_date('31.4.2000'))
