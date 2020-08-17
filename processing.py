import pandas as pd
import os

path = "./sheets"

meals_db = pd.read_csv("./sheets/Meal Prep - Meals.csv", header = 0)
meals_dict = meals_db.set_index('Name').T.to_dict('list')

day = 0
kcal = 0
carbs = 0
protein = 0
fat = 0
total = 0

days = []
headers = ['kcal', 'carbs', 'protein', 'fat']
macros = []

for sheet in os.listdir(path): #counts macros and adds them to a new sheet
    if sheet != "Meal Prep - Meals.csv" and sheet != "WeeklyMacros.csv":
        menu = pd.read_csv(os.path.join(path, sheet), header = 0)
        day += 1
        days.append("Day %d"%day)
        kcal = 0
        carbs = 0
        protein = 0
        fat = 0
        total = 0

        for index, row in menu.iterrows():
            name = row['Name']
            servings = row['Servings']

            kcal += meals_dict[name][0] * servings
            carbs += meals_dict[name][1] * servings
            protein += meals_dict[name][2] * servings
            fat += meals_dict[name][3] * servings
            total = carbs + protein + fat

            carbs = carbs/total * 100
            protein = protein/total * 100
            fat = fat/total * 100
        
        macros.append([kcal, carbs, protein, fat])

macros_df = pd.DataFrame(macros, index = days, columns = headers)
macros_df.to_csv(os.path.join(path, 'WeeklyMacros.csv'))
