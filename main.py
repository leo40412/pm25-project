from flask import Flask
from datetime import datetime

app = Flask(__name__)  # 開啟


@app.route("/bmi/height=<h>&weight=<w>")
def get_bmi(h, w):
    bmi = round(eval(w) / ((eval(h) / 100) ** 2), 2)
    return f"<h1>身高:{h}cm 體重:{w}kg<br> BMI:{bmi}</h1>"  # 字串、字典、串列


@app.route("/books")
@app.route("/books/id=<int:id>")  # /1=>id=1 比較好
# 給他ID /1/2/3 可以show出單一值
# 但無法單一畫面show出三個
# 給他int是因為上面123是字串
def get_book(id=None):  # id給他預設值None才可以去連接books
    try:
        books = {1: "Python book", 2: "Java book", 3: "Flask book"}

        if id == None:
            return books

        return books[id]
    except Exception as e:
        return f"書籍編號錯誤:{e}"


@app.route("/nowtime")
def now_time():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 西元年月日 時分秒
    print(time)
    return {"time": time}  # 只能return有容器的


@app.route("/")  # / 為首頁
def index():
    return "<h1>寫程式好難喔</h1>"


app.run(debug=True)  # 這樣才可以執行
