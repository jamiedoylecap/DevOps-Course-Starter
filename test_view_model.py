from viewmodel import ViewModel, Todo

def test_can_show_todo_items():
    # Setup
    todo_items = [
        Todo(1, "New Todo", "To Do")
    ]
    doing_items = [
        Todo(2, "In Progress Todo", "Doing")
    ]
    done_items = [
        Todo(3, "Finished Todo", "Done")
    ]

    view_model = ViewModel(todo_items, doing_items, done_items)

    # Act
    view_model_todo_items = view_model.just_todo

    # Assert
    assert len(view_model_todo_items) == 1
    assert view_model_todo_items[0].status == "To Do"

def test_can_show_doing_items():
    # Setup
    todo_items = [
        Todo(1, "New Todo", "To Do")
    ]
    doing_items = [
        Todo(2, "In Progress Todo", "Doing")
    ]
    done_items = [
        Todo(3, "Finished Todo", "Done")
    ]

    view_model = ViewModel(todo_items, doing_items, done_items)

    # Act
    view_model_doing_items = view_model.just_doing

    # Assert
    assert len(view_model_doing_items) == 1
    assert view_model_doing_items[0].status == "Doing"  

def test_can_show_done_items():
    # Setup
    todo_items = [
        Todo(1, "New Todo", "To Do")
    ]
    doing_items = [
        Todo(2, "In Progress Todo", "Doing")
    ]
    done_items = [
        Todo(3, "Finished Todo", "Done")
    ]

    view_model = ViewModel(todo_items, doing_items, done_items)

    # Act
    view_model_done_items = view_model.just_done

    # Assert
    assert len(view_model_done_items) == 1
    assert view_model_done_items[0].status == "Done"