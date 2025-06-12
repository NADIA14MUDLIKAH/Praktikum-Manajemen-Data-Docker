import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Prediksi Penonton Jumbo", layout="centered")
st.title("🎥 Prediksi Penonton Film Jumbo (14 Hari ke Depan)")

@st.cache_data
def load_data():
    df = pd.read_csv("DATA FILM JUMBO - Sheet1.csv")
    df = df[['Tanggal', 'Jumlah Penonton']].dropna()
    df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%d-%m-%Y')
    df['Jumlah Penonton'] = df['Jumlah Penonton'].str.replace('.', '', regex=False).astype(int)
    return df.sort_values('Tanggal').reset_index(drop=True)

df = load_data()

# Siapkan data untuk prediksi
X = np.array(range(len(df))).reshape(-1, 1)
y = df['Jumlah Penonton'].values

# Latih model regresi
model = LinearRegression()
model.fit(X, y)

# Prediksi 14 hari ke depan
future_days = 14
last_day = X[-1][0]
X_future = np.array([last_day + i for i in range(1, future_days + 1)]).reshape(-1, 1)
y_pred = model.predict(X_future)

# Buat dataframe prediksi
future_dates = pd.date_range(start=df['Tanggal'].iloc[-1] + pd.Timedelta(days=1), periods=future_days)
df_pred = pd.DataFrame({
    'Tanggal': future_dates,
    'Prediksi Penonton': y_pred.astype(int)
})

# Tampilkan tabel prediksi
st.subheader("📅 Prediksi 14 Hari ke Depan")
st.dataframe(df_pred)

# Grafik visualisasi
st.subheader("📈 Grafik Penonton Film Jumbo")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Tanggal'], df['Jumlah Penonton'], marker='o', label='Data Historis')
ax.plot(df_pred['Tanggal'], df_pred['Prediksi Penonton'], marker='x', linestyle='--', color='red', label='Prediksi')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penonton")
ax.set_title("Prediksi Penonton Film Jumbo")
ax.legend()
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(fig)

st.caption("Aplikasi prediksi sederhana berbasis linear regression")
