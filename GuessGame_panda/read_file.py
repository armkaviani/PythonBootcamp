
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data["Primary Fur Color"] == "Gray"
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

SQIRREL_COUNT = {"For Color":["Gray", "Cinnamon", "Black"], "Count":[gray_squirrels_count, red_squirrels_count,black_squirrels_count]}

df_squirrel = pd.DataFrame(SQIRREL_COUNT)
df_squirrel.to_csv("squirrel.count.csv")

        





 
            