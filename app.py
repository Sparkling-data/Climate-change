from flask.json import jsonify
from flask import Flask, render_template, request
from dao import chart_dao
# from mchart import
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=["GET"])
def start():
    return render_template("adult_login.html")


@app.route('/main', methods=["GET"])
def main():
    return render_template("order.html")


@app.route('/chart', methods=["GET"])
def move():
    return render_template("chart.html")


@app.route('/calling', methods=["get"])
def mchart():

    a = chart_dao().chart2()
    b = chart_dao().chart3()
    # 여기서 DAO 에서 판다스 만들기
    # mchart() == > 차트 만들기
    return a  # 에서 만든 차트 보내기??  가능?? 차트 정보 보내서 html 에서 google chart?


@app.route("/co2", methods=["get"])
def co2():
    return render_template("co2.html")


@app.route("/sea_t", methods=["get"])
def st():
    return render_template("sea_t.html")


@app.route("/atmo_t", methods=["get"])
def at():
    return render_template("atmo_t.html")


@app.route("/height", methods=["get"])
def height():
    return render_template("height.html")


@app.route("/total", methods=["get"])
def total():
    return render_template("total.html")


# pandas 가서 차트 만들기
# return render_template("chart2.html")
if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port="5000",
            debug=True)
