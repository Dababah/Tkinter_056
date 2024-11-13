import tkinter as tk
from tkinter import messagebox  # Untuk menampilkan pesan error

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # mengecek validnya nilai
    total_nilai = 0
    jumlah_input = 0
    validasi = True

    for entry in nilai_entries:
        nilai = entry.get()
        if not nilai.isdigit() or not (0 <= int(nilai) <= 100):
            validasi = False
            break
        total_nilai += int(nilai)
        jumlah_input += 1

    # nampilin teks kalo nilai nya ga sesuai
    if not validasi:
        messagebox.showerror("Input Error", "Harap masukkan nilai yang valid (0-100) untuk semua mata pelajaran.")
        return
    
    # hitung rata"
    rata_rata = total_nilai / jumlah_input

    # nentuin prodi sesuai nilai rata"
    if rata_rata >= 80:
        prodi = "Teknologi Informasi"
    elif rata_rata >= 60:
        prodi = "Teknik Sipil"
    else:
        prodi = "Teknik Mesin"
    
    # nampilin prodi seusia nilai rata"
    hasil_label.config(text=f"Prodi Pilihan: {prodi} (Rata-rata: {rata_rata:.2f})", fg="#1ABC9C", font=("Arial", 14, "bold"))
    animate_label(hasil_label)  # Memanggil fungsi animasi

# animasi dikit
def animate_label(label):
    text = label.cget("text")
    label.config(text="")
    for i in range(len(text) + 1):
        label.after(i * 100, lambda i=i: label.config(text=text[:i]))

# buat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x700")  # Ukuran window
root.config(bg="#f7f7f7")  # Latar belakang abu-abu terang

# nambah label judul 
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#FF6347", fg="white")
judul_label.grid(row=0, column=0, columnspan=2, pady=20)

# input 10 mata pelajaran
mata_pelajaran = [
    "Matematika", "Fisika", "Kimia", "Biologi", "Bahasa Indonesia",
    "Bahasa Inggris", "Ekonomi", "Sosiologi", "Geografi", "Sejarah"
]

nilai_entries = []
for i, pelajaran in enumerate(mata_pelajaran, start=1):
    label = tk.Label(root, text=f"Nilai {pelajaran}:", font=("Arial", 10), bg="#f7f7f7", anchor="w", fg="#34495E")
    label.grid(row=i, column=0, padx=20, pady=5, sticky="w")
    entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", fg="#2C3E50", highlightbackground="#3498DB", highlightcolor="#3498DB")
    entry.grid(row=i, column=1, padx=20, pady=5)
    nilai_entries.append(entry)

# Button untuk Hasil Prediksi 
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="raised", height=2)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=30)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12), bg="#f7f7f7", fg="#E74C3C")
hasil_label.grid(row=12, column=0, columnspan=2, pady=20)

# jalanin  aplikasi
root.mainloop()
