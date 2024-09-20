from flask import Flask, render_template, request, redirect, url_for, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pickle


import sklearn
import numpy
import flask

print("scikit-learn version:", sklearn.__version__)
print("numpy version:", numpy.__version__)
print("Flask version:", flask.__version__)


## creating  a simple flask application

app = Flask(__name__)   #entry point of the program, app is variable for our flast based app
app = Flask(__name__, static_folder='static')

# loading pickle file

import pickle

#using unpickler to ignore unknown class
# class IgnoreUnpickler(pickle.Unpickler):
#     def find_class(self, module, name):
#         if module == "flood_predictor":
#             return object
#         return super().find_class(module, name)
# with open('model/flood.pkl', 'rb') as f:
#     flood_model = IgnoreUnpickler(f).load()

storm_model = pickle.load(open('model/storm.pkl', 'rb'))
earthquake_model = pickle.load(open('model/earthquake.pkl', 'rb'))
flood_model = pickle.load(open('model/flood.pkl', 'rb'))
drought_model = pickle.load(open('model/drought.pkl', 'rb'))

#connecting html pages
@app.route("/", methods=["GET"])
def home():   #this function will tell what will be executed with home page
    return render_template('index.html')

#earthquake web page
@app.route("/earthquake", methods=["GET", "POST"])
def earthquake_disaster():
    if request.method == 'POST':
        try:
            lati = request.form.get('latitude')
            longi = request.form.get('longitude')
            dep = request.form.get('depth')
            stations = request.form.get('no-of-stations')

            # values printing
            print(f"Received data - Latitude: {lati}, Longitude: {longi}, Depth:{dep}, Stations: {stations}")

            #float conversion
            lati = float(lati) if lati else None
            longi = float(longi) if longi else None
            dep = float(dep) if dep else None
            stations = float(stations) if stations else None

            #checking missing fields
            if None in [lati, longi, dep, stations]:
                raise ValueError("All input fields are required.")

            # Prediction input
            input_features = np.array([[lati, longi, dep, stations]])
            prediction = earthquake_model.predict(input_features)

            # Determining the severity level
            if prediction < 4.0:
                severity = ("mild. \n"
                            "You're safe!")
            elif 4.0 <= prediction <= 6.0:
                severity = ("moderate. \n"
                            "Keep a check!")
            else:
                severity = ("severe. \n"
                            "Be precautious!")

            # Printing prediction in console
            print(f"Earthquake Prediction: {prediction[0]}")

            return render_template('earthquake.html', prediction=prediction[0], severity=severity)
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return render_template('earthquake.html', error=f"Invalid input: {ve}")
        except Exception as e:
            print(f"Error in earthquake prediction: {e}")
            return render_template('earthquake.html', error="Error processing form input.")
    return render_template('earthquake.html')


#flood web page
@app.route("/rainfall", methods=["GET", "POST"])
def flood_disaster():
    if request.method == 'POST':
        try:
            am1 = float(request.form.get('a1'))
            # am2 = float(request.form.get('a2'))
            # am3 = float(request.form.get('a3'))
            # am4 = float(request.form.get('a4'))
            # am5 = float(request.form.get('a5'))

            # values printing
            print(f"Received data - Amount: {am1}")

            # # float conversion
            # rainfall = float(rainfall) if rainfall else None

            # checking missing fields
            if not all([am1]):
                raise ValueError("All fields are required.")

            # Prediction input
            input_features = np.array([[am1]])
            prediction = flood_model.predict(input_features)

            if prediction == 1:
                severity  = "There is a chance of flood. Be precautious!"
            else:
                severity = "There is no chance of flood. You're safe!"

            # Return the result to the HTML template

            # Printing prediction in console
            print(f"Flood Prediction: {prediction[0]}")

            return render_template('rainfall.html', prediction=prediction[0], severity=severity)

        except ValueError as ve:
            print(f"ValueError: {ve}")
            return render_template('rainfall.html', error=f"Invalid input: {ve}")
        except Exception as e:
            print(f"Error in flood prediction: {e}")
            return render_template('rainfall.html', error="Error processing form input.")


    return render_template('rainfall.html')


#cyclone web page
@app.route("/storm", methods=["GET", "POST"])
def cyclone_disaster():
    if request.method == 'POST':
        try:
            wind_speed = request.form.get('wind-speed-eastward')
            pressure = request.form.get('sealevel-pressure')
            dist_wh = request.form.get('distance-weight')
            wind_speed_north = request.form.get('wind-speed-northward')

            # values printing
            print(
                f"Received data - Wind Speed: {wind_speed}, Pressure: {pressure}, Distance: {dist_wh}, Wind Speed Northward: {wind_speed_north}")

            # float conversion
            wind_speed = float(wind_speed) if wind_speed else None
            pressure = float(pressure) if pressure else None
            dist_wh = float(dist_wh) if dist_wh else None
            wind_speed_north = float(wind_speed_north) if wind_speed_north else None

            # checking missing fields
            if None in [wind_speed, pressure, dist_wh, wind_speed_north]:
                raise ValueError("All input fields are required.")

            # Prediction input
            input_features = np.array([[wind_speed, pressure, dist_wh, wind_speed_north]])
            prediction = storm_model.predict(input_features)

            # Determining the cyclone severity level based on prediction
            if prediction < 74:
                severity = "below cyclone level. You're completely safe!"
            elif 74 <= prediction <= 95:
                severity = "mild. You're safe!"
            elif 96 <= prediction <= 129:
                severity = "moderate. Keep a check!"
            else:
                severity = "severe. Be precautious!"


            # Printing prediction in console
            print(f"Storm Prediction: {prediction[0]}")


            return render_template('storm.html', prediction=prediction[0], severity=severity)
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return render_template('storm.html', error=f"Invalid input: {ve}")
        except Exception as e:
            print(f"Error in storm prediction: {e}")
            return render_template('storm.html', error="Error processing form input.")
    return render_template('storm.html')


#drought web page
@app.route("/drought", methods=["GET", "POST"])
def drought_disaster():
    if request.method == 'POST':
        try:
            min_temperature = request.form.get('min-temparature')
            max_temperature = request.form.get('max-temparature')
            precipite = request.form.get('precipitation')

            # values printing
            print(
                f"Received data - Min Temp: {min_temperature}, Max Temp: {max_temperature}, Precipitation: {precipite}")

            # float conversion
            min_temperature = float(min_temperature) if min_temperature else None
            max_temperature = float(max_temperature) if max_temperature else None
            precipite = float(precipite) if precipite else None

            # checking missing fields
            if None in [min_temperature, max_temperature, precipite]:
                raise ValueError("All input fields are required.")

            # Prediction input
            input_features = np.array([[min_temperature, max_temperature, precipite]])
            prediction = drought_model.predict(input_features)

            # Determining the drought severity level based on prediction
            if prediction < 2.0:
                severity = "mild. You're safe!"
            elif 2.0 <= prediction <= 4.0:
                severity = "moderate. Keep a check!"
            else:
                severity = "severe. Be precautious!"

            # Printing prediction in console
            print(f"Drought Prediction: {prediction[0]}")


            return render_template('drought.html', prediction=prediction[0], severity=severity)
        except ValueError as ve:
            print(f"ValueError: {ve}")
            return render_template('drought.html', error=f"Invalid input: {ve}")
        except Exception as e:
            print(f"Error in drought prediction: {e}")
            return render_template('drought.html', error="Error processing form input.")
    return render_template('drought.html')



if __name__ =="__main__":   #entry point
    app.run(port=5001, debug = True)    #automatically restarts the app





