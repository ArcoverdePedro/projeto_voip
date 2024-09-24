from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pergunta1')
def pergunta1():
    return render_template('pergunta1.html')

@app.route('/pergunta2')
def pergunta2():
    return render_template('pergunta2.html')

@app.route('/pergunta3')
def pergunta3():
    return render_template('pergunta3.html')

@app.route('/pergunta4')
def pergunta4():
    return render_template('pergunta4.html')

@app.route('/pergunta5')
def pergunta5():
    return render_template('pergunta5.html')

@app.route('/fim')
def fim():
    return render_template('fim.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

