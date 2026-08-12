from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/LOL')
def LOL():
    return render_template('demo_LOL.html')


@app.route('/income')
def income():
    return render_template('demo_income.html')


@app.route('/dbmovie')
def dbmovie():
    return render_template('demo_dbmovie.html')


@app.route('/dbmovie0')
def dbmovie0():
    return render_template('demo_dbmovie_0.html')


@app.route('/tv')
def tv():
    return render_template('demo_tv.html')


@app.route('/douyin')
def douyin():
    return render_template('demo_douyin.html')


@app.route('/tsdr')
def tsdr():
    return render_template('demo_tsdr.html')


@app.route('/58zufang')
def zufang58():
    return render_template('demo_58zufang.html')


@app.route('/zta')
def zta():
    return render_template('demo_zta.html')


@app.route('/weibohot')
def weibohot():
    return render_template('demo_weibohot.html')


@app.route('/city')
def city():
    return render_template('demo_city.html')

@app.route('/zbsk')
def zbsk():
    return render_template('demo_zbsk.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
