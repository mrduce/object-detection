from urllib import request
from flask import Flask, render_template,request
import socket
hostname =socket.gethostname() 
IpAddr = socket.gethostbyname(hostname)
app = Flask(__name__)
@app.route("/myexes")
def listofmyexes():
    return render_template("1.html")
@app.route("/fromfilled")    
def view():
    name = request.args.get("name")
    age = request.args.get("age")
    status = request.args.get("status")
    cd = (name +","+ age+","+status)
    return(cd)
if __name__=="__main__":
    app.run(host = str(IpAddr), port=8090, debug = True)    
