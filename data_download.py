import yfinance as yf
import statistics
import numpy as np


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """Выводит среднюю цену закрытия акций за заданный период"""
    print(f'Средняя цена закрытия акции за заданный период: {statistics.mean(data['Close'])}')


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
        print('Введённый порог колебаний вне диапазона 0-100%')


def export_data_to_csv(data, filename):
    """Сохраняет полученные дынные в файл *.csv"""
    if filename != '':
        data.to_csv(f'{filename}.csv', encoding='utf-8')
        print(f'Файл {filename}.csv успешно сохранён')
    else:
        print('Вы оставили поле пустым. Файл *.csv не был сохранён')


def rsi(data, period_rsi):
    """Рассчитывает RSI и добавляет RSI в DataFrame"""
    def rma(x, n, y0):
        a = (n - 1) / n
        ak = a ** np.arange(len(x) - 1, -1, -1)
        return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a ** np.arange(1, len(x) + 1)]

    data['change'] = data['Close'].diff()
    data['gain'] = data.change.mask(data.change < 0, 0.0)
    data['loss'] = -data.change.mask(data.change > 0, -0.0)
    data['avg_gain'] = rma(data.gain[period_rsi + 1:].to_numpy(), period_rsi,
                           np.nansum(data.gain.to_numpy()[:period_rsi + 1]) / period_rsi)
    data['avg_loss'] = rma(data.loss[period_rsi + 1:].to_numpy(), period_rsi,
                           np.nansum(data.loss.to_numpy()[:period_rsi + 1]) / period_rsi)
    data['rs'] = data.avg_gain / data.avg_loss
    data['rsi'] = 100 - (100 / (1 + data.rs))
    return data
