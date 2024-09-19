import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ambil data set
df = pd.read_csv('./day.csv')

st.title('Dashboard Penyewaan Sepeda')

# Menampilkan informasi dataset
st.subheader('Informasi Dataset')
st.write(df.describe())

# Sidebar untuk memilih fitur
st.sidebar.header('Pengaturan')
selectedWeather = st.sidebar.selectbox('Pilih Situasi Cuaca', ['Semua', 'Cerah, Beberapa Awan', 'Kabut + Berawan', 'Hujan Ringan, Salju'])
selectedHoliday = st.sidebar.selectbox('Pilih Tipe Hari', ['Semua', 'Hari Kerja', 'Hari Libur'])

if selectedWeather != 'Semua':
    weatherMap = {'Cerah, Beberapa Awan': 1, 'Kabut + Berawan': 2, 'Hujan Ringan, Salju': 3}
    df = df[df['weathersit'] == weatherMap[selectedWeather]]

if selectedHoliday != 'Semua':
    holidayMap = {'Hari Kerja': 0, 'Hari Libur': 1}
    df = df[df['holiday'] == holidayMap[selectedHoliday]]

# Visualisasi Situasi Cuaca
st.subheader('Jumlah Penyewa Berdasarkan Situasi Cuaca')
weatherCounts = df.groupby('weathersit')['cnt'].sum().reset_index()
weatherLabels = {1: 'Cerah, Beberapa Awan', 2: 'Kabut + Berawan', 3: 'Hujan Ringan, Salju'}
weatherCounts['weathersit'] = weatherCounts['weathersit'].map(weatherLabels)

plt.figure(figsize=(8, 6))
sns.barplot(data=weatherCounts, x='weathersit', y='cnt', palette='Blues')
plt.title('Jumlah Penyewa Berdasarkan Situasi Cuaca')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Jumlah Penyewa')
st.pyplot(plt)

# Visualisasi Hari Kerja dan Hari Libur
st.subheader('Jumlah Penyewa Berdasarkan Hari Kerja dan Hari Libur')
holidayLaounts = df.groupby('holiday')['cnt'].sum().reset_index()
holidayLabels = {0: 'Hari Kerja', 1: 'Hari Libur'}
holidayLaounts['holiday'] = holidayLaounts['holiday'].map(holidayLabels)

plt.figure(figsize=(6, 4))
sns.barplot(data=holidayLaounts, x='holiday', y='cnt', palette='Oranges')
plt.title('Jumlah Penyewa Berdasarkan Hari Kerja dan Hari Libur')
plt.xlabel('Tipe Hari')
plt.ylabel('Jumlah Penyewa')
st.pyplot(plt)

# kesimpulan
st.subheader('Kesimpulan')
st.write('Analisis ini menunjukkan bagaimana situasi cuaca dan tipe hari mempengaruhi jumlah penyewaan sepeda.')
