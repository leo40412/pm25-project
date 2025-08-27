from flask import Flask, render_template #連接網頁模板render這個
from datetime import datetime
from pm25 import get_open_data
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348"
    },

    2: {

        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348"
    },

    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348"
    },
}

app = Flask(__name__)  # 開啟

@app.route("/pm25")
def get_pm25():

    values = get_open_data()
    #print(values)
    columns = ["站點名稱","縣市","PM2.5","更新時間","單位"]
    return render_template("pm25.html",columns=columns,values=values)



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
        if id == None:
            return render_template("books.html",books=books)

        return books[id]
    except Exception as e:
        return f"書籍編號錯誤:{e}"


@app.route("/nowtime")
def now_time():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 西元年月日 時分秒
    # print(time)
    return time  # 盡量return 


@app.route("/")  # / 為首頁
def index():
    time=now_time()
    return render_template("index.html",x=time,name="jerry")


app.run(debug=True)  # 這樣才可以執行
