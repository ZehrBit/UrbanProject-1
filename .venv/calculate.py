def calculate_and_display_average_price(data):
    '''Выводит среднюю цену закрытия акций за заданный период'''
    print(f'Средняя цена закрытия акций за заданный период: {sum(data['Close']) / len(data['Close'])}')