from datetime import datetime
date_to_prove = '15.4.2023'

# def is_valid_date(date_string):
#     try:
#         day, month, year = map(int, date_string.split('.'))
#         # Проверяем, что день, месяц и год находятся в допустимых диапазонах
#         if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
#             return True
#         else:
#             return False
#     except ValueError:
#         return False
#
# # date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
# print(is_valid_date(date_to_prove))
#
from datetime import datetime
date_to_prove = '31.6.2023'



def date_proof(date):
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False

print(date_proof(date_to_prove))