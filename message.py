import nexmo
from flask import Flask,render_template,request,url_for

app = Flask(__name__)

client = nexmo.Client(key='3a9542ef',secret='e29280bddcd6e45f')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('index.html')
@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/send',methods=['GET','POST'])
def send():
    response = client.send_message({'from' : 'Raks','to' : '918919067237' , 'text':'Hello, thanks for using our API'})
    if request.method == 'GET':
        return 'Success'
    if request.method == 'POST':
        return 'Error'

if __name__ == '__main__':
    app.run(debug=True)
