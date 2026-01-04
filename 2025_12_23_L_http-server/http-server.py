from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
                        #Создаем сервер, обработка запросов

class CustomHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><meta charset='utf-8'></head>
            <body>
            <p>Текущий путь {path}</p>
            <p>Время на сервере: {time}</p>
            </body>
            </html>
        """

        from datetime import datetime
        html_content = html_content.format(
            path=self.path,
            time=datetime.now().strftime("%Y-%m-%d")
        )

        # порядок отправки ответа
        self.send_response(200)
        self.send_header("Content-type", 'text/html, charset="utf-8"')
        #self.send_header("Content-type", 'text/play, charset="utf-8"')
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

server = HTTPServer(("", 8000), CustomHTTPHandler)
print("http://localhost:8000/")
server.serve_forever()


# MIME  -  типы
# self.send_header("Content-type", 'text/html, charset="utf-8"')
#                        text/html
# text, image, application, / plain, html, json, css, javascript

class c(BaseHTTPRequestHandler):
    self.requestline =  '"GET / HTTP/1.1" 200 -'
    self.command = "GET"
    self.path = "/index.html"
    self.headers = "Заголовки апросв"
    self.rfile = "Поток для чтения запроса"
    # Ответ (respons)
    self.wfile = "поток для записи ответа"
    self.
    self.

    #
class h(HTTPServer):
    server_address = (host, port)
    handler_class = "Класс обработчик"
    serve_forever = "Запускает бесконечный цикл обработки запросов"
    serve_close() = "корректно закроет сервер"