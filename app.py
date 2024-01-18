from flask import Flask

app= Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
    return "Hello World !"

@app.route('/hetic',methods=['GET','POST'])
def hetic():
    return "Hello World Hetic !"

if __name__=='__main__':
    app.run("0.0.0.0",port=80)

'''
 web:
    build: .
    command: python app.py
    ports:
      - "80:80"
    restart: always
    volumes:
      - ./static/pwa/icon:/app/static/pwa/icon
'''