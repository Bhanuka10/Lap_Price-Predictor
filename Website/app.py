from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__, template_folder='Template')
def predict(list):
    fil_name ='model/model.pkl'
    with open(fil_name, 'rb') as file:
        model = pickle.load(file)
        pred_value = model.predict([list])
        return pred_value

@app.route('/', methods=['POST', 'GET'])

def home():
    pred = None  # Initialize pred variable
    if request.method == 'POST':
        ram = request.form['Ram']
        Weight = request.form['Weight']
        Touchscreen = request.form.get('Touchscreen', '')
        IPS = request.form.get('IPS', '')
        Companey = request.form['Companey']
        TypeName = request.form['TypeName']
        OperatingSystem = request.form['OperatingSystem']
        cpu= request.form['cpu']
        gpu = request.form['gpu']
        
        feature_list = []
        feature_list.append(int(ram))
        feature_list.append(float(Weight))
        feature_list.append(1 if Touchscreen else 0)
        feature_list.append(1 if IPS else 0)

        Companey_list = ['Asus', 'Acer', 'Dell', 'HP', 'Lenovo', 'MSI', 'Toshiba', 'Other']
        TypeName_list = ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation', 'Netbook']
        OperatingSystem_list = ['Windows', 'MacOS', 'Linux', 'Other']
        cpu_list = ['intel core i7', 'intel core i5', 'intel core i3', 'other intel processor', 'amd processor']
        gpu_list = ['nvidia', 'intel', 'amd']

        def traverse(Lst, value):
            for item in Lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse(Companey_list, Companey)
        traverse(TypeName_list, TypeName)
        traverse(OperatingSystem_list, OperatingSystem)
        traverse(cpu_list, cpu)
        traverse(gpu_list, gpu)

        pred = predict(feature_list)*219
        pred= np.round(pred[0], 2)
        print(f"Prediction: {pred}")
        
    return render_template('index.html', pred=pred)

if __name__ == '__main__':
    app.run(debug=True)
