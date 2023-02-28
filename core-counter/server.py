from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'A secret key.'


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        print('Counter does not exist!')
        session['counter'] = 0
    return render_template('index.html')


@app.route('/counter/add_two')
def plus_two():
    session['counter'] += 1
    print('Counter increments by 2.')
    return redirect('/')


@app.route('/counter/custom_increment/', methods=['POST'])
def custom_increment():
    num = request.form['num']
    session['counter'] += (int(num) - 1)
    return redirect('/')


@app.route('/counter/destroy')
def delete():
    session.pop('counter')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
