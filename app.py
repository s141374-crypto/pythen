from flask import Flask  # 載入 Flask

app = Flask(__name__)  # 建立 application 物件

# 建立網站首頁的回應方式
@app.route("/")
def index():
    return "hello flask"

# 只有直接執行這個檔案時才啟動 Flask
if __name__ == "__main__":#如果「現在是直接執行 app.py」，就執行 app.run()
    app.run()
