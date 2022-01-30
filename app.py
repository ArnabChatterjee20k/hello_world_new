from flask import Flask, render_template, request
import pickle
import numpy as np


crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))


app = Flask(__name__)


@ app.route('/')
def home():
    title = 'Home Page'
    return render_template('index.html', title=title)

@ app.route('/crop-recommend',methods=['POST','GET'])
def crop_recommend():
    title = 'Crop Recommendation'
    return render_template('crop.html', title=title)


@ app.route('/crop-predict', methods=['POST','GET'])
def crop_prediction():
    title = 'Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        T = float(request.form['temprature'])
        H = float(request.form['humidity'])
        rainfall = float(request.form['raainfall'])

        data = np.array([[N, P, K, T, H, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        
        final_prediction = "Banana"
        return render_template('crop-result.html', prediction=final_prediction, title=title)

    else:
        return render_template('try_again.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
