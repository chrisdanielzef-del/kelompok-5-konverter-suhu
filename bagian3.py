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
