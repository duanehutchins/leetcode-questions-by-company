from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="">Hello</h1>'\
           '<p>This is a paragraph</p>'\
           '<img src="https://media.giphy.com/media/05RSNPDymIkQor0AV1/giphy.gif" width=500px>'

def make_bold(fun):
    def wrapper():
        fun()
    return f"<b>{wrapper}"

@app.route('/hi')
@make_bold
def hi():
    return "Hello ki"

if __name__=="__main__":
    app.run()