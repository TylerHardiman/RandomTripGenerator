y = True
n = False

destinations = ['Paris', 'Bora Bora', 'Maui', 'Rome', 'Phuket']

resturants = ['Burger King', 'Chilis', 'Millers Ale House', 'Pizza', 'Soup and Stuff']

modes_of_transportation = ['Taxi', 'Train', 'Bus', 'Bike', 'Plane',]

entertainment = ['Plays', 'Museum', 'Cruise', 'City Tour', 'Bar Hopping']

print('Welcome to the Random Day Trip Generator')
your_name = input('Please enter your name. ')
print('Welcome to the Random Day Trip Generator: ' +your_name)
input('Press enter to continue')
print('Destination: ')
destinations = ['Paris', 'Bora Bora', 'Maui', 'Rome', 'Phuket']
import random
print(random.choice(destinations))

while destinations == True:
            destinations = input('Press Y accept or type N to reselect')
            if n:
                import random
            destinations = ['Paris', 'Bora Bora', 'Maui', 'Rome', 'Phuket']
            print(random.choice(destinations))
            break
        
            
print('Resturant: ')
resturants = ['Burger King', 'Chilis', 'Millers Ale House', 'Pizza', 'Soup and Stuff']
import random
print(random.choice(resturants))

while resturants == True:

        resturants = input('Press Y accept or type N to reselect')
        if n:
            import random
        resturants = ['Burger King', 'Chilis', 'Millers Ale House', 'Pizza', 'Soup and Stuff']
        print(random.choice(destinations))
        break

print('Transportation: ')
modes_of_transportation = ['Taxi', 'Train', 'Bus', 'Bike', 'Plane',]
import random
print(random.choice(modes_of_transportation))

while modes_of_transportation == True:
        
        modes_of_transportation = input('Press Y accept or type N to reselect')
        if n:
            import random
        modes_of_transportation = ['Taxi', 'Train', 'Bus', 'Bike', 'Plane',]
        print(random.choice(modes_of_transportation))
        break

print('Entertainment: ')
entertainment = ['Plays', 'Museum', 'Cruise', 'City Tour', 'Bar Hopping']
import random
print(random.choice(entertainment))

while entertainment == True:
        entertainment = input('Press Y accept or type N to reselect')
        break
if n:
            import random
entertainment = ['Plays', 'Museum', 'Cruise', 'City Tour', 'Bar Hopping']
print(random.choice(entertainment))

print('Here is your completed trip summary for: ' + your_name)

def day_trip_summary():
    input(summary)
    return summary

while day_trip_summary == True:
    summary = destinations + resturants + modes_of_transportation + entertainment
    print(f'Here is your completed trip for: ' + your_name)
    print(summary)
            
            



