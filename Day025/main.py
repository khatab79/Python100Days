# import pandas
#
# data = pandas.read_csv("./Day025/usa_game/weather_data.csv")
#
# #
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = dat["temp"].to_list()
# print(len(temp_list))

# print(max(data["temp"]))

# #Get data in columns
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("./Day025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cinnamon = len( data[data["Primary Fur Color"] == "Cinnamon"])
black =  len(data[data["Primary Fur Color"] == "Black"])
grey =  len(data[data["Primary Fur Color"] == "Gray"])

# squirel_count = [ 
#     { "Fur Color":"gray",
#         "Count":    grey 
#     },
#     {  "Fur Color":"red",
#         "Count":    cinnamon
#     },
#     { "Fur Color":"black",
#         "Count":    black 
#     },
# ]

squirel_count = {
    "Fur Color" : ["gray", "red", "black"],
    "Count" : [grey, cinnamon, black]
}

pandas.DataFrame(squirel_count).to_csv("squirel_count.csv")
