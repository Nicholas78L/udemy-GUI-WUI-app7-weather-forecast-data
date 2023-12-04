import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text_input, slider, selectbox and subheader widgets:
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view', ['Temperature', 'Sky'])
st.subheader(f'{option} for the next {days} day(s) in {place}')

if place:   # Дальнейший код будет выполняться только после присвоения значения переменной 'place'.
    # Get temperature/sky data:
    filtered_data = get_data(place, days)

    if option == 'Temperature':  # Делаем выборку (для возврата данных в виде списка) по Температуре:
        temperatures = [dict['main']['temp'] for dict in filtered_data]  # Выборки по температурам.
        dates = [dict['dt_txt'] for dict in filtered_data]               # Выборки по датам.
        # Создаём график изменения Температуры:
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == 'Sky':  # Делаем выборку (для возврата данных в виде списка) по Небу:
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                  'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        # Делаем "ПЕРЕВОД" данных, из строкового формата в рисунок. Для этого ключи словаря 'images'
        # делаем идентичными значениям, хранящимся в списке 'sky_conditions'. А значениями этих ключей
        # выступают пути хранения соответствующих рисунков:
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)
