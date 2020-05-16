#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[33]:


data=pd.read_csv('student-mat.csv')


# In[35]:


data.drop(['school','address','famsize','Pstatus','Medu','Fedu','reason','famrel','Dalc','Walc','failures','schoolsup','famsup','paid','activities','nursery','higher','romantic'], axis = 1, inplace=True)
data.drop_duplicates()
corr_matrix=data.corr()
#corr_matrix['internet'].sort_values(ascending=False)
#print(data.head())


# In[4]:


from sklearn.preprocessing import OneHotEncoder,LabelEncoder


# In[31]:


enc = LabelEncoder()
category_colums = data.select_dtypes('object').columns
for i in category_colums:
    data[i] = enc.fit_transform(data[i])
print(data['internet'].head())
'''

# In[26]:


X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values


# In[27]:


from sklearn.model_selection import cross_val_score,train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score
from random import randint


# In[28]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[29]:


cross_val_score(RandomForestRegressor(),X,y).mean()


# In[30]:


log = RandomForestRegressor()
log.fit(X_train,y_train)
y_predict = log.predict(X_test)
y_predict=log.predict([[0,18,0,0,0,100,0,0,0,0,0,50,5,5]])
y_predict'''

