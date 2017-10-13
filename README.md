# wsgi
## simplest uwsgi framework

This framework is designed for educational purposes and minimally supports the concept of mvc (Model View Controller).

for deploy application

> uwsgi --http :9090 --wsgi-file application.py

The application folder structure must match
* controller folder named "controller"
* model folder named "model"
* views folder named "view"
* template folder named "template"

# Attention
Render to templates are not implemented but you can do it yourself

Example application contain simple controller, model, view and simple sqlite3 database.

  Examples of rules bindings
  ```Python
  rules = {
        'mymodel/': 'mymodel_show',
        '/': 'mymodel_list'
    }