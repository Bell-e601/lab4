from flask import Flask, render_template, request
import frequent as fr
app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        text = request.form.get('text')
    return render_template('index.html', ans=fr.frequent_word(text))


if __name__ == '__main__':
    app.run()