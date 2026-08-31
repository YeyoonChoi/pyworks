from flask import Flask, render_template
import os #운영체제 관련 모듈

app = Flask(__name__)

# 현재 스크립트 디렉토리 경로 (절대 경로)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHOTOS_DIR = os.path.join(BASE_DIR, "static", "photos")

@app.route('/')
def index():
    # 웹 페이지 업로드
    return render_template("index.html")

@app.route('/gallery')
def gallery():
    # 디렉터리(폴더) 지정
    photo_list = os.listdir(PHOTOS_DIR)
    return render_template("gallery.html", photos=photo_list)

app.run(debug=True)