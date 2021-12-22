from flask import Flask, render_template

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 리부팅을 위한 분 함수
@app.route("/")
def hello_world():
    return render_template(
        "hello.html",
        title="HELLO")

@app.route("/first")
def first_page():
    return render_template("first.html")

@app.route("/second")
def second_page():
    return render_template("second.html")

# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080) # HTML 만 바꾸면, 서버를 껐다가 켜지 않아도 된다.