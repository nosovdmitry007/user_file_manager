def schet():

    import os
    import json
    pokupki={}

    def open_file_reading(name_file):
      with open(name_file, 'r') as expense:
        return expense.read()
    def sum_chet_write(schet):
      with open('invoice_amount.txt', 'w') as expense:
        expense.write(str(schet))
    def shopping_history_write(pokupki):
      with open('shopping_history.txt', 'a') as expense:
        expense.write(str(pokupki))


    if os.path.exists('invoice_amount.txt'):
        print('На счете: ', open_file_reading('invoice_amount.txt'))
    else:
        with open('invoice_amount.txt','w') as expense:
            expense.write('0')

    if not os.path.exists('shopping_history.txt'):
         with open('shopping_history.txt','w') as expense:
            expense.write('')


    def popolnenie():
        schet=int(open_file_reading('invoice_amount.txt'))
        schet+=int(input('На какую сумму пополнить счёт? '))
        print('Счет пополнен, сумма на счете: ', schet)
        sum_chet_write(schet)
    def pokupka():
      schet=int(open_file_reading('invoice_amount.txt'))
      k=int(input('Введите сумму покупки: '))
      if k>schet:
        print('Денег недостаточно для покупки: ')
      else:
        pokupki[input('Введите название покупки: ')]=k
        shopping_history_write(pokupki)
        schet=schet-k
        sum_chet_write(schet)
        print('Сумма на счете: ', schet)
    def story():
        print('История покупок: \n',json.dumps(open_file_reading('shopping_history.txt'), indent=3))
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            popolnenie()
        elif choice == '2':
            pokupka()
        elif choice == '3':
            story()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')