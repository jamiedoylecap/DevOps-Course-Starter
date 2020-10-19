#from datetime import datetime

class Todo:
    def __init__(self, item_id, name, status, dateLastActivity):
        self.item_id = item_id
        self.name = name
        self.status = status
        self.dateLastActivity = dateLastActivity

    # @classmethod
    # def from_trello_card(cls, trello_card, status):
    #     trello_date = date.strftime()
    #     return cls(trello_card['id'], trello_card['name'], status, trello_card['dateLastActivity'])
    #     return cls(trello_card['id'], trello_card['name'], status)

class ViewModel:
    def __init__(self, list_todo, list_doing, list_done):
        self.list_todo = list_todo
        self.list_doing = list_doing
        self.list_done = list_done

    # @classmethod
    # def build_from_json(cls, todo_list_api_response_in_json, doing_list_api_response_in_json, done_list_api_response_in_json):
    
    @staticmethod
    def build_from_json(todo_list_api_response_in_json, doing_list_api_response_in_json, done_list_api_response_in_json): 
        class_todo_list_api_response = []
        for iteminjson in todo_list_api_response_in_json:
            #class_todo_list_api_response.append(Todo.from_trello_card(iteminjson, 'To Do'))
            class_todo_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'To Do', iteminjson['dateLastActivity']))

        class_doing_list_api_response = []
        for iteminjson in doing_list_api_response_in_json:
            #class_doing_list_api_response.append(Todo.from_trello_card(iteminjson, 'Doing'))
            class_doing_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Doing', iteminjson['dateLastActivity']))
        
        class_done_list_api_response = []
        for iteminjson in done_list_api_response_in_json:
            #class_done_list_api_response.append(Todo.from_trello_card(iteminjson, 'Done'))
            class_done_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Done', iteminjson['dateLastActivity']))
        
        #return cls(class_todo_list_api_response, class_doing_list_api_response, class_done_list_api_response)
        return ViewModel(class_todo_list_api_response, class_doing_list_api_response, class_done_list_api_response)
    
    @property
    def just_todo(self):
        return self.list_todo
    
    @property
    def just_doing(self):
        return self.list_doing
    
    @property
    def just_done(self):
        return self.list_done
    
    @property
    def show_all_done_items(self, parameter_list):
        """
        docstring
        """
        pass

    @property
    def recent_done_items(self, parameter_list):
        #today_date = datetime.date.today()
        pass
    
    @property
    def older_done_items(self, parameter_list):
        """
        docstring
        """
        pass