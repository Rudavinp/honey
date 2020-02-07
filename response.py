from wsgiref.headers import Headers
import http.client as http

status = {200: '200 OK'}


class Response():
    def __init__(self, body='', headers=None, status_code=200):
        self.body = body.encode()
        self.status_code = status_code
        self.headers = headers if headers is not None else []
        self.status = status.get(status_code, '')