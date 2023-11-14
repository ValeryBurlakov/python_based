import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = 30
MAX_REMOVAL = 600
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER_OPERATION = 3
RICHNESS_SUM = 5_000_000
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)

bank_account = decimal.Decimal(0)
count = 0

command = 0
operations = []


# ==================================================================================================
def check_multiplicity(amount):
    if amount % MULTIPLICITY != 0:
        print('Сумма должна быть кратной 50 у.е.')
    else:
        return amount


def deposit(amount):
    global bank_account
    global count
    if check_multiplicity(amount):
        count += 1
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')


def withdraw(amount):
    global bank_account
    global count
    sum_percents = amount * PERCENT_REMOVAL
    if check_multiplicity(amount):
        sum_percents = amount * PERCENT_REMOVAL

        if sum_percents > MAX_REMOVAL:
            sum_percents = MAX_REMOVAL
        elif sum_percents < MIN_REMOVAL:
            sum_percents = MIN_REMOVAL

        if (amount + sum_percents) <= bank_account:
            bank_account -= sum_percents + amount
            count += 1
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {int(sum_percents)} у.е.. Итого {int(bank_account)} у.е.')
        else:
            sum_with_percents = int(sum_percents + amount)

            operations.append(
                f'Недостаточно средств. Сумма с комиссией {sum_with_percents} у.е. На карте {bank_account} у.е.')
    else:
        if sum_percents > MAX_REMOVAL:
            sum_percents = MAX_REMOVAL
        elif sum_percents < MIN_REMOVAL:
            sum_percents = MIN_REMOVAL

        sum_with_percents = sum_percents + amount
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {sum_with_percents} у.е. На карте {bank_account} у.е.')


def exit():
    if bank_account > RICHNESS_SUM:
        calculate_richness_tax()
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')
    return
    # exit()


def calculate_richness_tax():
    global bank_account

    if bank_account > RICHNESS_SUM:
        sum_percents = bank_account * RICHNESS_PERCENT
        bank_account -= sum_percents
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {sum_percents} у.е. Итого {bank_account} у.е.')


# def check_counter():
#     global bank_account
#
#     if count % COUNTER_OPERATION == 0:
#         sum_percent = bank_account * PERCENT_DEPOSIT
#         bank_account += sum_percent


# ===========================================================================================================

deposit(1000)
withdraw(200)
exit()

print(operations)

bank_account = decimal.Decimal(0)
count = 0

command = 0
operations = []
deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()
print(operations)

bank_account = decimal.Decimal(0)
count = 0

command = 0
operations = []
deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()
print(operations)

bank_account = decimal.Decimal(0)
count = 0

command = 0
operations = []
deposit(173)
withdraw(21)
exit()

print(operations)

# ['Пополнение карты на 10000 у.е. Итого 10000 у.е.',
#  'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.',
# 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
#  'Возьмите карту на которой 770 у.е.']

# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.',
#  'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
#  'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.',
#  'Пополнение карты на 500 у.е. Итого 940 у.е.',
#  'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.',
#  'Возьмите карту на которой 940 у.е.']

# Сумма должна быть кратной 50 у.е.
# Сумма должна быть кратной 50 у.е.
# ['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']

# ['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.',
#  'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.',
#  'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.',
#  'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.',
#  'Снятие с карты 3000 у.е. Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.',
#  'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.',
#  'Возьмите карту на которой 899999999997205.5000 у.е.']
