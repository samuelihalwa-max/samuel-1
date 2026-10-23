print("--- GENERATOR PROMPT VISUAL ---")

# Meminta input kata kunci
input_subjek = input("Masukkan Subjek (misal: Harimau, Pesawat): ")
input_latar = input("Masukkan Latar Tempat (misal: Hutan, Mars): ")

print("\n--- PILIH GAYA SENI VISUAL ---")
print("1. Cinematic Photorealistic (Seperti Foto Asli)")
print("2. Studio Ghibli (Anime Jepang Damai)")
print("3. Cyberpunk Neon (Futuristik Kota Malam)")

# Menangkap angka yang diketik oleh user
pilihan_gaya = input("Masukkan nomor pilihan Anda (1/2/3): ")

if pilihan_gaya == "1":
    gaya_inggris = "hyperrealistic, 8k resolution, cinematic lighting, highly detailed photography"
elif pilihan_gaya == "2":
    gaya_inggris = "Studio Ghibli style, beautiful 2D anime art, vibrant colors, peaceful"
elif pilihan_gaya == "3":
    gaya_inggris = "Unreal Engine 5 render, cyberpunk neon lighting, futuristic city"
else:
    print("Pilihan tidak valid! Menggunakan gaya standar.")
    gaya_inggris = "beautiful digital art, highly detailed"

# Membersihkan spasi berlebih dan merapikan huruf kapital
subjek_bersih = input_subjek.strip().title()
latar_bersih = input_latar.strip().title()

# Merakit F-String
prompt_final = f"A masterpiece artwork of {subjek_bersih}, located in {latar_bersih}. {gaya_inggris}."

print("\nSilakan Copy Prompt Ini:")
print(prompt_final)