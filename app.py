from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('page1.html')

@app.route('/page2')
def homepage_styles():
    return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

# cd flask-html
# python app.py