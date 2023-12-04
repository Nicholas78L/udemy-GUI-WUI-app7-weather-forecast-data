import requests

API_KEY = '71799afa63f51ded6d9d0396acf277f2'  # Ключ, полученный на сайте https://openweathermap.org/
cityname = 'Tokyo'


def get_data(place, forecast_days=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()         # Получаем огромный массив несортированых json данных.
    filtered_data = data['list']   # Выбираем только данные находящиеся в разделах 'list'
    # Т.к. сайт даёт данные с периодичностью в 3 часа (за сутки 8 раз) определяем число выборок данных
    nr_values = 8 * forecast_days  # исходя из произведения выборок за сутки на нужное кол-во дней (forecast_days)
    filtered_data = filtered_data[:nr_values]  # Делаем срез отфильтрованых данных исходя из нужного кол-ва выборок.
    return filtered_data          # Возвращщаем данные в место вызова ф-ции


# Создаём конструкцию для проверки работоспособности backend-a без запуска файла main.py:
if __name__ == '__main__':
    print(get_data(place='Tokyo', forecast_days=3))
