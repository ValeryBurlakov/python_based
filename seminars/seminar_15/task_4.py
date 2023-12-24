# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime
import logging
MONTHS = ('', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн',
          'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
DAYS = ('поне', 'втор', 'сред', 'четв', 'пятн', 'субб', 'воск')
logging.basicConfig(filename='loggingERROR_task_4.log', encoding='utf-8', level=logging.ERROR)

logger = logging.getLogger(__name__)


def get_date(date: str):

    try:
        count, wek_day, month = date.split()

    except ValueError as e:
        logger.error("Не удалось разбить строку на компоненты")
        return

    count = int(count[0])
    week_day = DAYS.index(wek_day[:4])
    month = MONTHS.index(month[:3])
    tmp = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=datetime.now().year)

        if date.weekday() == week_day:
            tmp += 1
            if tmp == count:
                # print(date)
                return date


if __name__ == '__main__':
    print(get_date('1-й четверг ноября'))
    print(get_date('3-я среда мая'))
    print(get_date('3-ясреда мая'))