#import consul
from flasgger import Swagger
from flask import Flask
#from flask_cors import CORS

app = Flask(__name__)

# csrf=SeaSurf(app)
# CORS(app,resources={r"/api/*": {"origins": "*"}})
#app.config['MONGODB_DB'] = 'Account_Opening'
#app.config['SECRET_KEY'] = 'secretkey'

app.config["SWAGGER"]={"title":"Swagger-UI","uiversion":2}

swagger_config={
    "headers":[],
    "title": "Account Opening API",
    "specs":[
        {
            "endpoint":"apispec_1",
            "route":"/apispec_1.json",
            "rule_filter":lambda rule: True,
            "model_filter": lambda tag:True,
        }
    ],
    "static_url_path":"/flasgger_static",
    "swagger_ui": True,
    "specs_route":"/swagger/",
}
swagger=Swagger(app, template_file='fundtransfer.yaml',config=swagger_config)

# db = MongoEngine(app)
# connect('db', host='mongodb-bank', port=27017, alias='bankservicedb')
# disconnect(alias='bankservicedb')


