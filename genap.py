print("DAFTAR BILANGAN GENAP")
nim = int(input("MASUKKAN NIM ANDA (tanpa 0 di depan) : "))
loop= int(input("MASUKKAN BERAPA LOOP YANG ANDA INGINKAN : "))
for i in range(nim,nim+loop):
	if (i % 2) == 0:
		print(i)
