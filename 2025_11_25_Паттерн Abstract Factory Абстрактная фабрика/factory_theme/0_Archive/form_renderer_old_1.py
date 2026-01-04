from jinja2 import Environment, FileSystemLoader
from design_system import WebForm, DesignSystemConfig

def render_web_form(web_form, WebForm,template_name="form.html")
    file_loader = Environment(".") # ищем в текущей директории
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    css_link = web_form.theme_css_link
    render_html = template.render(

    )