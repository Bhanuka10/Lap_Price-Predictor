from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Template')

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        ram = request.form['Ram']
        Weight = request.form['Weight']
        Touchscreen = request.form['Touchscreen']
        IPS = request.form['IPS']
        Companey = request.form['Companey']
        TypeName = request.form['TypeName']
        OperatingSystem = request.form['OperatingSystem']
        cpu= request.form['cpu']
        gpu = request.form['gpu']
        print(ram, Weight, Touchscreen, IPS, Companey, TypeName, OperatingSystem, cpu, gpu)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
