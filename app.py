import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, redirect, url_for
from viewmodel import Todo, ViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_config.Config')
    
    @app.route('/', methods=['get'])
    def index():
        api_responses = ApiCall.grab_the_json_from_trello()
        my_view_model = ViewModel.build_from_json(api_responses.api_todo, api_responses.api_doing, api_responses.api_done)
        return render_template('index.html', view_model=my_view_model)

    @app.route('/test', methods=['get'])
    def test():
        return render_template('test.html')

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
    return app

def get_trello_auth():
    return {'key': os.getenv('TRELLO_KEY'), 'token': os.getenv('TRELLO_TOKEN')}

def move_card_to_list(card_id, new_list_id):
    params = get_trello_auth()
    params['idList'] = new_list_id
    return requests.put(f"https://api.trello.com/1/cards/{card_id}", params=params)

class ApiCall:
    def __init__(self, api_todo, api_doing, api_done):
        self.api_todo = api_todo
        self.api_doing = api_doing
        self.api_done = api_done

    @staticmethod
    def grab_the_json_from_trello():
        api_todo = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_TODO') + '/cards', params=get_trello_auth()).json()
        api_doing = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DOING') + '/cards', params=get_trello_auth()).json()
        api_done = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DONE') + '/cards', params=get_trello_auth()).json()
        
        return ApiCall(api_todo, api_doing, api_done)

