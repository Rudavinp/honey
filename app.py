# -*- coding: utf-8 -*-
from api import API

app = API()

@app.route('/home/{name}')
def home(request, response, name):
    response.text= 'Привет,{} это главная страница'.format(name)

@app.route('/second/{some}')
def second(request, response, some):
    response.text = 'Hello, it is the second page {}'.format(some)
