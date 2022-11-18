def start():
    while True:
        func = input('Для импорта нажмите "1", для экспорта нажмите "2":')
        if func == '1':
            imp_data()
        elif func == '2':
            exp_data()
        break