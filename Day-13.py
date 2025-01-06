#Split:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

#If the array has less elements than required, it will adjust from the end accordingly.
#SPLIT 1-D ARRAY INTO 4 PARTS
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)

#SPLIT 1-D ARRAY INTO 3 PARTS
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

#SPLIT 2-D ARRAY INTO 3 PARTS
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

#An alternate solution is using hsplit() opposite of hstack()
#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

#Search:
#Find the indexes where the value is 4:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#Find the indexes where the values are even:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#Find the indexes where the values are odd:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
odd_indexes = np.where(arr % 2 != 0)
print("Indexes where the values are odd:", odd_indexes[0])

#Sorted Search
#find the indexes where the value 7 should be inserted:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

#By default the left most index is returned, but we can give side='right'to return the right most index instead.
#Find the indexes where the value 7 should be inserted, starting from the right:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

#To search for more than one value, use an array with the specified values.
#Find the indexes where the values 2, 4, and 6 should be inserted:
#SEARCHING MULTIPLE VALUES IN NUMPY ARRAY
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)

#SORTING A NUMERIC NUMPY ARRAY
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#SORTING A STRING NUMPY ARRAY
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

#If you use the sort() method on a 2-D array, both arrays will be sorted:
#Sort a 2-D array:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
print(newarr)

#GENERATING RANDOM INTEGER USING NUMPY
from numpy import random
x = random.randint(100)
print(x)

#GENERATING RANDOM FLOAT USING NUMPY
from numpy import random
x = random.rand()
print(x)

#ARRAY:
from numpy import random
x=random.randint(100, size=(5))
print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)

#GENERATING 1-D ARRAY WITH RANDOM FLOATS
from numpy import random
x = random.rand(5)
print(x)

#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
from numpy import random
x = random.rand(3, 5)
print(x)

#CHOICE
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)

#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
 
####Pandas
#CREATING A PANDAS SERIES
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#CREATING A PANDAS SERIES WITH CUSTOM INDEX
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print(myvar["y"])  #Return the value of "y"

#CREATING A PANDAS SERIES FROM A DICTIONARY
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#To select only some of the items in the dictionary, 
#use the index argument and specify only the items you want to include in the Series.
#Create a Series using only data from "day1" and "day2"
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#Dataframes:
import pandas as pd  # Importing pandas library
data = {  # Defining the data dictionary
  "calories": [420, 380, 390],  # Calories data
  "duration": [50, 40, 45]  # Duration data
}
# Load data into a DataFrame object:
df = pd.DataFrame(data) 
print(df)  # Print the DataFrame
# Refer to the row index:
print(df.loc[0])  
# Return row 0 and 1:
# Use a list of indexes:
print(df.loc[[0, 1]])  

#ADDING A LIST OF NAMES AS ROW INDEXES IN A DATAFRAME
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 
print(df.loc["day2"]) #Return "day2" refer to the named index

#CSV
import pandas as pd
df = pd.read_csv('C:\\Users\\My Pc\\OneDrive\\Desktop\\Pictures\\Documents\\data.csv')
print(df.to_string()) 

#PRINTING A DATAFRAME WITHOUT TO_STRING METHOD
import pandas as pd
df = pd.read_csv('C:\\Users\\My Pc\\OneDrive\\Desktop\\Pictures\\Documents\\data.csv')
print(df) 

#CHECKING THE MAXIMUM ROW DISPLAY OPTION IN PANDAS
import pandas as pd
print(pd.options.display.max_rows) 

#READING AND PRINTING JSON FILE USING PANDAS
import pandas as pd
df = pd.read_json('C:\\Users\\My Pc\\OneDrive\\Desktop\\Pictures\\Documents\\data.json')
print(df.to_string()) 

#CREATING A DATAFRAME FROM DICTIONARY AND PRINTING USING PANDAS
import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df) 

#PLOTTING DATA FROM CSV USING PANDAS AND MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\My Pc\\OneDrive\\Desktop\\Pictures\\Documents\\data.csv')
print("Data preview:")
print(df.head())
print("\nData types:")
print(df.dtypes)
df = df.dropna()  
df.plot()
plt.title('Data Plot')
plt.show()

#PLOTTING SCATTER PLOT FROM CSV USING PANDAS AND MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\My Pc\\OneDrive\\Desktop\\Pictures\\Documents\\data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()





