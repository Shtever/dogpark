#This program runs in conjustction with dogpark main program.
#This module is used to SEARCH & EDIT only the owner's name
#Copyright Steve McMillen 2023

import os #import needed for the remove & rename functions

def main():
  try:
    found = False                                   #found variable declared
    search = input('please enter dog\'s breed: ')    #search input declared
    owners = open('owners.txt', 'r')            #open owners as read-only
    temp_file = open('temp.txt', 'w')           #open temporary file as write
    record = owners.readline()                #read the line of owners.txt
    while record != '':                 #while not blank statement

      #assign variables (it moves to the next line after every 'readline()'
      dog = owners.readline()         
      breed = owners.readline()
      notes = owners.readline()

      #Strip newline escape scenario from entries
      record = record.rstrip('\n')
      dog = dog.rstrip('\n')
      breed = breed.rstrip('\n')
      notes = notes.rstrip('\n')

      #if 'record' matches search term
      if breed.upper() == search.upper():
        print('match')
        print(f'{breed.upper()} found: {dog}')
        breed = input(f'Please enter dog breed: ')      #input new name

        #write new data to temp_file
        temp_file.write(f'{record}\n')  #name      
        temp_file.write(f'{dog}\n')     #dog name
        temp_file.write(f'{breed}\n')   #breed
        temp_file.write(f'{notes}\n')   #notes
        found = True                    #set 'found' to TRUE- see bottom 'if' stmt.

      #if record does not match search term
      else:
        temp_file.write(f'{record}\n')  #write unchanged data to temp_file
        temp_file.write(f'{dog}\n')
        temp_file.write(f'{breed}\n')
        temp_file.write(f'{notes}\n')
      record = owners.readline()        #move to next entry
      

           #ERROR HANDLERS
  except IOError:         #IOError
        print('Reference does not exist')
  except ValueError:      #ValueError
        print('Please enter a number.')
  except:                 #Other error
        print('An error occured.')

  else:
    owners.close()          #close files
    temp_file.close()
    os.remove('owners.txt') #delete original owners file
    os.rename('temp.txt', 'owners.txt')   #replace with file containing new data

    #short hand for 'if found = True':
    if found:  
      print('The file has been updated')
    else:
        print('That name was not found in the file')

    
