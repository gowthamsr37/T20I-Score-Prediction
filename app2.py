# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
            Bat_Team = request.form['Bat_Team']
            if Bat_Team == 'AUS':
                temp_array = temp_array + [1,0,0,0,0,0,0,0,0]
            elif Bat_Team == 'BAN':
                temp_array = temp_array + [0,1,0,0,0,0,0,0,0]
            elif Bat_Team == 'ENG':
                temp_array = temp_array + [0,0,1,0,0,0,0,0,0]
            elif Bat_Team == 'IND':
                temp_array = temp_array + [0,0,0,1,0,0,0,0,0]
            elif Bat_Team == 'NZ':
                temp_array = temp_array + [0,0,0,0,1,0,0,0,0]
            elif Bat_Team == 'PAK':
                temp_array = temp_array + [0,0,0,0,0,1,0,0,0]
            elif Bat_Team == 'SA':
                temp_array = temp_array + [0,0,0,0,0,0,1,0,0]
            elif Bat_Team == 'SL':
                temp_array = temp_array + [0,0,0,0,0,0,0,1,0]
            elif Bat_Team == 'WI':
                temp_array = temp_array + [0,0,0,0,0,0,0,0,1]
            
            
            Bowl_Team = request.form['Bowl_Team']
            if Bowl_Team == 'AUS':
                    temp_array = temp_array + [1,0,0,0,0,0,0,0,0]
            elif Bowl_Team == 'BAN':
                    temp_array = temp_array + [0,1,0,0,0,0,0,0,0]
            elif Bowl_Team == 'ENG':
                    temp_array = temp_array + [0,0,1,0,0,0,0,0,0]
            elif Bowl_Team == 'IND':
                    temp_array = temp_array + [0,0,0,1,0,0,0,0,0]
            elif Bowl_Team == 'NZ':
                    temp_array = temp_array + [0,0,0,0,1,0,0,0,0]
            elif Bowl_Team == 'PAK':
                    temp_array = temp_array + [0,0,0,0,0,1,0,0,0]
            elif Bowl_Team == 'SA':
                    temp_array = temp_array + [0,0,0,0,0,0,1,0,0]
            elif Bowl_Team == 'SL':
                    temp_array = temp_array + [0,0,0,0,0,0,0,1,0]
            elif Bowl_Team == 'WI':
                    temp_array = temp_array + [0,0,0,0,0,0,0,0,1]
            
            
            overs = float(request.form['overs'])
            total_score = int(request.form['total_score'])
            total_wickets = int(request.form['total_wickets'])
            prev_runs_30 = int(request.form['prev_runs_30'])
            prev_wickets_30 = int(request.form['prev_wickets_30'])
            prev_30_dot_balls = int(request.form['prev_30_dot_balls'])
            prev_30_boundaries = int(request.form['prev_30_boundaries'])
            
            temp_array = temp_array + [overs,total_score,total_wickets,prev_runs_30,prev_wickets_30,prev_30_dot_balls,prev_30_boundaries]
            
            data = np.array([temp_array])
            my_prediction = int(regressor.predict(data)[0])
              
            return render_template('predict.html', lower_limit = my_prediction-1, upper_limit = my_prediction+1)



if __name__ == '__main__':
    app.run()