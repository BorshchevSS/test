from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

template_env = Environment(loader=FileSystemLoader('templates'))

from db import get_all_authors, get_author_detail, get_all_books, get_all_genres, create_database

def render_template(template_name, context={}):
    template = template_env.get_template(template_name)
    return template.render(context).encode("utf-8")

class LibraryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        if path.startswith('/static/'):
            self.send_static(path) #Прописать css js
            return
        content = None
        status_code = 200
        try:
            if path == "/" or path == '/authors':
                authors = get_all_authors() # todo: Прописать bd
                content = render_template("authors.html", {'authors': authors})
            elif path.startswith('/author/'):
                try:
                    author_id = int(path.split('/')[-1])
                    author = get_author_detail(author_id) # todo: Прописать bd
                    if author:
                        content = render_template('author_detail.html', {'author': author})
                    else:
                        status_code = 404
                        content = render_template('404.html', {'massage': 'Автор не найден'})
                except ValueError:
                    status_code = 400
                    content = render_template('404.html', {'massage': 'Некорректный ID автора'})
            elif path == '/books':
                books = get_all_books() # todo: Прописать bd
                genres = get_all_genres() # todo: Прописать bd
                content = render_template('books.html', {'books': books, 'genres': genres})
            else:
                status_code = 404
                content = render_template('404.html', {'massage': 'Страница не найдена'})
        except Exception as e:
            print(f"Ошибка при обработки запроса: {e}")
            status_code = 500
            content = render_template('500.html', {'error': str(e)})
        self.send_response(status_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        if content:
            self.wfile.write(content.encode("utf-8"))

    def send_static(self, path):
        file_path = path[1:]
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            if file_path.endswith('.css'):
                mime_types = 'text/css'
            elif file_path.endswith('.js'):
                mime_types = "application/javascript"
            else:
                mime_types = "application/octet-stream"

            self.send_response(200)
            self.send_header('Content-type', mime_types)
            self.send_header('Content-length', len(content))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, f'Файл не найден: {path}')


