import datetime
from flask import Flask , render_template , request
from pymongo import MongoClient
import urllib
import os
from dotenv import load_dotenv

load_dotenv()
def create_app():
    app = Flask(__name__)
    

    mongo_uri = "mongodb+srv://rajputsrshubham930:" + urllib.parse.quote("Shubham123@") + "@todolistappication.tn0o23o.mongodb.net/test"
    client = MongoClient(mongo_uri)
    app.db = client.todolistapplicationdata

    entries = []

    @app.route("/" , methods=['GET' , 'POST'])

    def hello():
        global entries
        if request.method=='POST':
            entry_content = request.form.get('content')
            app.db.entries.insert_one({
                'content':entry_content , 'date':datetime.datetime.today().strftime('%Y-%m-%d')

            })

        entries = [(
                entry['content'] , entry['date']

        ) for entry in app.db.entries.find({})]

        
        return render_template('home.html' , entries = entries)
    return app