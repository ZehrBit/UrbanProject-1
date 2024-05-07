import yfinance as yf
import statistics


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """Выводит среднюю цену закрытия акций за заданный период"""
    print(f'Средняя цена закрытия акций за заданный период: {statistics.mean(data['Close'])}')


def notify_if_strong_fluctuations(data, threshold):
    """Выводит даты колебания, если превышен заданный диапазон(threshold)"""
    if 0 <= threshold <= 100:
        index_period = 0
        for index_date in data.index:
            try:
                period1 = data.iloc[index_period, 3]
                period2 = data.iloc[index_period - 1, 3]
                if period1 > period2:
                    percent = abs(period2 / period1 * 100 - 100)
                else:
                    percent = abs(period1 / period2 * 100 - 100)
                index_period += 1
                if percent >= threshold:
                    print(f'Колебания больше {threshold}% за период: {index_date}')
            except IndexError:
                pass
    else:
        print('Введённый порог колебания вне диапазона 0-100%')


def export_data_to_csv(data, filename):
    """Сохраняет полученные дынные в файл *.csv"""
    if filename != '':
        data.to_csv(f'{filename}.csv', encoding='utf-8')
        print(f'Файл {filename}.csv успешно сохранён')
    else:
        print('Вы оставили поле пустым. Файл не был сохранён')
