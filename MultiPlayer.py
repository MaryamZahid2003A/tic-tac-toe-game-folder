import random
x="y"
run="start"
n1=1
n2=2
n3=3
n4=4
n5=5
n6=6
n7=7
n8=8
n9=9
#Number of turns
count=0

while x=="y":
    print("-------------Welcome to Tic Tac Toe game---------------")
    #Naming players
    player_1=input("Enter Your Name Player 1: ")
    player_2=input("Enter Your Name player 2: ")
    print(" ")
    choose=eval(input("Who want to choose first his sign:\nIf player 1 choose firstly, press1 \nif Player 2 choose firstly, Press 2 :"))
    print(" ")
    #Choosing Symbols
    if choose==1:
        h_t=eval(input("Player 1 You choose first Press 0 for Head and Press 1 for Tail: "))
        print(" ")
        while x=="y":
            symbol=input("Player 1 Enter your Symbol(x or o)")
            if symbol=="x" or symbol=="o":
                if symbol=="x":
                    player_x="x" 
                    player_y="o"
                elif symbol=="o":
                    player_x="o"
                    player_y="x"
                x="z"
            else:
                print("Invalid!Choose symbol from X and O")
                continue
    elif choose==2:
        h_t=eval(input("Player 2 You choose first press 0 for Head and Press 1 for Tail: "))
        print(" ")
        while x=="y":
            symbol=input("Player 2 Enter your Symbol(x or o)")
            if symbol=="x"  or symbol=="o":
                if symbol=="x":
                    player_x="o" 
                    player_y="x"
                elif symbol=="o":
                    player_x="x"
                    player_y="o"
                x="z"
            else:
                print("Invalid!Choose symbol from X and O")
                continue
    toss=random.randint(0,1)
    #Toss
    if toss==h_t:
         if toss==0:
             print(player_1," You won the toss!")
             i=1
         else:
            print(player_2," You won the toss!")
            i=2
    else:
        if toss==0:
            print(player_1," You won the toss!")
            i=1
        else:
            print(player_2," You won the toss!")
            i=2
    print(n1,"|",n2,"|",n3)
    print("---------")
    print(n4,"|",n5,"|",n6)
    print("---------")
    print(n7,"|",n8,"|",n9)
    
    while run=="start":
        #Turns
        check="To_check"
        if i==1:
            print(player_1,"Your Turn! ")
            turn=input("Which position do you want from 1 to 9,Press,and if you want to exit press e? ")
            print(" ")   
            #End Game
            if turn=="e" or turn=="E":
                print("Thanks for playing!")
                break
            #Is alphabet
            if turn.isalpha()==True:
                print("Invalid!Press from(1 to 9)")
                continue
            
            #Invalid Numbers
            turn=int(turn)  
            if int(turn)<=0 or int(turn)>=10:
                print("Invalid number,Enter number from 1 to 9")
                print(" ")
                continue
            #Position occupied
            if check=="To_check":
                if turn==1:
                    if n1=="x" or n1=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==2:
                    if n2=="x" or n2=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==3:
                    if n3=="x" or n3=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==4:
                    if n4=="x" or n4=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==5:
                    if n5=="x" or n5=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==6:
                    if n6=="x" or n6=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==7:
                    if n7=="x" or n7=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==8:
                    if n8=="x" or n8=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==9:
                    if n9=="x" or n9=="o":
                        print("Position is already occupied!")
                        continue
                check="Not_to_check"
                
            
            #Displaying on board
            if int(turn)>=1 and int(turn)<=9:
                if int(turn)==1:
                    n1=player_x
                elif int(turn)==2:
                    n2=player_x
                elif int(turn)==3:
                    n3=player_x
                elif int(turn)==4:
                    n4=player_x
                elif int(turn)==5:
                    n5=player_x
                elif int(turn)==6:
                    n6=player_x
                elif int(turn)==7:
                    n7=player_x
                elif int(turn)==8:
                    n8=player_x
                elif int(turn)==9:
                    n9=player_x
                        
            print(n1,"|",n2,"|",n3)
            print("---------")
            print(n4,"|",n5,"|",n6)
            print("---------")
            print(n7,"|",n8,"|",n9)
            count+=1
            i=2
           
            # Winning Conditions:
            if n1==player_x and n2==player_x and n3==player_x:
                print("********** Congratulation *********")
                print(player_1," You won the Game!")
                break
            
            elif n4==player_x and n5==player_x and n6==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
            
            elif n7==player_x and n8==player_x and n9==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
            
            elif n1==player_x and n4==player_x and n7==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
            
            elif n2==player_x and n5==player_x and n8==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
            
            elif n3==player_x and n6==player_x and n9==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
                
            elif n1==player_x and n5==player_x and n9==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
                
            elif n3==player_x and n5==player_x and n7==player_x:
                print("********* Congratulation **********")
                print(player_1," You won the Game!")
                break
                
            else:
                if count==9:
                    print("Tie")
                    break
          
        elif i==2:
            
            print(player_2," Your Turn!")
            turn=input("Which position do you want from 1 to 9,Press,and if you want to exit press e: ")
            print(" ")
            check="To_check"
             
            #End game
            
            if turn=="e" or turn=="E":
                print("Thanks for playing!")
                break
            
            #Is alphabet
            if turn.isalpha()==True:
                print("Invalid!Press from(1 to 9)")
                continue
            
            #Invalid Inputs
            turn=int(turn)
            if int(turn)<1 or int(turn)>9:
                print("Invalid Input!Enter a number between 1 and 9")
                continue
            
            if check=="To_check":
                if turn==1:
                    if n1=="x" or n1=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==2:
                    if n2=="x" or n2=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==3:
                    if n3=="x" or n3=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==4:
                    if n4=="x" or n4=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==5:
                    if n5=="x" or n5=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==6:
                    if n6=="x" or n6=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==7:
                    if n7=="x" or n7=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==8:
                    if n8=="x" or n8=="o":
                        print("Position is already occupied!")
                        continue
                elif turn==9:
                    if n9=="x" or n9=="o":
                        print("Position is already occupied!")
                        continue
                check="Not_to_check"
            #Row and column   
            if int(turn)>=1 and int(turn)<=9:
                if int(turn)==1:
                    n1=player_y
                elif int(turn)==2:
                    n2=player_y
                elif int(turn)==3:
                    n3=player_y
                elif int(turn)==4:
                    n4=player_y
                elif int(turn)==5:
                    n5=player_y
                elif int(turn)==6:
                    n6=player_y
                elif int(turn)==7:
                    n7=player_y
                elif int(turn)==8:
                    n8=player_y
                elif int(turn)==9:
                    n9=player_y
                        
            print(n1,"|",n2,"|",n3)
            print("---------")
            print(n4,"|",n5,"|",n6)
            print("---------")
            print(n7,"|",n8,"|",n9)
            count+=1
            i=1  
             
             # Winning Conditions:
            if n1==player_y and n2==player_y and n3==player_y:
                print("********** Congratulation *********")
                print(player_2," You won the Game!")
                break
            
            elif n4==player_y and n5==player_y and n6==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
            
            elif n7==player_y and n8==player_y and n9==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
                
            elif n1==player_y and n4==player_y and n7==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
            
            elif n2==player_y and n5==player_y and n8==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
            
            elif n3==player_y and n6==player_y and n9==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
                
            elif n1==player_y and n5==player_y and n9==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
                
            elif n3==player_y and n5==player_y and n7==player_y:
                print("********* Congratulation **********")
                print(player_2," You won the Game!")
                break
            else:
                if count==9:
                    print("Tie")
                    break
    
    
    end=input("If you want to play again then press y ! otherwise press k")
    if end=="y" or end=="Y":
         count=0
         x="y"
         n1=1
         n2=2
         n3=3
         n4=4
         n5=5
         n6=6
         n7=7
         n8=8
         n9=9
    else:
        if end=="k" or end=="K":
            print("Thanks for playing")
            break
