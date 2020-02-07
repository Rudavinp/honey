from request import Request
from parse import parse
from response import Response


class API:
    def __init__(self):
        self.routers = {}

    def __call__(self, environ, start_response):

        request = Request(environ)
        response = self.handle_request(request, environ)

        start_response(response.status, response.headers)
        print(environ.items())
        print('++++++++++++++++++')
        print(request.path)
        for i in request.headers:
            print(i)
        return [str.encode(response.body)]

    def route(self, path):
        def wrapper(handler):
            self.routers[path] = handler
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
        for path, handler in self.routers.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def default_response(self, response):
        response.status_code = 404
        response.body = 'Not found'

def server(host='127.0.0.1', port=8000, app=None):
    from wsgiref import simple_server
    server = simple_server.make_server(host, port, app)
    print('Start Honey server on port {} ....'.format(port))
    server.serve_forever()


