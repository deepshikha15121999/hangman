import random
def hangman():
    guessing_name=['deep','shikha','sania','rafat','parween','anju']
    random_name=random.choice(guessing_name)
    chance=10
    new_guess=''
    letters=set('abcdefghijklmnopqrstuvwxyz')
    while len(random_name)>0:
        correct_word=''
        for letter in random_name:
            if letter in new_guess:
                correct_word=correct_word+letter
            else:
                correct_word= correct_word+"_"
        if correct_word==random_name:
            print(correct_word)
            print('yupee! you are the winner....')
            break
        print('choose correct word ',correct_word)
        guess=input()
        if guess in letters:
            new_guess=new_guess+guess
        else:
            print('enter right charachter----')
            guess=input('enter single letter  ')
        if guess not in random_name:
            chance=chance-1
            if chance==9:
                print("9 chance left")
                print("try again ")
                print("    O        ")
            if chance==8:
                print("8 chance left")
                print("try again ")
                print("    O       ")
                print("    |       ")
            if chance==7:
                print("7 chance left")
                print("try again ")
                print("     O       ")
                print("    \|/      ")
            if chance==6:
                print("6 chance left")
                print("try again ")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
            if chance==5:
                print("5 chance left")
                print("try again ")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
                print("    / \      ")
            if chance==4:
                print("4 chance left")
                print("try again ")
                print("     |       ")
                print("     O       ")
                print("    \|/      ")
                print("     |       ")
                print("    / \      ")
            if chance==3:
                print("3 chance left"    )
                print("try again        ")
                print("     __          ")
                print("          |       ")
                print("          O       ")
                print("         \|/      ")
                print("          |       ")
                print("         / \      ")
            if chance==2:
                print("2 chance left")
                print("try again     ")
                print("   ______    ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |     \|/   ")
                print("  |      |    ")
                print("  |     / \   ")
                print("  |           ")
            if chance==1:
                print("you have only 1 chance ")
                print("try again    ")
                print("   _______    ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |     \|/   ")
                print("  |      |    ")
                print("  |     / \   ")
                print("  |           ")
                print(" -------------------")
            if chance==0:
                print("....oppppsssssss...")
                print(" << you loose >>")
                print("your word is",random_name)
                print("   _______    ")
                print("  |      |    ")
                print("  |      o    ")
                print("  |      |   ")
                print("  |     /|\    ")
                print("  |     / \   ")
                print("  |           ")
                print(" -------------------")
                break
name=input('enter your name:-')
print('welcome to the this game ',name)
print('guess the word ')
hangman()