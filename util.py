import json
import pickle
import numpy as np
__brand = None
__model = None
__data_columns = None
def get_predicted_price(CarName,wheelbase,carlength,carwidth,carheight,curbweight,cylindernumber,enginesize,horsepower,peakrpm,citympg):
    try:
        loc_index = __data_columns.index(CarName.lower())
    except:
        loc_index=-1    
    x=np.zeros(len(__data_columns))
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
    price = float(round(__model.predict([x])[0],0))/10   
    return price
def get_brand_names():
    return __brand
def load_saved_artifacts():
    global __data_columns
    global __brand

    with open("columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']
        __brand=__data_columns[12:]
    global __model    
    with open("CarPrice_Assignment - Copy.pickle","rb") as f:
        __model=pickle.load(f)

if __name__ == "__main__"    :
    load_saved_artifacts()
    print(get_brand_names())  
    print(get_predicted_price('audi',105,192,71,56,3086,5,131,140,5500,17)) 