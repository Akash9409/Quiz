que_ans_ops = {
    1 : ['Capital of Gujarat ?' , 'Ahmedabad' , ['Ahmedabad' , 'Surat' , 'Gandhinagar' , 'Rajkot']] ,
    2 : ['Capital of Maharashtra ?' , 'Mumbai' , ['Pune' , 'Mumbai' , 'New york' , 'Nagpur']] ,
    3 : ['Captian of Indian Cricket team ?' , 'M S Dhoni' ,
         ['Virat Kolhi' , 'M S Dhoni' , 'Rohit Sharma' , 'Ajinkya Rahane']] ,
    4 : ['President of BCCI' , 'Sunil Gavaskar' ,
         ['Sunil Gavaskar' , 'Sachin tendulkar' , 'Rahul Dravid' , 'Sourabh Ganguly']] ,
    5 : ['Largest mamal ?' , 'blue wale' , ['Lion' , 'blue whale' , 'Elephant' , 'Tiger']] ,
    6 : ['Home minister of India ?' , 'Amit Shah' ,
         ['Amit Shah' , 'Yogi Adityanath' , 'Narendra Singh Tomar' , 'Ashok Ghelot']] ,
}

level = {'easy' : [1 , 2] , 'normal' : [3 , 4] , 'hard' : [5,6]}

count = 0


def show_question(que , ops) :
    try :
        print ( 'Q.:' , que )
        # print('ans:', ans)
        print ( '(a)' , ops[0] , end='   ' )
        print ( '(b)' , ops[1] , end='   ' )
        print ( '(c)' , ops[2] , end='   ' )
        print ( '(d)' , ops[3] )

    except KeyError :
        print ( 'no more questions.' )


def selected_option(ops) :
    ans = input ( "Enter your correct option: " )
    if ans == 'a' :
        return ops[0]  # first value is key second list item index, key: options[1], index: [0]
    elif ans == 'b' :
        return ops[1]
    elif ans == 'c' :
        return ops[2]
    elif ans == 'd' :
        return ops[3]
    else :
        print ( 'option is invalid.' )


def check_ans(selected_ans , ans) :
    global count
    # make action after correct ans

    try :
        if selected_ans in ans :
            print ( 'correct answer!\n' )
            count += 1
        else :
            print("Wrong answer \n")
            print ( ans , 'Is the correct answer' )

    except TypeError :
        print ( 'incorrect option, Try again.\n' )


def set_question_no(q_no) :
    que = que_ans_ops[q_no][0]
    ans = que_ans_ops[q_no][1]
    ops = que_ans_ops[q_no][2]
    return que , ans , ops


def group_quiz(selected_q) :
    for q_no in selected_q :
        que , ans , ops = set_question_no ( q_no )
        show_question ( que , ops )
        selected_ans = selected_option ( ops )
        check_ans ( selected_ans , ans )


# def addquizQuestions() :
# print ( "we are in add questions" )
def add_que_ans_ops() :
    level = input ( "e: for Easy \nn: for Normal \nh: for Hard \nEnter dificulty lavel:" )
    question = input ( "Enter question here:" )
    ans = input ( "Enter correct answer:" )
    ans_op = input ( "NOTE: use coma ',' for difrent options\nEnter your options :" ).split ( ',' )
    que_ans = [question , ans]
    # update_question_option ( level , que_ans , ans_op )

    # level, que_ans, ans_op = add_que_ans_ops()

    # update_question_option ( )
    return level , que_ans , ans_op


def update_question_option(level , que_ans , ans_op) :
    for n in range ( 1 , 101 ) :
        if n not in que_ans :
            que_ans.update ( {n : que_ans} )
            options.update ( {n : ans_op} )
            if level == 'e' :
                easy.append ( n )
            if level == 'n' :
                normal.append ( n )
            if level == 'h' :
                hard.append ( n )
            break


def remove() :
    # print ( "we are in remove" )
    d =int(input("Enter the key of the question that you want to delete:"))
    que_ans_ops.pop(d)


def play() :
    # print ( "We are in play" )
    nm=input("Enter your name:")

    print ( "\n Hi",nm)
    print ( " Your Quiz Starts now:" )
    print ( "Level: Easy:" )
    group_quiz ( level['easy'] )
    print ( "Level: normal:" )
    group_quiz ( level['normal'] )
    print ( "Level: Hard" )
    group_quiz ( level['hard'] )
    print ( nm, "your score is:" , count )


choice = 1
while choice != 7 :
    try :
        print ( '\n=========WELCOME TO QUIZ==========' )
        print ( '-----------------------------------------' )
        print ( 'Press 1 for User:' )
        print ( 'Press 2 for SuperUser:' )
        print ( 'Press 3 to Exit:' )
        choice = input ( 'ENTER YOUR CHOICE: ' )
        choice = int ( choice )
        if choice == 1 :
            play ( )
        elif choice == 2 :
            supername = input ( "Enter your name:" )
            if supername == "AkashAatha" :

                superfunction = 1
                while superfunction != 4 :
                    try :
                        print ( '\n=========WELCOME',supername, '==========' )
                        print ( '-----------------------------------------' )
                        print ( 'Press 1 to add questions:' )
                        print ( 'Press 2 to remove questions:' )
                        print ( 'Press 3 to Exit:' )
                        superfunction = input ( 'ENTER YOUR CHOICE: ' )
                        superfunction = int ( superfunction )
                        if superfunction == 1 :
                            add_que_ans_ops ( )

                            # update_question_option()
                            # level, que_ans, ans_op = add_que_ans_ops()
                            # update_question_option(level, que_ans, ans_op)
                            # print('Question is added. succesfully.')
                            # print(question_ans)
                            # print(options)

                        elif superfunction == 2 :
                            # print ( "Remove questions" )
                            remove()
                        elif superfunction == 3 :
                            break

                        else :
                            print ( "Enter valid input" )
                    except ValueError :
                        print ( "Enter value in numbers" )

            else :
                print ( supername , "you are not authorized to make changes in the question" )

        elif choice == 3 :
            exit ( )

        else :
            print ( 'Please enter the numbers in between 1 to 3' )
    except ValueError :
        print ( "Enter value in numbers" )
