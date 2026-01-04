from abc import ABC, abstractmethod

# Abstract products (UI)
class Button(ABC):
    def __init__(self, label):
        self.label = label

    @abstractmethod
    def render(self):
        pass

class Input(ABC):
    def __init__(self, label):
        self.label = label

    @abstractmethod
    def render(self):
        pass

# Concreate Products
class BootstrapButton(Button):
    def render(self):
        return {
            'type': 'submit_button',
            'label': self.label,
            'css_class': 'btn btn-primary',
        }

class BootstrapInput(Input):
    def render(self):
        return {
            'type': 'input',
            'label': self.label,
            'css_class': 'form-control',
        }

class MaterialButton(Button):
    def render(self):
        return {
            'type': 'submit_button',
            'label': self.label,
            'css_class': 'waves-effect waves-light btn',
        }

class MaterialInput(Input):
    def render(self):
        return {
            'type': 'input',
            'label': self.label,
            'css_class': '',
        }

# Abstract Factory
class ThemeFactory(ABC):
    @abstractmethod
    def create_button(self, label):
        pass
    @abstractmethod
    def create_input(self, label):
        pass

# Concreate Factories
class BootstrapFactory(ThemeFactory):
    def create_button(self, label):
        return BootstrapButton(label)
    def create_input(self, label):
        return BootstrapInput(label)

class MaterialFactory(ThemeFactory):
    def create_button(self, label):
        return MaterialButton(label)
    def create_input(self, label):
        return MaterialInput(label)

# Product (builder)
class WebForm:
    def __init__(self, theme_css_link):
        self.components = []
        self.theme_css_link = theme_css_link

    def add_components(self, component_data):
        self.components.append(component_data)

# Builder
class FormBuilder:
    def __init__(self, factory: ThemeFactory):
        self.factory = factory
        config = DesignSystemConfig.get_instance()
        self.form = WebForm(config.get_css_link()) # css передать

    def get_form(self):
        return self.form

    def add_title(self, text):
        self.form.add_components({'type': 'title',
                                  'label': text})
    def add_input(self, label):
        input_component = self.factory.create_input(label)
        self.form.add_components(input_component.render())
    def add_submit_button(self, label):
        button_component = self.factory.create_button(label)
        self.form.add_components(button_component.render())

# Director
class FormDirector:
    def __init__(self, builder: FormBuilder):
        self.builder = builder

    def build_login_form(self):
        self.builder.add_title('Вход в систему')
        self.builder.add_input('Email')
        self.builder.add_input('Пароль')
        self.builder.add_submit_button('Войти')
        return self.builder.get_form()

    def build_register_form(self):
        self.builder.add_title('Регистрация')
        self.builder.add_input('Username')
        self.builder.add_input('Email')
        self.builder.add_input('Пароль')
        self.builder.add_submit_button('Зарегистрироваться')
        return self.builder.get_form()

# Singleton
class DesignSystemConfig:
    _instance = None
    BOOTSTRAP_CSS = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">'
    MATERIAL_CSS = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">'

    def __init__(self):
        if DesignSystemConfig._instance is not None:
            raise Exception('используйте get_instance()')
        self._active_factory = BootstrapFactory()
        self._css_link = self.BOOTSTRAP_CSS

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DesignSystemConfig.__new__(cls)
            cls._instance.__init_internal()
        return cls._instance

    def __init_internal(self):
        # внутренняя инициализация для обхода проверки в __init__
        self._active_factory = BootstrapFactory()
        self._css_link = self.BOOTSTRAP_CSS

    def set_factory(self, factory):
        # переключение активной фабрики
        self._active_factory = factory
        if isinstance(factory, BootstrapFactory):
            self._css_link = self.BOOTSTRAP_CSS
        elif isinstance(factory, MaterialFactory):
            self._css_link = self.MATERIAL_CSS
        else:
            self._css_link = '' #если тема неизвестна

    def get_active_factory(self):
        return self._active_factory

    def get_css_link(self):
        return self._css_link