import datetime, random
from enum import IntEnum


# tuplelist of months in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr','May','Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

def getBirthdays(numOfDays):
    # returns a list of number random objects for birthdays
    birthdays = []

    for  i in range(numOfDays):
        startOfYear = datetime.date(2024, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def matchBirthdays(birthdays):
    """returns the date object that occurs more than once in the birthdays list"""
    if len(birthdays) ==len(set(birthdays)):
        return None # all birthdays are unique

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA



# Display intro
print(''' Birthday Paradox, by Shanil Rajapaksha.

The Birthday Paradox shows us that in a group of N people, the odd
that two of them having matching birthdays is surprisibgly large.

(It's not actually a paradox, it's just a facinating fact!)
''')


while True: 
    print("How many birthdays shall I generate? (Max 100)")
    response = input('>')
    if response.isdecimal() and (0<int(response) <= 100):
        numBDays = int(response)
        break # user has given a valid amount

print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)

for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end = '')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')

print()
print()

# Determine if the are matching birthdays
match = matchBirthdays(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[birthdays.month-1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print('multiple people have abirthday on', dateText)
else:
    print('there are no matching birthday.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations')
simMatch = 0 # How many simulations had matching birthdays in them
for i in range(100_000):
    # Report on the progress every 10,00 simulations:
    if i % 10_000 ==0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if matchBirthdays(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

