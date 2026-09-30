def konversi_suhu(suhu, satuan):
    if satuan.upper() == "C":
        return (suhu * 9 / 5) + 32
    elif satuan.upper() == "F":
        return (suhu - 32) * 5 / 9
    else:
        return None

suhu = float(input("Masukkan nilai suhu: "))
satuan = input("Masukkan satuan suhu ('C' untuk Celsius atau 'F' untuk Fahrenheit): ")

hasil = konversi_suhu(suhu, satuan)

if hasil is None:
    print("Input satuan suhu salah!")
elif satuan.upper() == "C":
    print(f"{suhu}°C = {hasil:.2f}°F")
else:
    print(f"{suhu}°F = {hasil:.2f}°C")