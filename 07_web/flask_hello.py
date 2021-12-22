from flask import Flask

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 리부팅을 위한 분 함수
@app.route("/")
def hello_world():
    return '''
    <p>Hello, Flask!</p>
    <a href="/first">Go First</a>
    <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first_page():
    return '''
    <p>First Page</p>
    <a href="/">Go Home</a>
    '''

@app.route("/second")
def second_page():
    return '''
    <p>Second Page</p>
    <a href="/">Go Home</a>
    '''

# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)