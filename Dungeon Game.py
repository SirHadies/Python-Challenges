print('''
     888                                                 
     888                                                 
     888                                                 
 .d88888888  88888888b.  .d88b.  .d88b.  .d88b. 88888b.  
d88" 888888  888888 "88bd88P"88bd8P  Y8bd88""88b888 "88b 
888  888888  888888  888888  88888888888888  888888  888 
Y88b 888Y88b 888888  888Y88b 888Y8b.    Y88..88P888  888 
 "Y88888 "Y88888888  888 "Y88888 "Y8888  "Y88P" 888  888 
                             888                         
                        Y8b d88P                         
                         "Y88P"      

''')
print("Welcome to the Dungeon")
choice_1 = input("would you like to enter the dungeon? yes/no :")
#Keep going in game
if choice_1 == "yes":
    print("you wake up in the middle of a dark room")
          #Second Choice after continueing
    choice_2 = input("You see two doors one to the left and one to the right. Which way are you going? left/right :")
    if choice_2 == "left":
        print("you enter a beautiful room and see a key in the middle. You pick it up.")
        #Third Choice for next section. This will take you to the next area. 
        choice_3 = input("You now have the a golden key. There is a large golden door at the end of the room. Do you rest or open? rest/open :")
        if choice_3 == "open":
            print ("You open the door and see a larger gemstone. It is the fabled gemstone of immortality.")
            choice_4 = input("Do you take the gemstone or leave it? take/leave :")
            if choice_4 == "take":
                print("You Take the gemstone. You are now Immortal. Enjoy your prize adventurer....YOU WIN")
            else:
                print("You leave the gemstone and this place with a hefty amount of treasure.....YOU WIN")
        else:
            print("The goblins from another area attack you in your sleep......END GAME")
    else:
        print("You enter the room on the right. You see a group of goblins who quickly attack you slitting your throat.....END GAME")
else:
    print("You take the cowards way and leave this place.....END GAME")