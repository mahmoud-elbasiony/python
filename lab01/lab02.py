# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]

def reduce_list(list):
    for i in range(len(list)):
        list[i]=round(list[i])
    print(list)

reduce_list([1,2,3.3])

# 2
def divide_string(*args):
    front=""
    back=""
    for arg in args:
        length=len(arg)
        if length%2: #odd
            front+=arg[:length//2+1]
            back+=arg[length//2+1:]
            # print ("odd",length//2+1,front,back)
        else:
            front+=arg[:length//2]
            back+=arg[length//2:]
            # print ("even",length//2)
        
    print(f"front: {front}, back: {back}")

divide_string("mahmoud","ali")

# 3- Write a Python function that takes a sequence of numbers and determines
def is_deffirent(*args):
    for i in range(len(args)):
        for j in range(i+1,len(args)):
            if args[i]==args[j]:
                return False
    
    return True

print("[1,5,7,9] -> True: ",is_deffirent(1,5,7,9))
print("[2,4,5,5,7,9] -> False: ",is_deffirent(1,5,5,7,9))

# 4- Given unordered list, sort it using algorithm bubble sort

def bubble_sort(list):
    flag=True
    for i in range(len(list)):
        if not flag:
            return list
        
        flag=False
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                flag=True
    return list

print("sorted list: ",bubble_sort([1,2,3,4,5,6,7,8,9,0]))

# 5- Gusses game
import random
def gusses_game(tries=10):
    n=1
    rand=random.randint(0,100)
    gusses=set()
    while n<= tries:
        print(f"\ntry number: {n}")
        guess=int(input(f"\nEnter number:\n"))
        if guess > 100 or guess <0:
            print("\nonly numbers between 0 and 100 try again\n")
            continue
        if guess in gusses:
            print("\nyou already guessed this number before try again\n")
            continue

        gusses.add(guess)
        if guess>rand:
            print("\ntry smaller\n")
        elif guess<rand:
            print("\ntry bigger\n")
        else:
            print("\nbingooo\n")
            answer=input(f"\nDo you want to play again?y:n\n")
            if answer.lower()=="y":
                gusses_game()
                
            break
        n+=1
    if n>10:
        print("\nGameOver\n")
        answer=input(f"\nDo you want to play again?y:n\n")
        if answer.lower()=="y":
            gusses_game()
            
        
gusses_game(tries=10)