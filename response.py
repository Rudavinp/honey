from wsgiref.headers import Headers
import http.client as http

status = {200: 'OK'}


class Response():
    def __init__(self, body='', headers=None, status_code=200):
        self.body = body
        self.status_code = status_code
        self.headers = headers if headers is not None else []
        print(12, type(self.headers), self.headers)
        self.status = status.get(status_code, '')