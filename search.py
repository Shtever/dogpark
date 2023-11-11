def main():
  try:
    owners = open('owners.txt', 'r')      #open file as read-only
    record = owners.readline()
    record = record.rstrip('\n')
    print(record)
    record_input = input('please enter owner\'s name: ')
    if record.upper() != record_input.upper():
      print('no match')
      for x in range(3):
        x = owners.readline()
    elif record.upper() == record_input.upper():
      print('Match')
      #assign variables (it moves to the next line after every 'readline')
      dog = owners.readline()
      breed = owners.readline()
      notes = owners.readline()
      #Strip newline escape scenario from entries
      record = record.rstrip('\n')
      dog = dog.rstrip('\n')
      breed = breed.rstrip('\n')
      notes = notes.rstrip('\n')
      #print each line of data with the specified seperator
      print(record,dog,breed,notes, sep='  -  ')
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

main()
