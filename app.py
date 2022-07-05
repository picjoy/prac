from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['GET']) # '/test'라는 창구에서 그것을 받아 있음
def test_get():
   # 'title_give'라는 이름으로 뭔가를 받아와서 'title_receive'라는 변수에다 넣었고
   title_receive = request.args.get('title_give')
   # 걔를 찍었줬어!
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '요청 잘 받았어요!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)