from flask import Flask, request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('heart.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():

    a = request.form['AVGHEARTBEATSPERMIN']
    b = request.form['PALPITATIONSPERDAY']
    c = request.form['CHOLESTEROL']
    d = request.form['BMI']
    e = request.form['AGE']
    f = request.form['FAMILYHISTORY']
    g = request.form['SMOKERLAST5YRS']
    h = request.form['EXERCISEMINPERWEEK']

    total = [[a,b,c,d,e,f,g,h]]
    print(total)
    #print(total_1)
    prediction = model.predict(total)
    if prediction==0:
        prediction="Safe from heart Faliure"
    else:
        prediction="Having Heart Faliure"
    #print(prediction)
    #output=prediction[0][0]
    
    return render_template('index.html', prediction_text='Your are  {}'.format(prediction))

if __name__ == "__main__":
    app.run()
