
# Gunakan image dasar Python
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin semua isi folder lokal ke container
COPY . .

# Instal semua dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Buka port default Streamlit
EXPOSE 8501

# Jalankan aplikasi
CMD ["streamlit", "run", "app-analisis-film-jumbo.py", "--server.port=8501", "--server.address=0.0.0.0"]
