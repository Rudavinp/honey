from webob import Request, Response
from parse import parse

import gunicorn

class API:
    def __init__(self):
        self.routers = {}
        print(2, self.routers)

    def __call__(self, environ, start_response):
        print(1, self.routers)
        request = Request(environ)
        response = self.handle_request(request, environ)

        # response.text = 'Hello, World!'
        # status = '201 OK'
        # response_headers = [
        #     ('Content-type', 'text/plain'),
        #     ('Content-Length', str(len(response_body)))
        # ]
        # start_response(status, response_headers)
        return response(environ, start_response)

    def route(self, path):
        print(4, self.routers)
        def wrapper(handler):
            self.routers[path] = handler
            print(6, self.routers)
            return handler
        return wrapper

    def handle_request(self, request, environ):
        response = Response()
        handler, kwargs =  self.find_handler(request.path)

        if handler:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response


    def find_handler(self, request_path):
        print(3, self.routers)
        for path, handler in self.routers.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def default_response(self, response):
        response.status_code = 404
        response.text = 'Not found'

def server(host='127.0.0.1', port=8000, app=None):
    from wsgiref import simple_server
    server = simple_server.make_server(host, port, app)
    print('Start Honey server on port {} ....'.format(port))
    server.serve_forever()


