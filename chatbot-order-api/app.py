from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Rest(Resource) : #상속 : resource의 자식
    def get(self) :
        return{'rest':'Good!'}

api.add_resource(Rest, '/') #route

# @app.route('/') # decorator = 추가하는 것 
# # (route  속성값을 app에 등위;/ url) => url에 결과 값이 보여준다 w/o not works
# def index() :
#     return {'rest':'OK'}



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
    
