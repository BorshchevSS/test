from jinja2 import Environment, FileSystemLoader
from design_system import WebForm

def render_web_form(web_form: WebForm, template_name='form.html'):
    file_loader = FileSystemLoader('.') # ищем в текущей директории
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    css_link = web_form.theme_css_link
    render_html = template.render(
        components=web_form.components,
        css_link=css_link
    )
    return render_html