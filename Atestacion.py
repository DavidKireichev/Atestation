import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# one_hot_encoded = pd.get_dummies(data, columns=['whoAmI'])
# print(one_hot_encoded.head())

data = pd.DataFrame(random.sample(['robot', 'human']*10, 10) ,columns={'WhoAmI'})  
data.head() 

# data['tmp'] = 1
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value = 0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None
# print(data)