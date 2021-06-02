from flask import Flask, render_template, request
from docxtpl import DocxTemplate
import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")
        jobtitle = request.form.get("jobtitle")
        salary = request.form.get("salary")
        Today_Date = datetime.datetime.today().strftime('%d/%m/%Y')
        doc = DocxTemplate("sample.docx")
        context = {
            'Today_Date' : Today_Date,
            'Your_Name' : name,
            'Your_Address' : address,
            'Job_Title' : jobtitle,
            'Salary_Amount' : salary
        }
        doc.render(context)
        doc.save('name' + 'jobtitle' + '.docx')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)