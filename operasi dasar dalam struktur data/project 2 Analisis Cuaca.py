import requests
import pandas as pd

# Mengubah deskripsi cuaca menjadi bahasa Indonesia
deskripsi_cuaca_id = {
    'clear sky': 'cerah',
    'few clouds': 'berawan sebagian',
    'broken clouds': 'berawan',
    'overcast clouds': 'mendung',
    'light rain': 'hujan ringan',
    'shower rain': 'hujan gerimis',  # Perbaikan: 'hujam gerimis' menjadi 'hujan gerimis'
    'rain': 'hujan',
    'thunderstorm': 'badai petir',    # Perbaikan: 'thunderstrom' menjadi 'thunderstorm'
    'snow': 'salju',
    'mist': 'kabut',
}

# Fungsi ambil data cuaca
def ambil_data_cuaca(kota, api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={kota}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None
    
# Fungsi untuk mendapatkan cuaca
def analisis_cuaca(data):
    if data is None:
        return None

    forecast_list = data.get('list', [])
    dates = []
    temperatures = []
    humidities = []
    weather_descriptions = []

    for item in forecast_list:
        date = item['dt_txt'].split(' ')[0]
        dates.append(date)
        temperatures.append(item['main']['temp'])
        humidities.append(item['main']['humidity'])
        desc = item['weather'][0]['description']
        weather_descriptions.append(deskripsi_cuaca_id.get(desc, desc))

    df = pd.DataFrame({
        'Tanggal': dates,
        'Suhu (K)': temperatures,
        'Kelembapan (%)': humidities,
        'Deskripsi Cuaca': weather_descriptions
    })
        
    # Konversi suhu dari Kelvin ke Celcius
    df['Suhu (C)'] = df['Suhu (K)'] - 273.15
    df = df.drop(columns=['Suhu (K)'])

    # Mengelompokkan berdasarkan tanggal
    df_daily = df.groupby('Tanggal').agg({
        'Suhu (C)': 'mean',
        'Kelembapan (%)': 'mean',
        'Deskripsi Cuaca': lambda x: x.mode()[0]
    }).reset_index()

    df_daily.index = df_daily.index + 1
    return df_daily

# Fungsi utama
def main():
    kota = input('Masukkan Nama Kota: ')
    api_key = 'bb6263bda4d31b31fc6719b44be5d926'

    data = ambil_data_cuaca(kota, api_key)
    df = analisis_cuaca(data)

    if df is not None:
        print(df.head())

if __name__ == '__main__':
    main()
