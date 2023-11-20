#This is a program that reads or adds to a text document with
#owner/dog information. Built for my mom.
#Copyright Steve McMillen 2023

import read, write
import search_owner, search_dog, search_breed, search_notes
import edit_owner, edit_dog, edit_breed, edit_notes

def main():
    try:
        answer = input('Do you want to (r)ead, (s)earch or (a)dd to list? ')
        if  answer.upper() == 'R':
            read.main()
        elif answer.upper() =='A':
            write.main()
            print('Your entry has been made successfully')
            print()
            read.main()
        elif answer.upper() =='S':
            print('Which do you want to search for?')
            term = input('(o)wner, (d)og name, (b)reed, or (n)otes? ')
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
        else:
            print('please enter either \'r\', \'s\' or \'a\'')
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
