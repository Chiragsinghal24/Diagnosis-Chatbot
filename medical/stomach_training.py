import pickle
import pandas as pd
from sklearn import tree 
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import train_test_split

lung=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Stomach Disease.csv")
X=lung[['scaled_sex','scaled_symptoms','scaled_history']]
y=lung['scaled_severity']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
classifier=tree.DecisionTreeClassifier()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
acc=accuracy_score(y_test,y_pred)
print(classifier)
print("Accuracy is: ",acc)

with open('lung_model.pkl',"wb") as f:
    pickle.dump(classifier,f)

print("Dumped the model")
