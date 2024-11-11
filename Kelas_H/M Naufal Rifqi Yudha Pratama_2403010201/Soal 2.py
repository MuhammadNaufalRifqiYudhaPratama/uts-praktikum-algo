def konversi_suhu():
    try:
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        
        fahrenheit = (celcius * 9/5) + 32

        print(f"Suhu dalam Fahrenheit: {fahrenheit}")
    except ValueError:
        print("Harap masukkan angka, jangan yang lain:).")

# Panggil fungsi
konversi_suhu()