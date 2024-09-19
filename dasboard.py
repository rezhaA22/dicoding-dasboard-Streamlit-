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
selected_weather = st.sidebar.selectbox('Pilih Situasi Cuaca', ['Semua', 'Cerah, Beberapa Awan', 'Kabut + Berawan', 'Hujan Ringan, Salju'])
selected_holiday = st.sidebar.selectbox('Pilih Tipe Hari', ['Semua', 'Hari Kerja', 'Hari Libur'])

if selected_weather != 'Semua':
    weather_map = {'Cerah, Beberapa Awan': 1, 'Kabut + Berawan': 2, 'Hujan Ringan, Salju': 3}
    df = df[df['weathersit'] == weather_map[selected_weather]]

if selected_holiday != 'Semua':
    holiday_map = {'Hari Kerja': 0, 'Hari Libur': 1}
    df = df[df['holiday'] == holiday_map[selected_holiday]]

# Visualisasi Situasi Cuaca
st.subheader('Jumlah Penyewa Berdasarkan Situasi Cuaca')
weather_counts = df.groupby('weathersit')['cnt'].sum().reset_index()
weather_labels = {1: 'Cerah, Beberapa Awan', 2: 'Kabut + Berawan', 3: 'Hujan Ringan, Salju'}
weather_counts['weathersit'] = weather_counts['weathersit'].map(weather_labels)

plt.figure(figsize=(8, 6))
sns.barplot(data=weather_counts, x='weathersit', y='cnt', palette='Blues')
plt.title('Jumlah Penyewa Sepeda Berdasarkan Situasi Cuaca')
plt.xlabel('Situasi Cuaca')
plt.ylabel('Jumlah Penyewa')
st.pyplot(plt)

# Visualisasi Hari Kerja dan Hari Libur
st.subheader('Jumlah Penyewa Berdasarkan Hari Kerja dan Hari Libur')
holiday_counts = df.groupby('holiday')['cnt'].sum().reset_index()
holiday_labels = {0: 'Hari Kerja', 1: 'Hari Libur'}
holiday_counts['holiday'] = holiday_counts['holiday'].map(holiday_labels)

plt.figure(figsize=(6, 4))
sns.barplot(data=holiday_counts, x='holiday', y='cnt', palette='Oranges')
plt.title('Jumlah Penyewa Sepeda Berdasarkan Hari Kerja dan Hari Libur')
plt.xlabel('Tipe Hari')
plt.ylabel('Jumlah Penyewa')
st.pyplot(plt)

# kesimpulan
st.subheader('Kesimpulan')
st.write('Analisis ini menunjukkan bagaimana situasi cuaca dan tipe hari mempengaruhi jumlah penyewaan sepeda.')