from flask import Flask, render_template, request ,redirect, url_for
import pickle
import numpy as np


crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))


app = Flask(__name__)


@ app.route('/')
def home():
    title = 'Home Page'
    return render_template('index.html', title=title)


# here the form is present.
@ app.route('/crop-recommend',methods=['POST','GET'])
def crop_recommend():
    title = 'Crop Recommendation'
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potasium'])
        ph = float(request.form['ph'])
        T = float(request.form['temprature'])
        H = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])

        data = np.array([[N, P, K, T, H, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        
        final_prediction = "Banana"
        final_prediction = "Done"
        return redirect(url_for("crop_prediction",prediction=final_prediction)) # redirecting the url of crop-predict using the function

    # if request is not post then this template will be sent.
    return render_template('crop.html', title=title)


@ app.route('/crop-predict', methods=['GET'])
def crop_prediction():
    title = 'Crop Recommendation'
    return render_template('crop-result.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
