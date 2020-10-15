class Todo:
    def __init__(self, item_id, name, status):
        self.item_id = item_id
        self.name = name
        self.status = status

class IndexView:
    def __init__(self, list_todo, list_doing, list_done):
        self.list_todo = list_todo
        self.list_doing = list_doing
        self.list_done = list_done

    @staticmethod
    def build_from_json(todo_list_api_response_in_json, doing_list_api_response_in_json, done_list_api_response_in_json):
        class_todo_list_api_response = []
        for iteminjson in todo_list_api_response_in_json:
            class_todo_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'To Do'))

        class_doing_list_api_response = []
        for iteminjson in doing_list_api_response_in_json:
            class_doing_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Doing'))
        
        class_done_list_api_response = []
        for iteminjson in done_list_api_response_in_json:
            class_done_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Done'))
        
        return IndexView(class_todo_list_api_response, class_doing_list_api_response, class_done_list_api_response)
