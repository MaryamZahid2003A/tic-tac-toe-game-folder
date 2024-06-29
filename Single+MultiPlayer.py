import random
x="b"
run="start"
#Check board
board=[["1","2","3"],
       ["4","5","6"],
       ["7","8","9"]]
new_count=0
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
end="a"
value1=1
value2=2
print("-------------WELCOME TO TIC TAC TOE GAME---------------")
# choosing of game
def again():
    while run=="start":
        new_check=input("Enter 1! for Multiplayer \nEnter 2! for Single player \nEnter 3! for Exit")
        if new_check.isalpha()==True:
            print("Invalid!")
            print(" ")
            continue
        else:
            new_check=int(new_check)
            return new_check
        
def turns():
    value=again()
    if value==1:
        x="y"
    elif value==2:
        x="z"
    elif value==3:
        print(" ")
        x="Thanks for playing!"
        print(x)
    else:
        while value<=0 or value>=4:
            if value<=0 or value>=4:
                print("Invalid!Enter Correctly")
                print(" ")
                value=again()
                if value==1:
                    x="y"
                elif value==2:
                    x="z"
                elif value==3:
                    x="Thanks for playing!"
                    print(x)
                elif value<=0 or value>=4:
                    continue
    return x
new_turn=turns()
while end!="k" or end!="K":
    while new_turn=="y":
        if value1==1:
            while new_turn=="y":
                #Multiplayer Game
                print("-------------WELCOME TO MULTIPLAYER GAME---------------")
                #Naming players
                player_1=input("Enter Your Name Player 1: ")
                player_2=input("Enter Your Name player 2: ")
                print(" ")
                while run=="start":
                    choose=input("Who want to choose first his sign:\nIf player 1 choose firstly, enter 1 \nif Player 2 choose firstly, Enter 2 :")
                    if choose.isalpha()==True:
                        print("Invalid!")
                        continue
                    elif int(choose)!=1 and int(choose)!=2:
                        print("Invalid!")
                        continue
                    else:
                        run="nstart"
                    
                print(" ")
                #Choosing Symbols
                choose=int(choose)
                run="start"
                if choose==1:
                    while run=="start":
                        h_t=input("Player 1 You choose first Enter 0 for Head and Enter 1 for Tail: ")
                        if h_t.isalpha()==True:
                            print("Invalid!")
                            continue
                        elif int(h_t)!=0 and int(h_t)!=1:
                            print("Invalid!")
                            continue
                        else:
                            run="nstart"
                    while new_turn=="y":
                        symbol=input("Player 1 Enter your Symbol(x or o)")
                        if symbol=="x" or symbol=="o":
                            if symbol=="x":
                                player_x="x" 
                                player_y="o"
                            elif symbol=="o":
                                player_x="o"
                                player_y="x"
                            new_turn="z"
                        else:
                            print("Invalid!Choose symbol from X and O")
                            continue
                elif choose==2:
                    print(" ")
                    run="start"
                    while run=="start":
                        h_t=input("Player 2 You choose first Enter 0 for Head and Enter 1 for Tail: ")
                        if h_t.isalpha()==True:
                            print("Invalid!")
                            continue
                        elif int(h_t)!=0 and int(h_t)!=1:
                            print("Invalid!")
                            continue
                        else:
                            run="nstart"
                    while new_turn=="y":
                        symbol=input("Player 2 Enter your Symbol(x or o)")
                        if symbol=="x"  or symbol=="o":
                            if symbol=="x":
                                player_x="o" 
                                player_y="x"
                            elif symbol=="o":
                                player_x="x"
                                player_y="o"
                            new_turn="z"
                        else:
                            print("Invalid!Choose symbol from X and O")
                            continue
                toss=random.randint(0,1)
                h_t=int(h_t)
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
                
                def board():
                    print(n1,"|",n2,"|",n3)
                    print("---------")
                    print(n4,"|",n5,"|",n6)
                    print("---------")
                    print(n7,"|",n8,"|",n9)
                board()
                run="start"
                while run=="start":
                #Turns
                    check="To_check"
                    if i==1:
                        print(player_1,"Your Turn! ")
                        turn=input("Which position do you want from 1 to 9,Enter,and if you want to exit Enter e? ")
                        print(" ")   
                        #End Game
                        if turn=="e" or turn=="E":
                            print("Thanks for playing!")
                            break
                        #Is alphabet
                        if turn.isalpha()==True:
                            print("Invalid!Enter from(1 to 9)")
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
                        
                        board()
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
                        turn=input("Which position do you want from 1 to 9,Enter,and if you want to exit press e: ")
                        print(" ")
                        check="To_check"
                 
                        #End game
                
                        if turn=="e" or turn=="E":
                            print("Thanks for playing!")
                            break
                
                        #Is alphabet
                        if turn.isalpha()==True:
                            print("Invalid!Enter from(1 to 9)")
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
                        
                        board()
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
    
                print("Match is over!")
                print(" ")
                end=input("If you want to play again then Enter y ! otherwise Enter k")
                if end=="y" or end=="Y":
                    count=0
                    n1=1
                    n2=2
                    n3=3
                    n4=4
                    n5=5
                    n6=6
                    n7=7
                    n8=8
                    n9=9
                    board=[["1","2","3"],
                           ["4","5","6"],
                           ["7","8","9"]]
                    new_turn=turns()
                        
                else:
                    while run=="start":
                        value1=2
                        value2=1
                        if end=="k" or end=="K":
                            print("Thanks for playing!")
                            break
                        else:
                            print("Please Enter (K) For Exit!")
                            end=input("Enter k for exit")
                            if end=="k" or end=="K":
                                print("Thanks for playing!")
                            break
            
            


    while new_turn=="z" or new_turn=="Z":
        if value2==2:
            while new_turn=="z":
                #Single player game
                print("-------------WELCOME TO SINGLE PLAYER GAME---------------")
                #Naming players
                player_1=input("Enter Your Name Player 1: ")
                player_2="Computer"
                print(" ")
                while run=="start":
                    choose=input("Enter 0 for Head and 1 for Tail")
                    if choose.isalpha()==True:
                        print("Invalid!")
                        continue 
                    elif int(choose)!=0 and int(choose)!=1:
                        print("Invalid!")
                        continue
                    else:
                        run="notstart"
                        print("")
                choose=random.randint(0,1)
                symbol=input("Player 1 Enter your Symbol(x or o)")
                #Choosing Symbols
                if choose==0:
                    i=1
                    while new_turn=="z":
                        if symbol=="x" or symbol=="o":
                            if symbol=="x":
                                player_x="x"
                                player_y="o"
                            elif symbol=="o":
                                player_x="o"
                                player_y="x"
                            new_turn="y"
                            print(player_1,"You won the Toss!")
                        else:
                            print("Invalid!Choose symbol from X and O")
                            symbol=input("Player 1 Enter your Symbol(x or o)")
                            continue
                elif choose==1:
                    i=2
                    while new_turn=="z":
                        if symbol=="x" or symbol=="o":
                            if symbol=="x":
                                player_x="x"
                                player_y="o"
                            elif symbol=="o":
                                player_x="o"
                                player_y="x"
                            new_turn="y"
                            print(player_2,"You won the Toss!")
                        else:
                            print("Invalid!Choose symbol from X and O")
                            symbol=input("Player 1 Enter your Symbol(x or o)")
                            continue
                #Board displaying
                def display_board():
                    print(board[0][0],"|",board[0][1],"|",board[0][2])
                    print("---------")
                    print(board[1][0],"|",board[1][1],"|",board[1][2])
                    print("---------")
                    print(board[2][0],"|",board[2][1],"|",board[2][2])
                display_board()     
                #Turns
                run="start"
                while run=="start":
                    step=0
                    if i==1:
                        print(player_1,"Your Turn! ")
                        turn=input("Which position do you want from 1 to 9,Enter,and if you want to exit press e?")
                        print(" ")   
                        #End Game
                        if turn=="e" or turn=="E":
                            print("Thanks for playing!")
                            break
            
            
                    #Alpha digits:
                        if turn.isalpha()==True:
                            print("Invalid!ENter from(1 to 9)")
                            continue
                        #Invalid Numbers  
                        if int(turn)<=0 or int(turn)>=10:
                            print("Invalid number,Enter number from 1 to 9")
                            print(" ")
                            continue
                    
                        #For finding row and column:
                        if int(turn)>=1 or int(turn)<=9:
                            turn=int(turn)
                            turn=turn-1
                            row=turn//3
                            col=turn%3
            
                    
                #Position occupied
                        if board[row][col]=="x" or board[row][col]=="o":
                            print("This place is already taken!Choose another one")
                            print(" ")
                            continue
                
                #Position not occupied
                        else:
                            if board[row][col]!="x" or board[row][col]!="o":
                                board[row][col]=player_x
                        display_board()

                        if count>=8:
                            print("Tie")
                            break
                        count+=1
                        i=2
           
                    #Turns
                    elif i==2:
                        new_count=0
                        print(player_2," Your Turn")
                        if count==0 or count==1 or count==2:
                            if (board[1][1] !="x" and board[1][1]!="o")  or (board[0][0]!="x" and board[0][0] !="o") or (board[0][2]!="x" and board[0][2]!="o"):
                                if board[1][1] !="x" and board[1][1] !="o":
                                    board[1][1]=player_y
                                elif board[0][0] !="x" and board[0][0] !="o":
                                    board[0][0]=player_y
                                elif board[0][2]!="x" and board[0][2]!="o":
                                    board[0][2]=player_y
                            
                        #Winning conditions
                        if count>=3:
                            if (board[0][0]==player_y and board[0][1]==player_y) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif(board[0][1]== player_y and board[0][2]==player_y) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][0]==player_y and board[0][2]==player_y) and (board[0][1]!="x" and board[0][1]!="o"):
                                board[0][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][0]==player_y and board[1][1]==player_y) and (board[1][2]!="x" and board[1][2]!="o"):
                                board[1][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][1]==player_y and board[1][2]==player_y) and (board[1][0]!="x" and board[1][0]!="o"):
                                board[1][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][0]==player_y and board[1][2]==player_y) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[2][0]==player_y and board[2][1]==player_y) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[2][1]==player_y and board[2][2]==player_y) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[2][0]==player_y and board[2][2]==player_y) and (board[2][1]!="x" and board[2][1]!="o"):
                                board[2][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][0]==player_y and board[1][0]==player_y) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][0]==player_y and board[2][0]==player_y) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][0]==player_y and board[2][0]==player_y) and (board[1][0]!="x" and board[1][0]!="o"):
                                board[1][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][1]==player_y and board[1][1]==player_y) and (board[2][1]!="x" and board[2][1]!="o"):
                                board[2][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][1]==player_y and board[2][1]==player_y) and (board[0][1]!="x" and board[0][1]!="o"):
                                board[0][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][1]==player_y and board[2][1]==player_y) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][2]==player_y and board[1][2]==player_y) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][2]==player_y and board[2][2]==player_y) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][2]==player_y and board[2][2]==player_y) and (board[1][2]!="x" and board[1][2]!="o"):
                                board[1][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][0]==player_y and board[1][1]==player_y) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][0]==player_y and board[2][2]==player_y) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][1]==player_y and board[2][2]==player_y) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][2]==player_y and board[1][1]==player_y) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[1][1]==player_y and board[2][0]==player_y) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                            elif (board[0][2]==player_y and board[2][0]==player_y) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                                display_board()
                                print("**********Congratulation************")
                                print("Computer Win")
                                break
                        
                        
                        #Blocking Conditions
                            elif (board[0][0]==player_x and board[0][1]==player_x) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                            elif(board[0][1]== player_x and board[0][2]==player_x) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                            elif (board[0][0]==player_x and board[0][2]==player_x) and (board[0][1]!="x" and board[0][1]!="o"):
                                board[0][1]=player_y
                            elif (board[1][0]==player_x and board[1][1]==player_x) and (board[1][2]!="x" and board[1][2]!="o"):
                                board[1][2]=player_y
                            elif (board[1][1]==player_x and board[1][2]==player_x) and (board[1][0]!="x" and board[1][0]!="o"):
                                board[1][0]=player_y
                            elif (board[1][0]==player_x and board[1][2]==player_x) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                            elif (board[2][0]==player_x and board[2][1]==player_x) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                            elif (board[2][1]==player_x and board[2][2]==player_x) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                            elif (board[2][0]==player_x and board[2][2]==player_x) and (board[2][1]!="x" and board[2][1]!="o"):
                                board[2][1]=player_y
                            elif (board[0][0]==player_x and board[1][0]==player_x) and (board[2][0]!="x" and board[2][0]!="o"):
                                 board[2][0]=player_y
                            elif (board[1][0]==player_x and board[2][0]==player_x) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                            elif (board[0][0]==player_x and board[2][0]==player_x) and (board[1][0]!="x" and board[1][0]!="o"):
                                board[1][0]=player_y
                            elif (board[0][1]==player_x and board[1][1]==player_x) and (board[2][1]!="x" and board[2][1]!="o"):
                                board[2][1]=player_y
                            elif (board[1][1]==player_x and board[2][1]==player_x) and (board[0][1]!="x" and board[0][1]!="o"):
                                board[0][1]=player_y
                            elif (board[0][1]==player_x and board[2][1]==player_x) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                            elif (board[0][2]==player_x and board[1][2]==player_x) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                            elif (board[1][2]==player_x and board[2][2]==player_x) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                            elif (board[0][2]==player_x and board[2][2]==player_x) and (board[1][2]!="x" and board[1][2]!="o"):
                                board[1][2]=player_y
                            elif (board[0][0]==player_x and board[1][1]==player_x) and (board[2][2]!="x" and board[2][2]!="o"):
                                board[2][2]=player_y
                            elif (board[0][0]==player_x and board[2][2]==player_x) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                            elif (board[1][1]==player_x and board[2][2]==player_x) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                            elif (board[0][2]==player_x and board[1][1]==player_x) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                            elif (board[1][1]==player_x and board[2][0]==player_x) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                            elif (board[0][2]==player_x and board[2][0]==player_x) and (board[1][1]!="x" and board[1][1]!="o"):
                                board[1][1]=player_y
                            # other conditions
                            elif (board[0][0]==player_x and board[1][1]==player_y and board[2][2]==player_x) and (board[1][2]!="x" and board[1][2]!="o"):
                                board[1][2]=player_y
                            elif (board[0][2]==player_x and board[1][1]==player_y and board[2][0]==player_x) and (board[1][0]!="x" and board[1][0]!="o"):
                                board[1][0]=player_y   
                            elif (board[0][0]==player_y and board[1][1]==player_x and board[2][2]==player_x) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                            elif (board[0][2]==player_y and board[1][1]==player_x and board[2][0]==player_x) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                            elif (board[1][1]==player_y and board[0][1]==player_x and board[1][2]==player_x) and (board[0][0]!="x" and board[0][0]!="o"):
                                board[0][0]=player_y
                            elif (board[0][1]==player_x and board[1][1]==player_y and board[2][1]==player_x) and (board[2][0]!="x" and board[2][0]!="o"):
                                board[2][0]=player_y
                            elif (board[1][0]==player_x and board[1][1]==player_y and board[1][2]==player_x) and (board[0][2]!="x" and board[0][2]!="o"):
                                board[0][2]=player_y
                                    
                    #[1,9 then put in 6]
                            elif (board[0][0] == player_x) and (board[2][2] == player_x) and (board[1][2] != player_x) and (board[1][2] != player_y):
                                board[1][2] = player_y
                    #[3,7 then put in 4]
                            elif (board[2][0] == player_x) and (board[0][2] == player_x) and (board[1][0] != player_x) and (board[1][0] != player_y):
                                board[1][0] = player_y
                    #[9,2 then 3]
                            elif (board[2][2] == player_x) and (board[0][1] == player_x) and (board[0][2] != player_x) and (board[0][2] != player_y):
                                board[0][2] = player_y    
                        #[7,2 then 3]
                            elif (board[2][0] == player_x) and (board[0][1] == player_x) and (board[0][2] != player_x) and (board[0][2] != player_y):
                                board[0][2] = player_y   
                        #[1,8 then 9]
                            elif (board[0][0] == player_x) and (board[2][1] == player_x) and (board[2][2] != player_x) and (board[2][2] != player_y):
                                board[2][2] = player_y  
                        #[3,8 then 9]
                            elif (board[0][2] == player_x) and (board[2][1] == player_x) and (board[2][2] != player_x) and (board[2][2] != player_y):
                                board[2][2] = player_y
                            
                        #[7,6 then 9]
                            elif (board[2][0] == player_x) and (board[1][2] == player_x) and (board[2][2] != player_x) and (board[2][2] != player_y):
                                board[2][2] = player_y
                            
                        #[1,6 then 9]
                            elif (board[0][0] == player_x) and (board[1][2] == player_x) and (board[2][2] != player_x) and (board[2][2] != player_y):
                                board[2][2] = player_y
                            
                        #[9,4 then 1]
                            elif (board[2][2] == player_x) and (board[1][0] == player_x) and (board[0][0] != player_x) and (board[0][0] != player_y):
                                board[0][0] = player_y
                            
                        #[3,4 then 1]
                            elif (board[0][2] == player_x) and (board[1][0] == player_x) and (board[0][0] != player_x) and (board[0][0] != player_y):
                                board[0][0] = player_y
                        #if 6 and 8 then 3
                            elif (board[1][2] == player_x) and (board[2][1] == player_x) and (board[0][2] != player_x) and (board[0][2] != player_y):
                                board[0][2] = player_y
                        #if 6 and 8 then 7
                            elif (board[1][2] == player_x) and (board[2][1] == player_x) and (board[2][0] != player_x) and (board[2][0] != player_y):
                                board[2][0] = player_y
                        # if 1 and 8 then 7
                            elif (board[0][0] == player_x) and (board[2][1] == player_x) and (board[2][0] != player_x) and (board[2][0] != player_y):
                                board[2][0] = player_y
                        # if 4 and 8 then 3
                            elif (board[1][0] == player_x) and (board[2][1] == player_x) and (board[2][0] != player_x) and (board[2][0] != player_y):
                                board[2][0] = player_y
                        #if  2 and 4 then 1
                            elif (board[0][1] == player_x) and (board[1][0] == player_x) and (board[0][0] != player_x) and (board[0][0] != player_y):
                                board[0][0] = player_y
                                 
                        #if 4 and 9 then 3
                            elif (board[1][0] == player_x) and (board[2][2] == player_x) and (board[0][2] != player_x) and (board[0][2] != player_y):
                                board[0][2] = player_y
                                
                        #if 3 and 9 then 2
                            elif (board[0][2] == player_x) and (board[2][2] == player_x) and (board[0][1] != player_x) and (board[0][1] != player_y):
                                board[0][1] = player_y   
                                
                        #New
                        #if 2 and 4 then 6
                            elif (board[0][1] == player_x) and (board[1][0] == player_x) and (board[1][2] != player_x) and (board[1][2] != player_y):
                                board[1][2] = player_y
                        #if 2 and 6 then 4
                            elif (board[0][1] == player_x) and (board[1][2] == player_x) and (board[1][0] != player_x) and (board[1][0] != player_y):
                                board[1][0] = player_y
                        #if 2 and 6 then 8
                            elif (board[0][1] == player_x) and (board[1][2] == player_x) and (board[2][1] != player_x) and (board[2][1] != player_y):
                                board[2][1] = player_y
                        #if 6 and 8 then 2
                            elif (board[1][2] == player_x) and (board[2][1] == player_x) and (board[0][1] != player_x) and (board[0][1] != player_y):
                                board[0][1] = player_y
                        #if 2and 9 then 6
                            elif (board[0][1] == player_x) and (board[2][2] == player_x) and (board[1][2] != player_x) and (board[1][2] != player_y):
                                board[1][2] = player_y
                        #if 2 and 7 then 4
                            elif (board[0][1] == player_x) and (board[2][0] == player_x) and (board[1][0] != player_x) and (board[1][0] != player_y):
                                board[1][0] = player_y
                        #if 2 and 9 then 7
                            elif (board[0][1] == player_x) and (board[2][2] == player_x) and (board[2][0] != player_x) and (board[2][0] != player_y):
                                board[2][0] = player_y
                        #if 2 and 4 then 8
                            elif (board[0][1] == player_x) and (board[1][0] == player_x) and (board[2][1] != player_x) and (board[2][1] != player_y):
                                board[2][1] = player_y
                        
                        display_board()
                        if count>=8:
                            print("Tie")
                            break
                        count+=1
                        i=1

                print("Match is over!")
                print(" ")
                end=input("If you want to play again then Enter z !otherwise Enter k")
                if end=="z" or end=="Z":
                     board=[["1","2","3"],
                           ["4","5","6"],
                           ["7","8","9"]]
                     count=0
                     new_turn=turns()
                        
                else:
                    while run=="start":
                        value1=2
                        value2=1
                        if end=="k" or end=="K":
                            print("Thanks for playing!")
                            break
                        else:
                            print("Please Enter (K) For Exit!")
                            end=input("Enter k for exit")
                            if end=="k" or end=="K":
                                print("Thanks for playing!")
                                break
            
            
        
        


        
        
