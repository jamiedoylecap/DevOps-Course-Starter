# To-Do App C4 Diagrams

## Context

```puml
@startuml
!include <c4/C4_Context.puml>  

'ref http://plantuml.com/stdlib
!include <office/Users/user.puml>
!include <office/Users/mobile_user.puml>

LAYOUT_WITH_LEGEND()

title System Context diagram for To-Do Application

Person(user  , To-Do User , "<$user>\n An end user who CRUD To-Do items" )

System(todo_system, "To-Do System", "Allows users to view information, update and delete their To-Do cards.")

System_Ext(trello, "Trello", "Stores all of the To-Do cards as a cloud service")

Rel(user, todo_system, "Uses")

Rel(todo_system, trello, "Uses")
@enduml
```

## Container


## Component


## Code (Stretch)