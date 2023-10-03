# flask , pandas , scikit-learn , pickle-mixin

from flask import Flask,render_template,request

import pandas as pd
import pickle
model=pickle.load(open('lrmodel.pkl','rb'))

app=Flask(__name__)
car=pd.read_csv("cleaned_data.csv")


@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique(),reverse=True)
    years=sorted(car['year'].unique())
    fuel_type=car['fuel_type'].unique()
    return render_template("index.html",companies=companies,car_models=car_models,years=years,fuel_types=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    print(request.form)
    company=request.form.get('company')
    car_model=request.form.get('car_model')
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    print(company,car_model,year,fuel_type,kms_driven)
    prediction=model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))

    print(prediction)

    return str(prediction[0])



if __name__=='__main__':
    app.run(debug=True)
