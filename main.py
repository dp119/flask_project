from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


app.run(debug=True)
