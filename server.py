from flask import Flask, request, jsonify
import util
app=Flask(__name__)
@app.route('/get_brand_names',methods=['GET'])
def get_brand_names():
    response=jsonify({
        'CarName':util.get_brand_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route("/estimate_price",methods=['POST','GET'])    
def estimate_price():
    wheelbase=float(request.form['wheelbase'])
    carlength=float(request.form['carlength'])
    CarName=request.form['CarName']
    carwidth=float(request.form['carwidth'])
    carheight=float(request.form['carheight'])
    curbweight=float(request.form['curbweight'])
    cylindernumber=float(request.form['cylindernumber'])
    enginesize=float(request.form['enginesize'])
    horsepower=float(request.form['horsepower'])
    peakrpm=float(request.form['peakrpm'])
    citympg=float(request.form['citympg'])
    response=jsonify({
        'estimated_price':util.get_predicted_price(CarName,wheelbase,carlength,carwidth,carheight,curbweight,cylindernumber,enginesize,horsepower,peakrpm,citympg)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__ =="__main__" :
    util.load_saved_artifacts()  
    app.run()