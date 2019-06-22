

from sklearn.datasets import load_breast_cancer

cancer=load_breast_cancer()
dir(cancer)

cancer.DESCR

cancer.data

cancer.filename

cancer.target

cancer.feature_names

cancer.target_names

feature=cancer.data
feature.shape
label=cancer.target

from sklearn.model_selection import train_test_split

train_data,test_data,label_train,label_test=train_test_split(feature,label,test_size=0.1)

from sklearn.tree import DecisionTreeClassifier

clf=DecisionTreeClassifier()

trained=clf.fit(train_data,label_train)

predicted_cancers=trained.predict(test_data)

predicted_cancers

from sklearn.metrics import accuracy_score

label_test

accuracy_score(label_test,predicted_cancers)

