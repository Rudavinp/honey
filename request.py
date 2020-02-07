
class Request:
    def __init__(self, environ):
        self.environ = environ if environ else {}
        self.environ['haney.request'] = self

    @property
    def path(self):
        return '/' + self.environ.get('PATH_INFO', '').lstrip('/')

    @property
    def method(self):
        return self.environ.get('REQUEST_METHOD', 'GET').upper()

    @property
    def headers(self):
        return{k[len('HTTP_'):]:v
               for k, v in self.environ.items()
               if k.startswith('HTTP_')}

    @property
    def body(self):
        length = self.environ['CONTENT_LENGTH']
        if length:
            self._body = self.environ['wsgi.input'].read(int(length))
        else:
            self._body = b''
        return self._body.decode('utf-8')

    def __getitem__(self, item):
        return self.environ[item]