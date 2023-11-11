#This program writes owner/dog info into a text file.

def main():
  try:
    num_owners = int(input('How many records do you want to add? '))
    owners = open('owners.txt', 'a')
    for num in range(num_owners):
        owner = input(f'Owner #{num+1}\'s name: ')
        line1 = owners.write(owner + '\n')
        dog = input(f'Dog #{num+1}\'s name: ')
        line1 = owners.write(dog + '\n')
        breed = input(f'Dog #{num+1}\'s breed: ')
        line1 = owners.write(breed + '\n')
        notes = input(f'#{num+1} additional notes: ')
        line1 = owners.write(notes + '\n')

  except IOError:         #IOError
        print('An error occured trying to read the file.')
  except ValueError:      #ValueError
        print('Please enter a number.')
  except:                 #Other error
        print('An error occured.')
  else:
    owners.close()
