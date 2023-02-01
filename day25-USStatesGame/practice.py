import pandas as pd

# import csv
#
# with open("weather_data.csv", mode="r") as f:
#     temperatures = []
#     data_stock = csv.reader(f)
#     for row in data_stock:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


# data_stock = pd.read_csv("weather_data.csv")
# data_dict = data_stock.to_dict()
# data_list = data_stock["temp"].to_list()

# print(data_stock[data_stock["condition"] == "Sunny"])
# print(data_stock[data_stock["temp"] == data_stock["temp"].max()])
# print(data_stock[data_stock["day"] == "Monday"]["temp"]*1.8+32)
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

df = pd.DataFrame({
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Squirrel Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
})
df.to_csv("squirrel_count.csv")
