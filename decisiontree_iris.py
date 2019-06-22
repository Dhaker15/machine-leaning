

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris=load_iris()
dir(iris)

#iris.DESCR
iris.feature_names #features name

iris.target_names #labels or answer

features=iris.data #actual data with attributes
features
#features.shape

type(features)

#now time for label data  that will be exactly same as no. of features
  label=iris.target
  label.shape

SL=features[0:,0]
SW=features[0:,1]

plt.xlabel("Length")
plt.ylabel("Width")
plt.scatter(SL,SW,label="sepal_data",marker='*')
plt.scatter(features[0:,2],features[0:,3],label="petal_data",marker='+')

#now time for separating data into two category
#1. training dta
#2. testing data .... questions
from sklearn.model_selection import train_test_split
train_data,test_data,label_train,label_test=train_test_split(features,label,test_size=0.1)

clf=DecisionTreeClassifier() #calling

trained=clf.fit(train_data,label_train)

#now predicting flowers
predicted_flowers=trained.predict(test_data)

predicted_flowers #algo answer

label_test #actual  answer

accuracy_score(label_test,predicted_flowers)

