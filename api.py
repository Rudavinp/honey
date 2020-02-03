from webob import Request, Response
from parse import parse
import gunicorn

class API:
    def __init__(self):
        self.routers = {}

    def __call__(self, environ, start_response):
        print(100, start_response)
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
        def wrapper(handler):
            self.routers[path] = handler
            return handler
        return wrapper

    def handle_request(self, request, environ):
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        print(22, method)
        print(22, path)
        user_agent = request.environ.get("HTTP_USER_AGENT", "No User Agent Found")
        response = Response()
        handler, kwargs =  self.find_handler(request.path)

        if handler:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response


    def find_handler(self, request_path):
        for path, handler in self.routers.items():
            print(33, path, request_path)
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def default_response(self, response):
        response.status_code = 404
        response.text = 'Not faund'