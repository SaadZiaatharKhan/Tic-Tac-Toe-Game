import sys, subprocess

print("***** WELCOME TO TIC TAC TOE GAME *****\n")

first_box=1
second_box=2
third_box=3
forth_box=4
fifth_box=5
sixth_box=6
seventh_box=7
eigth_box=8
ninth_box=9

playerx=input("\nWho Wants To Be X : ")
playero=input("Who Wants To Be O : ")

def game_layout():
  print(f"\n {first_box} | {second_box} | {third_box} ")
  print("-----------")
  print(f" {forth_box} | {fifth_box} | {sixth_box} ")
  print("-----------")
  print(f" {seventh_box} | {eigth_box} | {ninth_box} \n")
  
def playerx_function():
  game_layout()
  turnx=input(f"{playerx} turn : ")
  global first_box
  global second_box
  global third_box
  global forth_box
  global fifth_box
  global sixth_box
  global seventh_box
  global eigth_box
  global ninth_box
  if (turnx=="1"):
    first_box="X"
  elif (turnx=="2"):
    second_box="X"
  elif (turnx=="3"):
    third_box="X"
  elif (turnx=="4"):
    forth_box="X"
  elif (turnx=="5"):
    fifth_box="X"
  elif (turnx=="6"):
    sixth_box="X"
  elif (turnx=="7"):
    seventh_box="X"
  elif (turnx=="8"):
    eigth_box="X"
  elif (turnx=="9"):
    ninth_box="X"
  else:
    print("Your Chance Is Lost Now. Next Time Remember To Enter A Valid Option.")
  subprocess.run('clear' , shell=True)

def playero_function():
  game_layout()
  turno=input(f"{playero} turn : ")
  global first_box
  global second_box
  global third_box
  global forth_box
  global fifth_box
  global sixth_box
  global seventh_box
  global eigth_box
  global ninth_box
  if (turno=="1"):
    first_box="O"
  elif (turno=="2"):
    second_box="O"
  elif (turno=="3"):
    third_box="O"
  elif (turno=="4"):
    forth_box="O"
  elif (turno=="5"):
    fifth_box="O"
  elif (turno=="6"):
    sixth_box="O"
  elif (turno=="7"):
    seventh_box="O"
  elif (turno=="8"):
    eigth_box="O"
  elif (turno=="9"):
    ninth_box="O"
  else:
    print("Your Chance Is Lost Now. Next Time Remember To Enter A Valid Option.")
  subprocess.run('clear' , shell=True)

i=9
while (i>0):
  
  playerx_function()
  
  if (first_box==second_box==third_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (forth_box==fifth_box==sixth_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (seventh_box==eigth_box==ninth_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (first_box==forth_box==seventh_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (second_box==fifth_box==eigth_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (third_box==sixth_box==ninth_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (first_box==fifth_box==ninth_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break
  elif (third_box==fifth_box==seventh_box=="X") :
    print(f"{playerx} Wins\n Congratulations")
    break

  playero_function()

  if (first_box==second_box==third_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (forth_box==fifth_box==sixth_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (seventh_box==eigth_box==ninth_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (first_box==forth_box==seventh_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (second_box==fifth_box==eigth_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (third_box==sixth_box==ninth_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (first_box==fifth_box==ninth_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break
  elif (third_box==fifth_box==seventh_box=="O") :
    print(f"{playero} Wins\n Congratulations")
    break

  i=i-1
  if (i==0):
    break

a=input()