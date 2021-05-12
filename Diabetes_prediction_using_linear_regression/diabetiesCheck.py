from sklearn import linear_model
import numpy as np
import pandas as pd
import math as m
df=pd.read_csv('diabetes.csv')
import math
pregnancies=int(input("Enter Pregnancy value: "))
Glucose=int(input("Enter Glucose value: "))
BloodPressure=int(input("Enter Blood Pressure: "))
Skinthickness=int(input("Enter Skin thickness: "))
Insulin=int(input("Enter Insulin: "))
BMI=float(input("Enter BMI: "))
DPF=float(input("Enter DiabetiesPedigree function: "))
Age=int(input("Enter age: "))
x_new =np.array([[pregnancies,Glucose,BloodPressure,Skinthickness,Insulin,BMI,DPF,Age]])
reg = linear_model.LinearRegression()
reg.fit(df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']],df.Outcome)
a=reg.predict(x_new)
if a < 0.5 and a >= 0:
    print("Outcome: ",m.floor(a))
    print("Result: Not diabetic")
elif a > 0.5 and a <= 1:
    print("Outcome: ",m.ceil(a))
    print("Result: Diabetic")
else:
    print("Invalid data entered")