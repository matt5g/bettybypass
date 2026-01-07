from flask import Flask, request
from flask_cors import CORS, cross_origin
import random
import string
import requests
import sys

url = "https://raw.githubusercontent.com/matt5g/bettybypass/refs/heads/main/htm.txt"
r = requests.get(url)
if (r.text != "penis67"):
    sys.exit("Access revoked.")


app = Flask(__name__)

@app.route('/')
def index():
    return 'API Hijacked by bypass.py'

@app.route('/v1/info/<id>',methods = ['GET'])
@cross_origin(supports_credentials=True)
def cbdinfo(id):
    
    info = {
            "settings":{
                "text":"Dont Worry this is just a formality We dont actually care",
                "success_text":"LOL EZ bypass",
                "workflow":{
                    "us":{
                        "min_age":21
                    },
                    "states":{
                    },
                    "ca":{
                        "min_age":21
                    },
                    "ca_provinces":{
                    },
                    "international":{
                        "min_age":21
                    },"countries":{
                    }
                }
            },
            "store_name":"Vladimir"
        }
    return info
@app.route('/v1/create',methods = ['POST','OPTIONS'])
@cross_origin(supports_credentials=True)
def cbdcreate():
    if request.method == 'OPTIONS':
        return '', 200
    else:
        uuid = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(32))
        print('bypassed age verification with uuid : ' + uuid)
        return {
            "uuid": f"{uuid}",                
            "status": "accepted"
        }


if __name__ == '__main__':
    context = (r'C:\Users\lydia\Desktop\BettyVape\api.agechecker.net+2.pem',r'C:\Users\lydia\Desktop\BettyVape\api.agechecker.net+2-key.pem')
    app.run(port = 443, debug = False, ssl_context = context)
    