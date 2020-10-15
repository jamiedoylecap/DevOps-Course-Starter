import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, redirect, url_for
from viewmodel import Todo, IndexView


app = Flask(__name__)
app.config.from_object('flask_config.Config')

def get_trello_auth():
    return {'key': os.getenv('TRELLO_KEY'), 'token': os.getenv('TRELLO_TOKEN')}

def move_card_to_list(card_id, new_list_id):
    params = get_trello_auth()
    params['idList'] = new_list_id
    return requests.put(f"https://api.trello.com/1/cards/{card_id}", params=params)


@app.route('/', methods=['get'])
def index():

    todo_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_TODO') + '/cards', params=get_trello_auth()).json()
    doing_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DOING') + '/cards', params=get_trello_auth()).json()
    done_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + os.getenv('TRELLO_DONE') + '/cards', params=get_trello_auth()).json()

    my_view_model = IndexView.build_from_json(todo_list_api_response_in_json, doing_list_api_response_in_json, done_list_api_response_in_json)
    #my_view_model = ViewModel(class_todo_list_api_response, doing_list_api_response_in_json, done_list_api_response_in_json)
    return render_template('index.html', view_model=my_view_model)
    #return render_template('index.html', list_todo=class_todo_list_api_response, list_doing=doing_list_api_response_in_json, list_done=done_list_api_response_in_json)

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