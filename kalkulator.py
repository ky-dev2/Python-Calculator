while True:
  try:
    angka1 = float(input("angka ke 1: "))
    angka2 = float(input("angka ke 2: "))
  except Valueerror:
    print("input harus angka, coba lagi \n")
    continue
 
  operasi = input("pilih operasi: |+|-|*|/|: ")
  
  if operasi == "+":
    hasil = angka1 + angka2
  elif operasi == "-":
    hasil = angka1 + angka2
  elif operasi == "*":
    hasil = angka1 * angka2
  elif operasi == "/":
    if angka2 == 0:
      hasil = "tidak bisa dibagi 0"
    else:
      hasil = angka1 / angka2
  else:
    hasil = "operasi tidak valid!"
      
  print("Hasil:", hasil)