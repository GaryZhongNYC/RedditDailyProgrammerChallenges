''' Reddit Dailyprogrammer Challenge #1 [Easy]:
create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
for extra credit, have the program log this information in a file to be accessed later.

Author notes: Program writes to file and appends it to new line. In addition to requirements, added program loop for restarting, case insensitive. 

'''

def challenge1():
    name = input('\nWhat is your name? ')
    age = input('What is your age? ')
    username = input('What is your reddit username? ')
    print('\nYour name is ',name, ', you are ' ,age,' years old and your username is ',username,'\n', sep='')
    file = open('Challenge_1_output.log', 'a')
    file.write('Your name is ' + str(name) + ', you are ' + str(age) + ' years old and your username is ' + str(username) + '\n')
    file.close()
    return restart()

def restart():
        while True:
            restart = input('Would you like to enter new inputs? (Y/N): ')
            if restart not in {'y','Y','n','N'}:
                print('Please enter valid input (Y/N):')
            elif restart.lower() == 'n':
                break
            elif restart.lower() == 'y':
                return challenge1()

challenge1()
                  

