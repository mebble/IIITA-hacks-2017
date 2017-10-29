from flask import Flask,render_template,request,url_for,redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/places')
def places():
        return render_template('places.html')




if __name__ == '__main__':
    app.run(debug=True)
