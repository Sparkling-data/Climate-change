from flask.json import jsonify
from flask import Flask, render_template, request
from dao import chart_dao
# from mchart import
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=["GET"])
def home():
    return render_template("main.html")


@app.route('/chart2', methods=["GET"])
def mchart():
    a = chart_dao()
    # 여기서 DAO 에서 판다스 만들기
    # mchart() == > 차트 만들기
    return a  # 에서 만든 차트 보내기??  가능?? 차트 정보 보내서 html 에서 google chart?


# pandas 가서 차트 만들기

# return render_template("chart2.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port="5000",
            debug=True)
