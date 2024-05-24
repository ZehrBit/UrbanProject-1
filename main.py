# Python 3.12.0

import data_download as dd
import data_plotting as dplt


styles = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic',
          'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright',
          'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid',
          'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper',
          'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white',
          'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet "
          "Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc): ")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите порог колебания(%) от 0 до 100: "))
    filename = input("Если нужно сохранить данные в файл *.csv, то введите имя для файла. Если сохранять не нужно - "
                     "оставьте поле пустым: ")
    period_rsi = int(input("Введите период(целое число) для RSI, например 14: "))
    start_date = input('Введите начальную дату периода в формате "YYYY-MM-DD": ')
    end_date = input('Введите конечную дату периода в формате "YYYY-MM-DD": ')
    style = styles[int(input('Для выбора стиля графика введите целое число от 0 до 27 включительно: '))]

    # Получает данные об акции
    stock_data = dd.fetch_stock_data(ticker, period, start_date, end_date)

    # Добавляет скользящее среднее в DataFrame
    stock_data = dd.add_moving_average(stock_data)

    # Выводит в терминал среднюю цену закрытия акций за заданный период
    dd.calculate_and_display_average_price(stock_data)

    # Выводит в терминал даты колебания, если превышен заданный диапазон
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Сохраняет полученные дынные в файл *.csv
    dd.export_data_to_csv(stock_data, filename)

    # Рассчитывает RSI и добавляет RSI в DataFrame
    stock_data = dd.rsi(stock_data, period_rsi)

    # Добавляет стандартное отклонение цены закрытия в DataFrame
    stock_data = dd.add_standard_deviation(stock_data)

    # Создание графика с ценами
    dplt.create_and_save_plot(stock_data, ticker, period, style)

    # Создание графика RSI
    dplt.create_and_save_plot_rsi(stock_data, ticker, period)

    # Создаёт график стандартного отклонения
    dplt.create_and_save_plot_standard_deviation(stock_data, ticker, period)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
