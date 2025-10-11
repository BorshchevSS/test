class RoleDescriptor:

    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __set__(self, instance, value):
        current_role = instance.current_role
        #instance экземпляр класса User
        if 'admin' in self.allowed_roles:
        # разрешаем изменение
            instance.__dict__[self.name] = value
            # self.name устанавливается в get как атрибут
        elif 'editor' in self.allowed_roles or 'viewer' in self.allowed_roles:
            raise PermissionError(f'Role {current_role}'
                                  f'cannot modify')
        else:
            raise PermissionError(f'Role {current_role}'
                                  f'cannot modify')

    def __get__(self, instance, owner):
        current_role = instance.current_role

        if current_role in self.allowed_roles:
            return instance.__dict__[self.name] #возвращаем значение атрибута
        raise PermissionError(f'Role {current_role} access denied')

    #для установки имени атрибута
    def __set_name__(self, owner, name):
        self.name = name #сохраняем имя атрибута

class User:
    #определяем атрибуты с конторлем доступа через дескриптор
    field1 = RoleDescriptor(allowed_roles=['admin','editor'])
    field2 = RoleDescriptor(allowed_roles=['admin'])
    field3 = RoleDescriptor(allowed_roles=['admin', 'viewer'])

    def __init__(self, role):
        self.current_role = role  #текущая роль
        #начальные значения аттрибутов
        self.field1 = 'default value field 1'
        self.field2 = 'default value field 2'
        self.field3 = 'default value field 3'

try:
    # admin_user = User('admin')
    # print(admin_user.field3)
    # admin_user.field3 = 'new value field 3'
    # print(admin_user.field3)

    viewer_user = User('editor')
    print(viewer_user.field3)
    viewer_user.field3= 'trying to modify' #доступ запрещен
    print(viewer_user.field3)

except PermissionError as e:
    print(e)

