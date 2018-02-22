from flask import Flask, request
from flask_restful import Resource, Api
import sys
import time
from pytz import reference
import datetime

app = Flask(__name__)
api = Api(app)


class TodoSimple(Resource):
    def get(self):
        return { 'time' : time.strftime("%b %d %Y %H:%M:%S") }

class TodoSimple1(Resource):
    def get(self):
        localtime = reference.LocalTimezone()
        today = datetime.datetime.now()
        return { 'timezone' : localtime.tzname(today) }

class TodoYear(Resource):
    def get(self):
        now = datetime.datetime.now()
        return { 'date' : now.year}


class TodoMonth(Resource):
    def get(self):
        now = datetime.datetime.now()
        return { 'date' : now.month}


class TodoDay(Resource):
    def get(self):
        now = datetime.datetime.now()
        return { 'date' : now.day}

api.add_resource(TodoSimple, '/time')
api.add_resource(TodoSimple1, '/timezone')
api.add_resource(TodoYear, '/year')
api.add_resource(TodoMonth, '/month')
api.add_resource(TodoDay, '/day')

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10002
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
