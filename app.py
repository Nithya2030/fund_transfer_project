from flask import Flask,request
from flask import jsonify
from pymongo import MongoClient
from datetime import datetime
from datetime import date
from bson.json_util import dumps
import json
from flask import make_response
from dbconfig import app


client = MongoClient("mongodb://127.0.0.1:27017")
db = client['fundtransfer'] #atabase name ==> fundtransfer
beneficiary = db['beneficiary'] # collection1 name ==> beneficiary
fundtransfer = db['fundtransaction'] #collection2 name ==> fundtransaction

@app.route('/fundtransfer', methods = ['POST'])
def fundtrans():
    try:
        #getting values from json
        transfer_from = request.json['transfer_from']
        bank_name = request.json['bank_name']
        amount = request.json['amount']
        remarks = request.json['remarks']
        payment_type = request.json['payment_type']
        toaccount = request.json['toaccount']
        
        #checking if the condition is POST
        if transfer_from and bank_name and amount and remarks and payment_type and toaccount and request.method == 'POST':
            #query to insert into db(fundtransfer)
            fundtransfer.insert_one({'transfer_from':transfer_from, 'bank_name':bank_name, 'amount':amount, 'remarks':remarks, 
                                    'payment_type':payment_type,'toaccount':toaccount, 'payment_date':tdate, 'payment_time':current_time})
            #returns jsonify result
            resp = jsonify("Details Added Successfully")
            resp.status_code = 200  #status code 
            return resp
        else:
            return make_response({"Message":"Not allowed"}, 400)
        
    except Exception as ex:
        return make_respose({'Bad request':str(ex)}, 404)

#to get the current time    
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#to get the current date
today = date.today()
tdate = today.strftime('%d:%m:%y')

@app.route('/getdetail', methods = ['GET'])
def getdetail():
    try:    
        if request.method == 'GET':    
            payeename = request.json['payeename']
            date_from = request.json['date_from']
            date_to = request.json['date_to']
            debitaccno = request.json['debitaccno']
        #if payeename and date_from and date_to and debitaccno and request.method == 'POST':
         #   fundtransfer.insert_one({'payeename':payeename, 'date_from':date_from, 'date_to':date_to, 'debitaccno':debitaccno})
        
            name = beneficiary.find({'name':name},{'bene_accno':1})
            print("Name",name)
            debitacc = fundtransfer.find({'transfer_from':transfer_from}, {'transfer_from':1})
            result = json.dumps(debitacc)
            print("Debitaccno",debitacc)
                               
            if payeename == name and debitaccno == result:
                res = fundtransfer.find({'paymentdate': {'$lt': date_to, '$gte': date_from }})
                resp = json.dumps({res})
                return resp
    except Exception as ex:
        return make_response({"ERROR":str(ex)}, 400)


@app.route('/getallaccdetails', methods = ['GET'])
def getalldetails():
    try:
        #if the method is GET
        if request.method == 'GET':
            #query to get all the data from the db
            result = fundtransfer.find({})
            resp = dumps(result)
            #resp.status_code = 200
            return jsonify({"Result":resp})
    except Exception as ex:
        return make_response({'ERROr':str(ex)}, 400)

if __name__ == "__main__":
    app.run(debug = True, host= '0.0.0.0', port = 5000)