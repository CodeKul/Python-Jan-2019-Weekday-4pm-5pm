
import pandas as pd

# dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
#        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
#        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
#        "population": [200.4, 143.5, 1252, 1357, 52.98] }

# brics = pd.DataFrame(dict)
# print(brics)
# # print(brics.head(3))
# # print(brics.tail(3))
# for item in brics.iterrows():
#     print(item)


# Import the cars.csv data: cars
scorecard = pd.read_csv('Scorecard-Elements.csv')

# Print out cars
print(scorecard.isin([100654,100200,1002,0.2531554273,'NaN',0.2913]))