questions_dict = {"Easy":{"1-> Capital of Gujarat ?":["(a): Ahmedabad","(b): Surat","(c): Gandhinagar","(d): Rajkot"],"2-> Capital of Maharashtra ???":["(a): Pune","(b): Mumbai","(c): New york","(d): Nagpur"],"3-> Captian of Indian Cricket team ??":["(a): Virat Kolhi","(b): M S Dhoni","(c): Rohit Sharma","(d): Ajinkya Rahane"],"4-> President of BCCI":["(a): Sunil Gavaskar","(b): Sachin tendulkar","(c): Rahul Dravid","(d): Sourabh Ganguly"]},"Intermediate":{"1-> Largest mamal ??":["(a): Lion","(b): blue wale","(c): Elephant","(d): Tiger"],"2-> Home minister of India ??":["(a): Amit Shah","(b): Yogi Adityanath","(c): Narendra Singh Tomar","(d): Ashok Ghelot"],"3-> Fastest animal ??":["(a): leopard","(b): panther","(c): Cheetah","(d): Lioness"]},"Hard":{"1-> value of gravitational force in meter per second square ??":["(a): 9.8","(b): 10","(c): 11","(d): 9.72"],"2-> The Central Rice Research Station is situated in ??":["(a): Chennai","(b): Cuttack","(c): Bangalore","(d): Quilon"],"3-> Who among the following wrote Sanskrit grammar?":["(a): Kalidasa","(b): Charak","(c): Panini","(d): Aryabhatt"]}}
answers_list = ["c","b","a","d","b","a","c","a","b","c"]
def UserloginAccount():
	playername = input("Please enter your name \n")
	print("\n","Hi", playername)




def play():
    user_answers = []

    UserloginAccount()
    print("\nLets Start with the Quiz")
    for i, j in questions_dict["Easy"].items():
        print("Questions. (Level: Easy)")
        print("\t", i)
        print("Options")
        for k in j:
            print("\t", k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)
    for i, j in questions_dict["Intermediate"].items():
        print("Questins. (Level: Intermediate)")
        print("\t", i)
        print("Options")
        for k in j:
            print("\t", k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)
    for i, j in questions_dict["Hard"].items():
        print("Questins. (Level: Hard)")
        print("\t", i)
        print("Options")
        for k in j:
            print("\t", k)
        print("  Enter your option:")
        ans = input()
        user_answers.append(ans)

    count = 0
    for i in range(len(user_answers)):
        if user_answers[i] == answers_list[i]:
            count += 1

    print("Your Score is :")
    print(count)
    user_answers = []



def addquizQuestions():
    print("Process of adding question starts::::::")
    print("\n")
    typeofquestion = input("Please enter the type of question you would like to add.\tEasy\tIntermediate\tHard->")
    removequestions(typeofquestion)
    question = input("Please enter the question.")
    options = []
    for i in range(97, 101):
        temp = input("Please enter the option ")
        final = "(" + chr(i) + ")" + temp
        options.append(final)

    answer=input("enter answer")
    answers_list.insert(4,answer)
    if typeofquestion == "Easy":
        questions_dict["Easy"][question] = options
    elif typeofquestion == "Intermediate":
        questions_dict["Intermediate"][question] = options
    elif typeofquestion == "Hard":
        questions_dict["Hard"][question] = options
    else:
        print("Invalid Option")

def removequestions(typeof):
    print("\nPlease remove the question first before adding more questions to the question list")
    if typeof == "Easy":
        for i,j in questions_dict["Easy"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Easy"].pop(i)
                break
            else:
                continue
    elif typeof == "Intermediate":
        for i,j in questions_dict["Intermediate"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Intermediate"].pop(i)
                break
            else:
                continue
    elif typeof == "Hard":
        for i,j in questions_dict["Hard"].items():
            print(i)
            print("Do you want to remove this question? Y or N")
            x = input()
            if x == "Y" or x == "y":
                questions_dict["Hard"].pop(i)
                break
            else:
                continue
    else:
        print("Please choose the correst parameter")
choice = 1
while choice != 7:
    print('\n=========WELCOME TO QUIZ MASTER==========')
    print('-----------------------------------------')
    print('Press 1 for User:')
    print('Press 2 for SuperUser:')
    print('Press 3 to Exit:')
    choice = int(input('ENTER YOUR CHOICE: '))
    if choice == 1:
        play()
    elif choice == 2:
        supername = input("Enter your name: ")
        if supername == "SuperUser":


            superfunction=1
            while superfunction!=4:
                print('\n=========WELCOME SUPERUSER==========')
                print('-----------------------------------------')
                print('Press 1 to add questions:')
                print('Press 2 to remove questions:')
                print('Press 3 to Exit:')
                superfunction = int(input('ENTER YOUR CHOICE: '))
                if superfunction == 1:
                    addquizQuestions()
                elif superfunction == 2:
                    removequestions()
                elif superfunction == 3:
                    break
                else:
                    print("Enter valid input")


        else:
            print(supername, "you are not authorized to make changes in the question")
    elif choice == 3:
        exit()
        break
    else:
        print('WRONG INPUT. ENTER THE CHOICE AGAIN')


