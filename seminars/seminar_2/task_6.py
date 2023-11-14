# банкомат

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

bank_account = 0
count = 0

command = 0

while command != CMD_EXIT:
    if bank_account > RICHNESS_SUM:
        sum_percents = bank_account * RICHNESS_PERCENT
        bank_account -= sum_percents
        print(f'налог на богатство: {sum_percents}. Ваш баланс: {bank_account}. ')

    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1

        while amount % MULTIPLICITY != 0:
            amount = decimal.Decimal(input(f"Введите сумму кратную {MULTIPLICITY} -> "))

        if command == CMD_DEPOSIT:
            count += 1
            bank_account += amount

        elif command == CMD_WITHDRAW:
            sum_percents = amount * PERCENT_REMOVAL
            if MIN_REMOVAL > sum_percents:
                sum_percents = MIN_REMOVAL

            elif MAX_REMOVAL < sum_percents:
                sum_percents = MAX_REMOVAL

            print(f'сумма комиссии {sum_percents}')

            if (amount + sum_percents) <= bank_account:
                bank_account -= sum_percents + amount
                count += 1

            else:
                print('Недостаточно средств.')

        if count % COUNTER_OPERATION == 0:
            sum_percent = bank_account * PERCENT_DEPOSIT
            bank_account += sum_percent
            print(f'Ваши 3 процента: {sum_percent}')

    print(f"Ваш баланс: {bank_account}. ")
    command = str(input(f"пополнить - {CMD_DEPOSIT}, снять {CMD_WITHDRAW}, выйти - {CMD_EXIT}: "))
print(f'Работа с терминалом завершена, ваш баланс: {bank_account}')
