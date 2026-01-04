from design_system import (
    DesignSystemConfig,
    BootstrapFactory,
    MaterialFactory,
    FormBuilder,
    FormDirector
)
from form_renderer import render_web_form

config = DesignSystemConfig.get_instance()
config.set_factory(BootstrapFactory())
bootstrap_factory = config.get_active_factory()
builder = FormBuilder(bootstrap_factory)
director = FormDirector(builder)
bootstrap_login_form = director.build_login_form()
html_bootstrap = render_web_form(bootstrap_login_form)
with open('login_form.html', 'w', encoding='utf-8') as f:
    f.write(html_bootstrap)

config.set_factory(MaterialFactory())
material_factory = config.get_active_factory()
builder = FormBuilder(material_factory)
director = FormDirector(builder)
material_register_form = director.build_register_form()
html_material = render_web_form(material_register_form)
with open('register_form.html', 'w', encoding='utf-8') as f:
    f.write(html_material)