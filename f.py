import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv('CarPrice_Assignment - Copy.csv')
dummy=pd.get_dummies(df.CarName)
df1=pd.concat([df,dummy],axis='columns')
df2=df1.drop(['CarName','model','drivewheel','enginelocation','enginetype','fuelsystem','boreratio','stroke','compressionratio'],axis='columns')
#print(df2)
X=df2.drop('price',axis='columns')
y=df2.price
#print(y)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=10)
lr_clf=LinearRegression()
lr_clf.fit(X_train,y_train)
lr_clf.score(X_test,y_test)
def predict_price(CarName,wheelbase,carlength,carwidth,carheight,curbweight,cylindernumber,enginesize,horsepower,peakrpm,citympg):
    loc_index=np.where(X.columns==CarName)[0][0]
    x=np.zeros(len(X.columns))
    x[0]=wheelbase
    x[1]=carlength
    x[2]=carwidth
    x[3]=carheight
    x[4]=curbweight
    x[5]=cylindernumber
    x[6]=enginesize
    x[7]=horsepower
    x[8]=peakrpm
    x[9]=citympg
    
    if loc_index >=0:
        x[loc_index]=1
    return lr_clf.predict([x])[0] 


print(predict_price('audi',105,192,71,56,3086,5,131,140,5500,17))
import pickle
with open('CarPrice_Assignment - Copy.pickle','wb')as f:
      pickle.dump(lr_clf,f)
import json
columns={
    'data_columns':[col.lower() for col in X.columns]
}      
with open("columns.json","w") as f:
    f.write(json.dumps(columns))