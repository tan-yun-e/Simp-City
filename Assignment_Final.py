#Tan Yun-E CSF01 9/8/21
#This program allows the user to assume the role of the mayor of Simp City.
#They are given a 4x4 grid and 5 fixed buildings to use while building.
#Users can view how many buildings left they can use, their accumulated points,
#and save their progress to come back to it later.
#They can only build buildings orthagonally  
import random

def print_options(): #show the options when you start a game
    print()
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Show high scores")
    print()
    print("0. Exit")

def options_code(op1,op2): #show the options once you start a game
    print("1. Build a", op1 )
    print("2. Build a", op2 )
    print("3. See remaining buildings")
    print("4. See current score")
    print()
    print("5. Save game")
    print("0. Exit to main menu")

def game_code(n): #prints the 4x4 board 
    print()
    print("Turn",n)
    for y in range(len(line_list)):
        print(''.join(line_list[y]),end='')
        print("  +-----+-----+-----+-----+")
        y +=1
    options_code(op1,op2)

def print_file(file):
    y=0
    line_list=[]
    for line in file:
        if line[0].isdigit():
            break
        else:
            line=line.split(',')
            line_list.append(line)
            print(''.join(line_list[y]),end='')
            print("  +-----+-----+-----+-----+")
            y +=1
    return line_list

def building_option(n):
    if n==1:
        n='BCH'
    elif n==2:
        n='FAC'
    elif n==3:
        n='HSE'
    elif n==4:
        n='SHP'
    elif n==5:
        n='HWY'
    return n

def print_highscores():                      
    value_list=list(highscores.values())
    key_list=list(highscores.keys())
    print('--------- HIGH SCORES ---------')
    print('Pos Player                Score')
    print('--- ------                -----') 
    rank=1
    while len(value_list)>0:
        highest=0
        for i in range(len(value_list)):    
            remainder=highest-value_list[i]
            if remainder<0:
                highest=value_list[i]        
        position = value_list.index(highest)
        user = key_list[position]
        print('{:>2d}. {:<20s}{:>7d}'.format(rank,user,highest))
        value_list.pop(position)
        key_list.pop(position)
        rank=rank+1
    print('-------------------------------')

def points_system(line_list):
    total_points= []
    for row in range(len(line_list)):
        y=line_list[row]   
        count=y.count('HWY')
        if count==4:   
            for i in range(count):
                HWY_points.append(4)
                HWY_points_s.append('4')
        if count==3:
            if line_list[row][1]=='HWY':
                if line_list[row][3]=='HWY' and line_list[row][5]=='HWY':
                    for i in range(3):
                        HWY_points.append(3)
                        HWY_points_s.append('3')
                else:
                    if line_list[row][3]=='HWY':
                        for i in range(2):
                            HWY_points.append(2)
                            HWY_points_s.append('2')
                        HWY_points.append(1)
                        HWY_points_s.append('1')
                    if line_list[row][5]=='HWY':
                        HWY_points.append(1)
                        HWY_points_s.append('1')
                        for i in range(2):
                            HWY_points.append(2)
                            HWY_points_s.append('2')
            elif line_list[row][3]=='HWY':
                for i in range(3):
                    HWY_points.append(3)
                    HWY_points_s.append('3')
        if count==2:
            if line_list[row][1]=='HWY':
                if line_list[row][3]=='HWY':
                    for i in range(2):
                        HWY_points.append(2)
                        HWY_points_s.append('2')
                else:
                    for i in range(2):
                        HWY_points.append(1)
                        HWY_points_s.append('1')
            elif line_list[row][3]=='HWY':
                if line_list[row][5]=='HWY':
                    for i in range(2):
                        HWY_points.append(2)
                        HWY_points_s.append('2')
                else:
                    for i in range(2):
                        HWY_points.append(1)
                        HWY_points_s.append('1')
            elif line_list[row][5]=='HWY':
                if line_list[row][7]=='HWY':
                    for i in range(2):
                        HWY_points.append(2)
                        HWY_points_s.append('2')
                else:
                    for i in range(2):
                        HWY_points.append(1)
                        HWY_points_s.append('1')
        if count==1:
            HWY_points.append(1)
            HWY_points_s.append('1')
                                                                      
        for col in range(len(line_list[row])):
            if line_list[row][col]=='BCH': #points for beach
                if col==1 or col==7:
                    BCH_points.append(3)
                    BCH_points_s.append('3')
                else:
                    BCH_points.append(1)
                    BCH_points_s.append('1')

            if line_list[row][col]=='FAC':
                FAC_list.append('i')

            if line_list[row][col]=='HSE': 
                surround=[]
                check=True
                if (row==3 or row==2) and (col==3 or col==5): 
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif row==1 and (col==3 or col==5):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif row==4 and (col==3 or col==5):
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif col==1 and (row==3 or row==2):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                elif col==7 and (row==3 or row==2):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col-2])
                elif row==1 and col==7:
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col-2])
                elif row==4 and col==7:
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col-2])
                elif row==1 and col==1:
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col+2])
                elif row==4 and col==1:
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                if surround.count('FAC')>0:
                    HSE_points.append(1)
                    HSE_points_s.append('1')
                    check=False
                if check==True:
                    for i in surround:
                        if i=='BCH':
                            HSE_points.append(2)
                            HSE_points_s.append('2')
                        elif i=='SHP' or i=='HSE':
                            HSE_points.append(1)
                            HSE_points_s.append('1')

            if line_list[row][col]=='SHP':
                surround=[]
                if (row==3 or row==2) and (col==3 or col==5):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif row==1 and (col==3 or col==5):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif row==4 and (col==3 or col==5):
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                    surround.append(line_list[row][col-2])
                elif col==1 and (row==3 or row==2):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                elif col==7 and (row==3 or row==2):
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col-2])
                elif row==1 and col==7:
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col-2])
                elif row==4 and col==7:
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col-2])
                elif row==1 and col==1:
                    surround.append(line_list[row+1][col])
                    surround.append(line_list[row][col+2])
                elif row==4 and col==1:
                    surround.append(line_list[row-1][col])
                    surround.append(line_list[row][col+2])
                for i in surround:
                    if i=='   ':
                        surround.pop(surround.index(i))
                for i in surround:
                    if i=='   ':
                        surround.pop(surround.index(i))
                for i in surround:
                    if i=='HWY':
                        surround.pop(surround.index(i))
                n=0
                for i in surround:
                    if surround.count(i)>1:
                        n=surround.count(i)-1
                SHP_points.append(len(surround)-n)
                SHP_points_s.append(str(len(surround)-n))                    
    total_num=len(FAC_list)
    if total_num>4:
        for i in range(4):
            FAC_points.append(4)
            FAC_points_s.append('4')
        for i in range(total_num-4):
            FAC_points.append(1)
            FAC_points_s.append('1')
    else:
        for i in range(total_num):
            FAC_points.append(total_num)
            FAC_points_s.append(str(total_num))
    for y in range(len(type_name)):
        x=points_list_s[y]
        print("{}: {} = {}".format(type_name[y],' + '.join(x),sum(points_list[y])))
        x=sum(points_list[y])
        total_points.append(x)
    total_point=sum(total_points)
    print('Total score: {}'.format(total_point))
    return total_point

print("Welcome, mayor of Simp City!")
print("----------------------------")
building_list=[]
game=True
type_name=['HSE','FAC','SHP','HWY','BCH']
print_options()
start_game=False
choice=0
highscores={}

while not(start_game==True) or choice==3 or choice==0: #check for correct input
    choice=input("Your choice? ")
    if choice.isdigit():
        choice=int(choice)
    if choice==1:#starting a new save file
        filename="game_file.csv"
        n=1
        start_game=True
    elif choice==2:#
        filename="savefile.csv"
        file=open(filename,'r')
        for i in range(5):
            file.readline()
        n=file.readline()
        n=n.split(',')
        n=int(n[0])
        building_list=file.readline()
        building_list=building_list.split(',')
        if building_list[0]=='':
            building_list.pop(0)
        start_game=True
    elif choice==3:
        print_highscores()
    elif choice==0:
        print_options()
        
    else:
        print("Please choose a valid option.")
        



  
y=0
line_list=[]
file=open(filename,'r')
print()
print("Turn",n)
for line in file:
    if line[0].isdigit():
        break
    else:
        line=line.split(',')
        line_list.append(line)
        print(''.join(line_list[y]),end='')
        print("  +-----+-----+-----+-----+")
        y +=1
    
op1=random.randint(1,5)#random house options
op1=building_option(op1)
op2=random.randint(1,5)
op2=building_option(op2)
options_code(op1,op2)
    
while n<17 and game==True: 
    option=input("Your choice? ")
    if option.isdigit():#for correct input
        option=int(option)
    
    if option==1 or option==2: #for building the building
        new_build=input("Build where? ")#option to build
        pop=True
        repeat=0
        if len(new_build)==2 and (new_build[1].isdigit() and (new_build[1]=='1' or new_build[1]=='2' or new_build[1]=='3' or new_build[1]=='4')) and (new_build[0]=='a' or new_build[0]=='b' or new_build[0]=='c' or new_build[0]=='d'):
            #for correct input
            building_list.append(new_build)
            first_letter=new_build[0]
            first_number=new_build[1]
            build=0
            builds=0
            if first_letter=='a':
                first_letter=1
            elif first_letter=='b':
                first_letter=3
            elif first_letter=='c':
                first_letter=5
            elif first_letter=='d':
                first_letter=7
            first_number=int(first_number)
            if len(building_list)>0:
                for structure in range(len(building_list)-1): #check if it is built correctly
                    check1=building_list[structure][0]
                    check2=building_list[structure][1]
                    if check1=='a':
                        check1=1
                    elif check1=='b':
                        check1=3
                    elif check1=='c':
                        check1=5
                    elif check1=='d':
                        check1=7
                    check2=int(check2)
                    if check2==first_number and check1==first_letter:
                        repeat=True
                    if check1==first_letter and (check2==first_number+1 or check2==first_number-1):
                        build=True
                    elif check2==first_number and (check1==first_letter+2 or check1==first_letter-2):
                        build=True
                    if build==True:
                        builds=True
        else: #for incorrect input
            builds=False
            pop=False
            print("Please choose a valid option.")
        if (n==1 and len(new_build)==2) or (n>1 and builds==True) and not(repeat==True): #build the building
            building_choice=[op1,op2]
            i=first_number           
            line_list[i].pop(first_letter)
            line_list[i].insert(first_letter,building_choice[option-1])
            op1=random.randint(1,5)#random house options
            op1=building_option(op1)
            op2=random.randint(1,5)
            op2=building_option(op2)
            n+=1
        elif pop==True or repeat==True:
            print("You must build next to an existing building.")
            building_list.pop()
        if n<17:
            game_code(n)


    if option==5: #save file and continue the game
        file=open("savefile.csv",'w')
        save=','.join(line_list[0])
        file.write(save)
        for y in range(4):
            save=','.join(line_list[y+1])
            file.write(save)
        file.write(str(n)+'\n')
        building_lists=','.join(building_list)
        file.write(building_lists)
        file=open('savefile.csv','r')
        print()
        print('Game saved!')


    if option==3: #show remaining buildings
        HWY=8
        HSE=8
        SHP=8
        BCH=8
        FAC=8
        for row in line_list: #checks each square for the building and -1 for the corresponding building
            for col in row:
                if col=='HWY':
                    HWY=HWY-1
                if col=='SHP':
                    SHP=SHP-1
                if col=='FAC':
                    FAC=FAC-1
                if col=='HSE':
                    HSE=HSE-1
                if col=='BCH':
                    BCH=BCH-1
        type_list=[HSE,FAC,SHP,HWY,BCH]        
        print()#print the buildings left
        print("{:20s}{}".format("Building",'Remaining'))
        print("{:20s}{}".format("--------",'---------'))    
        for i in range(len(type_list)):
            print("{:20s}{}".format(type_name[i],type_list[i]))
    if option==0: #Exit to main menu and start a new round
        print_options()
        choice=int(input("Your choice? "))
        start_game=False
        while not(start_game==True) or choice==3 or choice==0: #check for correct input    
            if choice==1:#starting a new save file
                filename="game_file.csv"
                n=1
                start_game=True
            elif choice==2:#opening a saved file
                filename="savefile.csv"
                file=open(filename,'r')
                for i in range(5):
                    file.readline()
                n=file.readline()
                n=n.split(',')
                n=int(n[0])
                building_list=file.readline()
                building_list=building_list.split(',')
                building_list.pop(0)
                start_game=True
            elif choice==3:
                print_highscores()
                print_options()
                choice=int(input("Your choice? "))
            elif choice==0:
                print_options()
                choice=int(input("Your choice? "))
                
            else: #for incorrect input
                print("Please choose a valid option.")
        y=0
        line_list=[]
        file=open(filename,'r')
        print()
        print("Turn",n)
        for line in file:
            if line[0].isdigit():
                break
            else:
                line=line.split(',')
                line_list.append(line)
                print(''.join(line_list[y]),end='')
                print("  +-----+-----+-----+-----+")
                y +=1
        op1=random.randint(1,5) 
        op1=building_option(op1)
        op2=random.randint(1,5)
        op2=building_option(op2)
        options_code(op1,op2)
    if option==4: #points system
        HSE_points=[]
        FAC_points=[]
        SHP_points=[]
        HWY_points=[]
        BCH_points=[]
        HSE_points_s=[]
        FAC_points_s=[]
        SHP_points_s=[]
        HWY_points_s=[]
        BCH_points_s=[]
        points_list=[HSE_points,FAC_points,SHP_points,HWY_points,BCH_points]
        points_list_s=[HSE_points_s,FAC_points_s,SHP_points_s,HWY_points_s,BCH_points_s]
        FAC_list=[]
        points_system(line_list)  
    if not(option==1 or option==2 or option==3 or option==4 or option==5):
        print("Please choose a valid option.")
        
        

#The end of the game        
    if n==17:
        n=1
        print()    #print final layout
        print("Final layout of Simp City:")
        for y in range(len(line_list)):
            print(''.join(line_list[y]),end='')
            print("  +-----+-----+-----+-----+")
            y +=1
        HSE_points=[]   #points system
        FAC_points=[]
        SHP_points=[]
        HWY_points=[]
        BCH_points=[]
        HSE_points_s=[]
        FAC_points_s=[]
        SHP_points_s=[]
        HWY_points_s=[]
        BCH_points_s=[]
        points_list=[HSE_points,FAC_points,SHP_points,HWY_points,BCH_points]
        points_list_s=[HSE_points_s,FAC_points_s,SHP_points_s,HWY_points_s,BCH_points_s]
        FAC_list=[]
        points=points_system(line_list)
        higher=0
        val_list_s=[]
        for n in highscores:  #find if there is a new highscore
            compare=int(highscores[n])
            remainder=points-compare
            if remainder>0:
                higher=True
        if higher==True or len(highscores)<=10: #finding out ranking
            val_list=list(highscores.values())
            val_list.append(points)
            val_list=sorted(val_list)
            new_rank=val_list.index(points)+1
            for i in range(len(val_list)):
                print(len(val_list))
                n=val_list[len(val_list)-i-1]
                val_list_s.append(n)
            new_rank=val_list_s.index(points)+1
            print("Congratulations! You made the high score board at position {}!".format(new_rank))
            repeats=0
            name=input("Please enter your name (max 20 chars): ")
            while len(name)>19:
                print("Name too long.")
                name=input("Please enter your name (max 20 chars): ")
            for i in highscores.keys():
                if i==name:
                    repeats=True
            while repeats==True: 
                repeats=0
                name=input("No repeat names allowed, enter new name:")
                for i in highscores.keys():
                    if i==name:
                        repeats=True
            print(len(highscores))        
            highscores[name]= points
            if len(highscores)>10:
                value_list=list(highscores.values())
                key_list=list(highscores.keys())
                lower=300
                for i in range(len(value_list)):
                
                    remainder=lower-value_list[i]
                    print(lower)
                    if remainder>0:
                        lower=value_list[i]
                position = value_list.index(lower)
                user= key_list[position]
                highscores.pop(user,lower)
            print_highscores()
        #return to menu
        print_options()
        choice=input("Your choice? ")
        if choice.isdigit():
            choice=int(choice)
            if choice==1:#starting a new save file
                filename="game_file.csv"
                n=1
                start_game=True
            if choice==2:#
                filename="savefile.csv"
                file=open(filename,'r')
                for i in range(5):
                    file.readline()
                n=file.readline()
                n=n.split(',')
                n=int(n[0])
                building_list=file.readline()
                building_list=building_list.split(',')
                if building_list[0]=='':
                    building_list.pop(0)
                start_game=True
            else:
                print("Please choose a valid option.")
        else:
            print("Please choose a valid option.")
        y=0
        line_list=[]
        file=open(filename,'r')
        print()
        print("Turn",n)
        for line in file:
            if line[0].isdigit():
                break
            else:
                line=line.split(',')
                line_list.append(line)
                print(''.join(line_list[y]),end='')
                print("  +-----+-----+-----+-----+")
                y +=1
        op1=random.randint(1,5)#random house options
        op1=building_option(op1)
        op2=random.randint(1,5)
        op2=building_option(op2)
        options_code(op1,op2)
        
        
        
        
            



    


            

    



