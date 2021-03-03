# ToDo App C4 Diagrams

## Context

```puml
@startuml
!include <c4/C4_Context.puml>  
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>
LAYOUT_WITH_LEGEND()

Person(user  , ToDo User , "<$user>\n An end user who CRUD ToDo items" )
System(todo_system, "ToDo System", "Allows users to view information, update and delete their ToDo cards.")
System_Ext(trello, "Trello", "Stores all of the ToDo cards as a cloud service")

Rel(user, todo_system, "Uses")
Rel(todo_system, trello, "Uses")
@enduml
```

## Container

```puml
@startuml
!include <c4/C4_Container.puml>  
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>
LAYOUT_WITH_LEGEND()

Person(user  , ToDo User , "<$user>\n An end user who CRUD ToDo items" )

System_Boundary(c1, "ToDo System") {
    Container(gunicorn, "WSGI Server", "Gunicorn", "Provides the gateway between the user and the web app")
    Container(flask, "WSGI Framwork", "Flask", "Provides all the To-Dp app functionality to users via their web browser")
    Container(todo, "ToDo App", "Python", "Provides the ToDo app functionality via HTTP")
}
System_Ext(trello, "Trello", "Stores all of the ToDo cards as a cloud service")

Rel(user, gunicorn, "Uses", "HTTP")
Rel_Neighbor(gunicorn, flask, "Forwards")
Rel(flask, todo, "Uses")
Rel_Neighbor(todo, trello, "Make API calls to", "JSON/HTTPS")
@enduml
```

## Component

```puml
@startuml
!include <c4/C4_Component.puml>  
LAYOUT_WITH_LEGEND()

' Outside of Component Level
Container(flask, "WSGI Framwork", "Flask", "Provides all the To-Dp app functionality to users via their web browser")
System_Ext(trello, "Trello", "Stores all of the ToDo cards as a cloud service")

' Inside Component Level
Container_Boundary(todo, "ToDo Application") {
    Component(root, "Controller", "Python", "Provides entry point for user interaction and deals with all app route requests.")
    Component(webform, "Page render", "Flask/Jinja", "provides UI")
    Component(env, "Environment", "local file", "Contains Trello keys")
    Rel(root, webform, "Uses")
    Rel(webform, flask, "Supplies")
    Rel(root, trello,"API/HTTPS")
    Rel(root, env,"Imports")
}
@enduml
```

## Code (Stretch)

Not done
