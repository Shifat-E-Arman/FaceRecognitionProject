import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.neighbors import KNeighborsClassifier


df = pd.read_csv('final_bright.csv')


Y = df['label']
X = df.drop(['label'],axis=1)

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.3, random_state=42)

param_grid = {'n_neighbors':np.arange(1,20)}
knn=KNeighborsClassifier()

gcv = GridSearchCV(knn, param_grid,cv=5)

gcv.fit(X_train,y_train)

print("Best n= ",gcv.best_params_)
print("Best Score= ",gcv.best_score_)

y_pred = gcv.predict(X_test)

print("Confusion Matrix")
print("----------------")
print(confusion_matrix(y_test,y_pred))