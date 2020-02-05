# -*- coding: utf-8 -*-
from api import API, server

app = API()



@app.route('/second/{some}')
def second(request, response, some):
    print(5)
    response.body = 'Hello, it is the second page {}'.format(some)

@app.route('/home/{name}')
def home(request, response, name):
    response.body= 'Привет,{} это главная страница'.format(name)


server(app=app)