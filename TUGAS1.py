import tkinter as tk
from tkinter import messagebox
import sqlite3

# Fungsi untuk prediksi prodi
def prediksi_prodi():
    # Mengambil nilai dari entry
    nama_siswa = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    # Kondisi untuk menentukan prodi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # Menampilkan hasil prediksi
    label_hasil.config(text=f"Hasil Prediksi: {prediksi}")

    # Menampilkan messagebox notifikasi setelah hasil prediksi
    messagebox.showinfo("Hasil Prediksi", f"Prodi yang direkomendasikan untuk {nama_siswa}: {prediksi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('data_siswa.db')
    cursor = conn.cursor()

    # Membuat tabel 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            prediksi_fakultas TEXT
        )
    ''')

    # Menyimpan data ke tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))

    conn.commit()
    conn.close()

    # Menampilkan messagebox notifikasi setelah data berhasil disimpan
    messagebox.showinfo("Sukses", "Data berhasil disimpan!")

# Membuat window Tkinter
window = tk.Tk()
window.geometry("360x360")
window.title("Aplikasi Prediksi Prodi Pilihan")

# Create frame
frame = tk.Frame(window, width=300, height=200)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Membuat label judul
label_judul = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
label_judul.pack(pady=10)

# Membuat entry untuk nama siswa
label_nama = tk.Label(frame, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(frame, width=40, justify="center")  
entry_nama.pack()

# Membuat entry untuk nilai mata pelajaran
label_biologi = tk.Label(frame, text="Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(frame, width=20, justify="center") 
entry_biologi.pack()

label_fisika = tk.Label(frame, text="Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(frame, width=20, justify="center")  
entry_fisika.pack()

label_inggris = tk.Label(frame, text="Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(frame, width=20, justify="center")  
entry_inggris.pack()

# Membuat button untuk prediksi
button_prediksi = tk.Button(frame, text="Hasil Prediksi", command=prediksi_prodi)
button_prediksi.pack(pady=10)

# Membuat label hasil prediksi
label_hasil = tk.Label(frame, text="Hasil Prediksi:")
label_hasil.pack()

# Menjalankan main loop
window.mainloop()
