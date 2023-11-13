#This program runs in conjustction with dogpark main program.
#This module is used to search for dog's breed
#Copyright Steve McMillen 2023

def main():
  try:
    found = False
    search = input('please enter dog\'s breed: ')
    owners = open('owners.txt', 'r')
    record = owners.readline()
    while record != '':
      dog = owners.readline()
      breed = owners.readline()
      notes = owners.readline()
      #Strip newline escape scenario from entries
      record = record.rstrip('\n')
      dog = dog.rstrip('\n')
      breed = breed.rstrip('\n')
      notes = notes.rstrip('\n')
      if breed.upper() == search.upper():
        print('match')
        print(record,dog,breed,notes, sep='  -  ')
        found = True
      record = owners.readline()

           #ERROR HANDLERS
  except IOError:         #IOError
        print('Reference does not exist')
  except ValueError:      #ValueError
        print('Please enter a number.')
  except:                 #Other error
        print('An error occured.')
  else:
    owners.close()      #close file
