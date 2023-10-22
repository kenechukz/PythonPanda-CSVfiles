# with open('./Day 25/weather_data.csv', 'r+') as data_file:
#    data = data_file.readlines()
#    print(data)

# import csv

# with open('./Day 25/weather_data.csv', 'r+') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []

#    for row in data:
#        temperature = (row[1])
#        if temperature != 'temp':
#            temperatures.append(int(temperature))

#    print(temperatures)

import pandas

data = pandas.read_csv('./Day 25/weather_data.csv')
#print(data['temp'])
data_dict = data.to_dict()
print(data_dict)

#temp_list = data['temp'].to_list()
#print(temp_list)

""" Finding the average of a series/column """

"""Method 1"""
# total = 0

# for temp in temp_list:
#    total += temp

# average = total/len(temp_list)
# print(average)


"""Method 2"""
# average = sum(temp_list)/len(temp_list)
# print(average)


"""Method 3"""
#print(data['temp'].mean())

##print(data['temp'].max())

# Get data in a Column
#print(data['condition'])
#print(data.condition)

# Get data in a Row
# print(data[data.day == 'Monday'])

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == 'Monday']

#print(monday.temp)

#monday_temp = monday.temp

#monday_temp_F = (9/5 * int(monday_temp)) + 32

#print(monday_temp_F)

# Create a dataframe from scratch

# data_dict = {
#    'students':["Amy","James","Angela"],
#    'scores': [76, 56, 45]
#}
#dataframe = pandas.DataFrame(data_dict)

#print(dataframe)

#dataframe.to_csv('new_data.csv')

#data = pandas.read_csv('./Day 25/Central_Park_Squirrel_Census.csv')

#fur_colour = data['Primary Fur Color']

#black_count = 0

#gray_count = 0

#cinnamon_count = 0

#for colour in fur_colour:

    #if colour == 'Black':
        #black_count += 1
    
    #if colour == 'Gray':
        #gray_count += 1

    #if colour == 'Cinnamon':
        #cinnamon_count += 1

#print(black_count,gray_count,cinnamon_count)


#data_dict = {
    #'Fur Colour': ['Grey','Red','Black'],
    #'Count': [gray_count,cinnamon_count,black_count]
#}

#data_new =  pandas.DataFrame(data_dict)

#data_new.to_csv('fur_colour.csv')