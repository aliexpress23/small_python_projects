import random
def question():
    return int(input("guess a number "))


random_number = int(random.randint(1,100))

while True:
    player = question()
    if player == random_number:
        print("correct")
        break
        
    elif player > random_number:
        print("over")
    else:
        print("under")
        



