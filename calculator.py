while True:
    try:
        angka1 = float(input("Masukkan angka1: "))
        angka2 = float(input("Masukkan angka2: "))
    except ValueError:
        print("Input harus angka, coba lagi.\n")
        continue

    operasi = input("Pilih operasi (+, -, *, /): ")

    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        if angka2 == 0:
            hasil = "Tidak bisa dibagi 0"
        else:
            hasil = angka1 / angka2
    else:
        hasil = "Operasi tidak valid"

    print("Hasil:", hasil)

    lanjut = input("Hitung lagi? (y/n): ")
    if lanjut.lower() != "y":
        print("Program selesai.")
        break