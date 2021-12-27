# nested if

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇


# choice 1
choice1 = input('Kamu sedang berada di pertigaan, jalan mana yang mau kamu pilih? Ketik "kiri" atau "kanan" \n').lower() # menggunakan lower karena bisa jadi user menginput dengan huruf besar
if choice1 == "kiri":
  # choice 2
  choice2 = input('Nah, sekarang kamu berada di pinggir laut, lalu kamu melihat ada sebuah pulau di depan sana, apa yang kamu lakukan?. Ketik "tunggu" Untuk menunggu perahu. Ketik "berenang" untuk berenang ke pulau. \n').lower() # menggunakan lower karena bisa jadi user menginput dengan huruf besar
  if choice2 == "tunggu":
    
    # choice 3
    choice3 = input("Kamu sampai di pulau dengan selamat. Disana ada 3 pintu. Berwarna Merah, Kuning dan Biru. Warna apa yang ingin anda pilih? \n").lower() # menggunakan lower karena bisa jadi user menginput dengan huruf besar
    if choice3 == "merah":
      print("Kamu memilih ruangan penuh dengan api. Game Over.")
    elif choice3 == "kuning":
      print("You found the treasure! You Win!")
    elif choice3 == "biru":
      print("Kamu memilih pintu penuh dengan hewan buas. Game Over.")
    else:
      print("Pintu yang kamu pilih tidak ada. Game Over.")
      
  # choice 2
  else:
    print("Yahh, kamu tenggelam, Game Over.")
# choice 1
else:
  print("Yahh, kamu terjatuh di lubang besar, Game Over.")
