class ClassTest:
    def instance_method(self):
        print(f'Called instance method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called class method {cls}')

    @staticmethod
    def static_method():
        print(f'Call static method.')


ClassTest.class_method()
ClassTest.static_method()
