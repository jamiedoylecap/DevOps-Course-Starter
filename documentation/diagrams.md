# ToDo App C4 Diagrams

## Context

```puml
@startuml
!include <c4/C4_Context.puml>  

'ref http://plantuml.com/stdlib
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>

LAYOUT_WITH_LEGEND()

title System Context diagram for ToDo Application

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
'!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Container.puml
!include <c4/C4_Container.puml>  

'ref http://plantuml.com/stdlib
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>

LAYOUT_WITH_LEGEND()


'title Container diagram for ToDo Application

Person(user  , ToDo User , "<$user>\n An end user who CRUD ToDo items" )

System_Boundary(c1, "ToDo System") {
    Container(gunicorn, "WSGI Server", "Gunicorn", "XXX")
    Container(flask, "WSGI Framwork", "Flask", "Provides all the To-Dp app functionality to users via their web browser")
    Container(todo, "ToDo App 'app.py'", "Python", "Provides the ToDo app functionality via HTTP")
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

'!includeurl https://raw.githubusercontent.com/RicardoNiepel/C4-PlantUML/master/C4_Component.puml
!include <c4/C4_Component.puml>  


LAYOUT_WITH_LEGEND()


title Component diagram for Internet Banking System - API Application

Container(spa, "Single Page Application", "javascript and angular", "Provides all the internet banking functionality to customers via their web browser.")
Container(ma, "Mobile App", "Xamarin", "Provides a limited subset ot the internet banking functionality to customers via their mobile mobile device.")
ContainerDb(db, "Database", "Relational Database Schema", "Stores user registration information, hashed authentication credentials, access logs, etc.")
System_Ext(mbs, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

Container_Boundary(api, "API Application") {
    Component(sign, "Sign In Controller", "MVC Rest Controlle", "Allows users to sign in to the internet banking system")
    Component(accounts, "Accounts Summary Controller", "MVC Rest Controlle", "Provides customers with a summory of their bank accounts")
    Component(security, "Security Component", "Spring Bean", "Provides functionality related to singing in, changing passwords, etc.")
    Component(mbsfacade, "Mainframe Banking System Facade", "Spring Bean", "A facade onto the mainframe banking system.")

    Rel(sign, security, "Uses")
    Rel(accounts, mbsfacade, "Uses")
    Rel(security, db, "Read & write to", "JDBC")
    Rel(mbsfacade, mbs, "Uses", "XML/HTTPS")
}

Rel(spa, sign, "Uses", "JSON/HTTPS")
Rel(spa, accounts, "Uses", "JSON/HTTPS")

Rel(ma, sign, "Uses", "JSON/HTTPS")
Rel(ma, accounts, "Uses", "JSON/HTTPS")
@enduml
```

## Code (Stretch)