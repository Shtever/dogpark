#This is a program that reads or adds to a text document with
#owner/dog information. Built for my mom.
#Copyright Steve McMillen 2023

import read, write
import search_owner, search_dog, search_breed, search_notes
import edit_owner, edit_dog, edit_breed, edit_notes

def main():
    try:
        print('Welcome to the dogpark app.')
        print('With this app, you can:')
        print('\t (R)ead all entries')
        print('\t (S)earch entries')
        print('\t (A)dd to the list')
        print('\t (E)dit an entry')
        answer = input('Please make a choice ')
        if  answer.upper() == 'R':
            read.main()
        elif answer.upper() =='A':
            write.main()
            print('Your entry has been made successfully')
            print()
            read.main()
        elif answer.upper() =='S':
            print('Which do you want to search for?')
            print('\t (O)wner name ')
            print('\t (D)og name ')
            print('\t (B)reed ')
            print('\t (N)otes term ')
            term = input('Please select: ')
            if term.upper() == 'O':
                search_owner.main()
            elif term.upper() == 'D':
                search_dog.main()
            elif term.upper() == 'B':
                search_breed.main()
            elif term.upper() == 'N':
                search_notes.main()
            else:
                print('Incorrect entry. Starting over')
                main()
        elif answer.upper() =='E':
            print('Which do you want to edit?')
            print('(O)wner name ')
            print('(D)og name ')
            print('(B)reed ')
            print('(N)otes term ')
            term = input('Please select: ')
            if term.upper() == 'O':
                edit_owner.main()
            elif term.upper() == 'D':
                edit_dog.main()
            elif term.upper() == 'B':
                edit_breed.main()
            elif term.upper() == 'N':
                edit_notes.main()
            else:
                print('Incorrect entry. Starting over')
                main()
        else:
            print('please enter a valid response')
            main()
    
  #ERROR HANDLERS
    except IOError:         #IOError
        print('Reference does not exist')
    except ValueError:      #ValueError
        print('Please enter a number.')
    except:                 #Other error
        print('An error occured.')
    finally:
        print('___________________________________________')
        print()
        main()

main()
