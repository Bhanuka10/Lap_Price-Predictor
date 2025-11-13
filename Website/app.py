from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Template')

@app.route('/', methods=['POST', 'GET'])
def home():
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

        Companey_list = ['Apple', 'Asus', 'Acer', 'Dell', 'HP', 'Lenovo', 'MSI', 'Toshiba', 'Other']
        TypeName_list = ['Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible', 'Workstation', 'Netbook']
        OperatingSystem_list = ['Windows', 'MacOS', 'Linux', 'Other']
        cpu_list = ['Intel Core i7', 'Intel Core i5', 'Intel Core i3', 'Other Intel processor', 'amd processor']
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

        print(feature_list)   
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
