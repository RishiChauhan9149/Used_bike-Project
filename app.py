from flask import Flask, render_template,url_for, request
import joblib
model=joblib.load(r'C:\Users\hii\OneDrive\Desktop\Python\Project\Used_bike\model.joblib')
app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])

def predict():
    if request.method=='POST':
        brand_name = request.form['brand_name']
        owner= request.form['owner']
        kms_driven= request.form['kms_driven']
        age=request.form['age']
        power=request.form['power']

if __name__=='__main__':  
    app.run(debug=True)      


