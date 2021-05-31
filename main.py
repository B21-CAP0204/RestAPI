from flask import Flask, jsonify, request
import json
#This API is a dummy API for return validation family card number.
#If response for kk -> "kk" : True -> It means data that entered by user & pass by ML not exists on database Dukcapil. So we verify that data can be registered.
#If response for kk -> "kk" : False -> It means data that entered by user & pass by ML exists on database Dukcapil. So user can't register with that data.
users_data = [
    {
        "id" : 1,
        "no_kk" : "123456789",
        "nama_kepala" : "Jokowi",
        "ttl":"12091990"
    },
    {
        "id" : 2,
        "no_kk" : "987654321",
        "nama_kepala" : "Rudi",
        "ttl":"8051995"
    }
]

app = Flask(__name__)

#This function is for search by the ID and return all the data by id
#Example : http://url/users?id=1 -> the results are all the data in this API
# @app.route('/users', methods=['GET'])
# def get_value_by_id():
#     user_id = request.args.get('id',type=int)

#     user_id = int(json.dumps(user_id))-1
    
#     return jsonify(users_data[user_id])


@app.route('/api2', methods=['GET'])
def kk():
    no_kk = request.args.get('no_kk',type=str)
    resp_kk = {}
    if not any(data['no_kk'] == no_kk for data in users_data):
        resp_kk = {
            "kk" : True
        }
        return jsonify(resp_kk)
    else:
        resp_kk={
            "kk" : False
        }
        return jsonify(resp_kk)
    

if __name__ == '__main__':
  app.run()