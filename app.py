import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, redirect, url_for
from viewmodel import Todo, Index_view


app = Flask(__name__)
app.config.from_object('flask_config.Config')

def get_trello_auth():
    return {'key': os.getenv('TRELLO_KEY'), 'token': os.getenv('TRELLO_TOKEN')}

def move_card_to_list(card_id, new_list_id):
    params = get_trello_auth()
    params['idList'] = new_list_id
    return requests.put(f"https://api.trello.com/1/cards/{card_id}", params=params)

class Api_call:
    def __init__(self, api_todo, api_doing, api_done):
        # self.api_todo = api_todo 
        # self.api_doing = api_doing
        # self.api_done = api_done
        pass

    @property
    def get_todo(self):
        return requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_TODO') + '/cards', params=get_trello_auth()).json()
    
    @property
    def get_doing(self):   
        return requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DOING') + '/cards', params=get_trello_auth()).json()
        
    @property
    def get_done(self):
        return requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DONE') + '/cards', params=get_trello_auth()).json()
        
    # def grab_the_json_from_trello():
    #     api_todo = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_TODO') + '/cards', params=get_trello_auth()).json()
    #     api_doing = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DOING') + '/cards', params=get_trello_auth()).json()
    #     api_done = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DONE') + '/cards', params=get_trello_auth()).json()
    # return Api_call(get_todo, get_doing, get_done)

@app.route('/', methods=['get'])
def index():
    # api_responses = Api_call.get_todo
    # my_view_model = Index_view.build_from_json(api_responses.api_todo, api_responses.api_doing, api_responses.api_done)
    # return render_template('index.html', view_model=my_view_model)
    
    todo = Api_call.get_todo
    #doing = Api_call.get_doing
    #done = Api_call.get_done
    my_view_model = Index_view.build_from_json(todo, todo, todo)
    return render_template('index.html', view_model=my_view_model)

@app.route('/additem', methods=['post'])
def add():
    new_item = request.form.get('new_title')
    params = get_trello_auth() 
    params['idList'] = os.getenv('TRELLO_TODO')
    params['name'] = new_item
    params['desc'] = 'From Jamies App'
    requests.post('https://api.trello.com/1/cards', params=params)
    return redirect('/', code=302)

@app.route('/movetonew/<id>', methods=['get'])
def move_to_new(id):
    move_card_to_list(id, os.getenv('TRELLO_TODO'))
    return redirect('/', code=302)

@app.route('/movetodoing/<id>', methods=['get'])
def move_to_doing(id):
    move_card_to_list(id, os.getenv('TRELLO_DOING'))
    return redirect('/', code=302)

@app.route('/movetodone/<id>', methods=['get'])
def move_to_done(id):
    move_card_to_list(id, os.getenv('TRELLO_DONE'))
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run()