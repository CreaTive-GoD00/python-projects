# import csv
# with open("weather_data.csv", 'r')as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# import pandas
# table = (pandas.read_csv("weather_data.csv"))
# # max_temp = (table['temp'].max())
# # print(max_temp)
# # print(table[table.temp == max_temp])
# monday = table[table.day == "Monday"]
# print((monday['temp'] * 1.8) + 32 )

import pandas

file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Cin = len(file[file["Primary Fur Color"] == "Cinnamon"])
grey = len(file[file["Primary Fur Color"] == "Gray"])
Black = len(file[file["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["grey", "black", "Cinnamon"],
    "Count": [grey, Black, Cin]
 }
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_Count.csv")
print(df)










