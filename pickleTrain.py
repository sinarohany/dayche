# Data Serialization

import pickle
import sys
import shelve

cars = list()

cars.append({"make": "alfa", "colour": "red"})
cars.append({"make": "land rover", "colour": "green"})
cars.append({"make": "aston", "colour": "gold"})

cars[0]["ownercount"] = 2
cars[1]["ownercount"] = 1
cars[2]["ownercount"] = 3

cars[0]["owners"] = ["tom", "james"]
cars[1]["owners"] = ["alison"]
cars[2]["owners"] = ["tom", "james", "jake"]

print(cars)

sampleList = [1, 2, 3]
sampleTuple = 1, 2, 3
names = ['Sina', 'Sogol', 'Sadaf', 'Ali']
with open('cars.pickle', 'bw') as pickleFile:
    pickle.dump(cars, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleList, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleTuple, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)

with open('cars.pickle', 'br') as pickleFile:
    newCars = pickle.load(pickleFile)
    newList = pickle.load(pickleFile)
    newTuple = pickle.load(pickleFile)


# =================================================================
print('=' * 50)

with shelve.open('demo.shelve') as shelveFile:
    shelveFile['cars'] = cars
    shelveFile['sampleList'] = sampleList
    shelveFile['sampleTuple'] = sampleTuple
    shelveFile['names'] = names
    # del shelveFile['name']

    print('=' * 50)
    for item in shelveFile:
        print(item, '\t', shelveFile[item])

# =================================================================
print('=' * 50)

names = ['Sina', 'Sogol', 'Sadaf', 'Ali']
age = [31, 30, 24, 18]
cities = ['Mashhad', 'Astara', 'Astara', 'Tehran']

# with shelve.open('shelveSpecs.shelve', writeback=True) as s_file:
with shelve.open('shelveSpecs.shelve') as s_file:
    s_file['names'] = names
    s_file['age'] = age
    s_file['cities'] = cities

    # s_file['names'].append('Naser')
    s_file['age'].append(21)
    tempList = names
    tempList.append('Naser')
    s_file['names'] = tempList

    for item in s_file:
        print(item, '\t', s_file[item])


