from seleck import start
import csv

data = [['Фамилие', 'Имя', 'Отчество', 'Телефон'],
        ['Нестеров', 'Сергей', 'Викторович', '89031234567'],
        ['Андрианив', 'Олег', 'Валерьевич', '89161234567'],
        ['Щеглов', 'Андрей', 'Иванович', '89017654321'],
        ['Корольков', 'Денис', 'Александрович', '89037654321']]


with open('sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('sw_data_new.csv') as f:
    print(f.read())
start()

