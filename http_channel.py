from flask import Flask
from flask import request
from datetime import datetime
app = Flask(__name__)

@app.route('/inbound',methods=['GET','POST'])
def inbound():
    if(request.method == 'GET'):
        res=request.args
        f=open('data','a+')
        data=request.args
        f.write(str(datetime.now())+str(data)+"\n")
        return(res)
    if(request.method == 'POST'):
        res=request.data
        print(request.form)
        f=open('data','a+')
        f.write(str(datetime.now())+str(request.form)+"\n")
        return(res)

    return('not my kind of dish .! i eat possstterrs!')

@app.route('/outbound',methods=['GET','POST'])
def outbound():
    return("yes")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=9090)
