from http.client import responses
from pickle import GLOBAL
from wsgiref.util import application_uri

from jinja2 import Environment, FileSystemLoader
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

#Настройка среды для jinja2
template_env = Environment(
    loader=FileSystemLoader("templates")
)

GLOBAL_COUNTER = 0
PORT = 8000
HOST = "localhost"

class HTTPHandler(BaseHTTPRequestHandler):
    # Запрос на сервер, возвращает html страницу
    def do_GET(self):
        global GLOBAL_COUNTER

        if self.path == '/':
            html_content = self.render_template('index.html', {'count': GLOBAL_COUNTER})
            self.send_response(200)
            self.send_header("Content-type", 'text/html; charset="utf-8"')
            self.end_headers()
            self.wfile.write(html_content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found') # байтовая кодировка передачи текста

    def do_POST(self):
        global GLOBAL_COUNTER
        if self.path == '/increment':
            GLOBAL_COUNTER += 1
            new_count = GLOBAL_COUNTER
            response_data = {'status': 'success', 'new_count': new_count}
            json_response = json.dumps(response_data).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_response)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found') # байтовая кодировка передачи текста

    def render_template(self, template_name, context={}):
        template = template_env.get_template(template_name)
        return template.render(context).encode("utf-8")


if __name__=='__main__':
    server_address = (HOST, PORT)
    server = HTTPServer(server_address, HTTPHandler)
    print('http://localhost:8000/')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close() #Корректно закрывает сервер