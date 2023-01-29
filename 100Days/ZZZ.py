class Person(object):

    # 限定Person對象只能綁定_name, _age和_gender屬性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飛行棋.' % self._name)
        else:
            print('%s(%s)正在玩鬥地主.' % (self._name, self._gender))


def main():
    person = Person('王大錘', 22)
    person._gender = '男'
    person.play()   
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True

if __name__ == '__main__':
    main()