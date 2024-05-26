import matplotlib.pyplot as plt
import pandas as pd
from bokeh.palettes import tol
from bokeh.plotting import figure, show


def create_and_save_plot(data, ticker, period, style, filename=None):
    plt.figure(figsize=(10, 6))
    plt.style.use(style=f'{style}')

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акции с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()
    plt.show()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_and_save_plot_rsi(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['rsi'].values, label='RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['rsi'], label='RSI')

    plt.title(f"{ticker} RSI акции с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()

    if filename is None:
        filename = f"{ticker}_{period}_RSI.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def create_and_save_plot_standard_deviation(data, ticker, period, filename=None):
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Std_Deviation'].values, label='Стандартное отклонение')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Std_Deviation'], label='Стандартное отклонение')

    plt.title(f"{ticker}  акции с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Стандартное отклонение")
    plt.legend()
    plt.show()

    if filename is None:
        filename = f"{ticker}_{period}_standard_deviation.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def bokeh_show(data, ticker):
    """Создаёт интерактивный график"""
    p = figure(title=f"Индикаторы {ticker}",
               background_fill_color="#fafafa", x_axis_type="datetime")
    dates = data.index.to_numpy()
    p.line(dates, data['rsi'], legend_label="RSI", color='red')
    p.line(dates, data['Std_Deviation'], legend_label="Стандартное отклонение", color='blue')
    p.legend.location = "top_left"

    show(p)
