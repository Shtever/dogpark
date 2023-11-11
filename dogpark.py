#This is a program that reads or adds to a text document with
#owner/dog information. Built for my mom.
#Copyright Steve McMillen 2023

import read, write

def main():
    try:
        answer = input('Do you want to (r)ead or (a)dd to list? ')
        if  answer == 'r':
            read.main()
        elif answer =='a':
            write.main()
            print('Your entry has been made successfully')
            print()
            read.main()
        else:
            print('please enter either \'r\' or \'a\'')
            main()
    
  #ERROR HANDLERS
    except IOError:         #IOError
        print('Reference does not exist')
    except ValueError:      #ValueError
        print('Please enter a number.')
    except:                 #Other error
        print('An error occured.')

main()
