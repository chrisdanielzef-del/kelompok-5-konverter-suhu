print("=== Konverter Suhu Sederhana ===")
print("1. Celsius ke Fahrenheit")
print("2. Celsius ke Kelvin")
print("3. Fahrenheit ke Celsius")
print("4. Fahrenheit ke Kelvin")
print("5. Kelvin ke Celsius")
print("6. Kelvin ke Fahrenheit")

pilihan = int(input("Pilih konversi (1-6): "))
nilai = float(input("Masukkan nilai suhu: "))

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

if pilihan == 1:
    print(f"Hasil: {celsius_to_fahrenheit(nilai):.2f} °F")
elif pilihan == 2:
    print(f"Hasil: {celsius_to_kelvin(nilai):.2f} K")
elif pilihan == 3:
    print(f"Hasil: {fahrenheit_to_celsius(nilai):.2f} °C")
elif pilihan == 4:
    print(f"Hasil: {fahrenheit_to_kelvin(nilai):.2f} K")
elif pilihan == 5:
    print(f"Hasil: {kelvin_to_celsius(nilai):.2f} °C")
elif pilihan == 6:
    print(f"Hasil: {kelvin_to_fahrenheit(nilai):.2f} °F")
else:
    print("Pilihan tidak valid!")
