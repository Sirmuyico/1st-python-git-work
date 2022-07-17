import random

number_of_trail = 3

guess = 0

point = 5


num = list(range(53, 74))

random.shuffle(num)



com_choice = random.choice(num)
while guess < number_of_trail:
        print("Welcome to my game")
        print("You can select from the list below.")
        print(num)
        user_choice = int(input(">  "))
        guess = guess +1
        if user_choice in num:
            if user_choice == com_choice:
                print("You win!")
                print(f'your point is {point}')
                print(f"Computer choice: {com_choice}")
                

                print('Do you want to replay')
                while True:
                    response = str(input("yes to play again and no to quit>  "))
                    if response.lower() == "yes":
                        print("welcome back")
                        break
                    else:
                        print("You made good effort ")
                
            
        
            
            else:
                if user_choice > com_choice:
                    print("Too High")
                    print(f"Computer choice: {com_choice}")
                    print('Try again later')
                    break


                else:
                    print("Too low")
                    print(f"Computer choice: {com_choice}")
                    print('Try again later')
                    break
                    
           
        else:
            print("Invalid input")
            break
        




