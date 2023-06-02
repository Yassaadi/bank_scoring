from flask import Flask, render_template, request, jsonify
import sklearn
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)
model = pickle.load(open('pad_pkl_model.pkl', 'rb'))
path= "app_data.csv"
txt = pd.read_csv(path, engine= 'python', sep=',', chunksize=100, usecols=lambda col: col not in ['Unnamed: 0', 'index'])
app_data = pd.concat(txt, ignore_index=True)
features = [col for col in app_data.columns if col != 'SK_ID_CURR' ]

@app.route('/')
def home():
  return render_template('indexFLASK.html')

@app.route('/predict',methods=['POST'])
def predict():
  client_id = int(request.form['client_id'])
  client_data = app_data.loc[app_data["SK_ID_CURR"]==client_id, features]
  prediction = model.predict_proba(client_data)
  return render_template('indexFLASK.html', output="Client statute: {}".format(prediction[0, 1]))

if __name__=='__main__':
   app.run()
