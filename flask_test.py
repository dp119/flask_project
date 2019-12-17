from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
    return render_template('index.html')


@app.route('/about')
def deepu():
    return render_template('about.html')


app.run(debug=True)
