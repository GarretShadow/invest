from flask import Flask, render_template
from flask import redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def start_page():
    return render_template('start_page.html')


@app.route('/sanding')
def sanding():
    file = request.args.get('filename')

    return redirect(url_for("stocks", symbol=symbol, start=start, end=end))
#@app.route('/stocks/<symbol>/<int:year>')


@app.route('/stocks')
def stocks(symbol, start, end):
    return render_template('stocks.html', data=data['data'], symbol=symbol, year=year)

@app.route('/')
def index():
    context = {}

    file = request.args.get('filename')

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
