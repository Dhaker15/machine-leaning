

import pandas as pd

df=pd.read_csv("http://13.234.66.67/summer19//datasets/info.csv")

df

X=df.iloc[:,0:].values
X

df.info()

#remove missing value oe replace missing values with some relevent dat
#df.describe()
from sklearn.preprocessing import Imputer

imp=Imputer(missing_values='NaN',axis=0,strategy="mean")

impute=imp.fit(X[:,1:3])    #this is only fitting of columns that we want to process

#time for transforming the fuittig columns
X[:,1:3]=impute.transform(X[:,1:3])

X

# string label int/float
from  sklearn.preprocessing import LabelEncoder

cont=LabelEncoder()

#now apply column first in this LAbelEn
X[:,0]=cont.fit_transform(X[:,0])

X

#labeling last columns
p=LabelEncoder()

X[:,3]=p.fit_transform(X[:,3])

X

# Now encoding first column ----- making subcolumn of first column
  from  sklearn.preprocessing import OneHotEncoder

firstcl=OneHotEncoder(categorical_features=[0])   #defining exact column number where we want to make category

X=firstcl.fit_transform(X).toarray()      #after transform we need to convert into numpy array

X

X.astype(int)

