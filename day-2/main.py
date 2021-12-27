#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("Berapa total bill nya? $ "))
tip = int(input("Berapa banyak tip yang mau anda beri? 10, 12, atau 15 (Dalam Persen)? "))
people = int(input("Berapa banyak orang yang mau split bill?"))


# persenkan dulu tipnya
tip_as_percent = tip / 100

# jumlahkan tip yang sudah dipersenkan tadi dengan billnya untuk mendapatkan total tipnya
total_tip_amount = bill * tip_as_percent
# setelah itu tambah bill dengan tip supaya dapat total bayar
total_bill = bill + total_tip_amount

# bagi total bayar dengan jumlah orang untuk tau berapa banyak yang perlu dibayar tiap orang
bill_per_person = total_bill / people


# karna dimintanya 2 angka dibelakang koma maka kita bisa menggunakan round
final_amount = round(bill_per_person, 2)
print(f"Setiap orang harus membayar sebanyak: ${final_amount}")
