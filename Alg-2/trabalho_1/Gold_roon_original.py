from sys import exit

# -> fim
def gold_room():
  print("This room is full of gold. How much do you take?")
  choice = int(input("> "))
  if choice == int:
    # mudado o "if "0" in choice or "1" in choice:" pois não fazia sentido
    dead("Man, learn to type a number.")
    #alterado a ordem, colocado função dead no lugar da sting how much
  else:
    how_much = int(choice)
  if how_much < 50:
    print("Nice, you're not greedy, you win!")
    exit(0)
  elif choice == "end":
    dead
  #opção para terminar o jogo mais rapido
  else:
    dead("You greedy bastard!")

# -> gold_room
def bear_room():
  print("There is a bear here.")
  print("The bear has a bunch of honey.")
  print("The fat bear is in front of another door.")
  print("How are you going to move the bear?")
  bear_moved = False
  while True:
    choice = input("> ")
    if choice == "take honey" and not bear_moved:
      #colocado o "and not bear_moved, para corrigir"
      dead("The bear looks at you then slaps your face off.")
    elif choice == "excuse bear" and not bear_moved:
      # criado a escolha excuse bear para pedir licença e passar pelo urso
      print("The bear has moved from the door.")
      print("You can go through it now.")
      bear_moved = True
    elif choice == "end":
      dead
      #opção para terminar o jogo mais rapido
    elif choice == "taunt bear" and not bear_moved:
      dead("The bear gets pissed off and chews your leg off.")
      #colocado o "and not bear_moved, para corrigir"
    elif choice == "open door" and bear_moved:
      gold_room()
    elif choice != "open door" and bear_moved:
      print("just open the door")
      #colocado elif para criar uma direcionar o jogador a abrir a porta
    else:
      print("I got no idea what that means.")

# -> sala_do_bau
def cthulhu_room():
  print("Here you see the great evil Cthulhu.")
  print("He, it, whatever stares at you and you go insane.")
  print("Do you flee for your life, eat your head or barganha")
  choice = input("> ")
  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that was tasty!")
  elif "barganha" in choice:
    print ("você trocou 3 anos de vida para sair com um tesouro")
    #add nova opção de escolha
    sala_do_bau()
  elif choice == "end":
    dead
    #colocado o "and not bear_moved, para corrigir"
  else:
    cthulhu_room()


def dead(why):
  print(why, "Good job!")
  exit(0)

def start():
  print("You are in a dark room.")
  print("There is a door to your right and left.")
  print("Which one do you take?")
  have_adaga = False
  choice = input("> ")
  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  elif choice == "end":
    dead
  else:
    dead("You stumble around the room until you starve.")

def sala_do_bau():
  print ("você entrou na sala do bau e tem uma escolha para fazer")
  print ("uma pequena adaga")
  print ("um grande punhado de rubis")
  print ("qual você escolhe")
  choice = input("> ")
  if choice == "adaga":
    print ("escolha certa pode continuar")
    vulcao()
  elif choice == "rubis":
    dead(" Cthulhu te pregou uma peça, você foi ganancioso")
  elif choice == "end":
    dead
  else:
    dead("demorou demais, MORTE")
    #add sala bau

def vulcao():
  print ("você encontra um vulcao e precisa se livrar")
  print("A lava está subindo!")
  print ("você tem duas opções")
  print ("um balde de água")
  print ("um caminho estreito")
  choice = input("> ")
  if choice == "balde de água":
    dead("A água acabou e você morreu com a lava.")
  elif choice == "caminho estreito":
    print ("você conseguiu se livrar, você saiu do vulcão.")
    ilha_do_farol()
  elif choice == "end":
    dead
  else:
    dead("demorou demais, a lava te alcançou")
    #add sala vulcao
    
def ilha_do_farol():
  print ("você encontra uma ilha com um farol")
  print("você tem três opções")
  print ("uma chave")
  print ("pegar algo brilhando na areia")
  print("Pegar o bote")
  choice = input("> ")
  if choice == "chave":
    print ("você conseguiu abrir o farol e achou o caminho para a sala do urso")
  elif choice == "pegar algo brilhando na areia":
    dead("era um escorpião! voce morreu.")
  elif choice == "pegar o bote":
    print("você afundou.")
    cthulhu_room()
  elif choice == "end":
    dead
  else:
    dead("um furação veio e você morreu.")
    #add sala ilha do farol
    
start()