from flask import Flask
import random,os
app = Flask(__name__)

@app.route('/')
def randompic():
    #<img src=""></img>
    os.chdir('img')
    fn = os.listdir()
    imgname = str(random.randint(0,len(fn))) + '.jpg'
    return '<img src="/img/' + imgname + '"></img>'