class SingletonMeta(type):
    #Метакласс - класс для классов(экземпляр метакласса - класс(Detector))

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args,**kwargs)
        return  cls._instance

class Detector(metaclass=SingletonMeta):
    count = 0

    def __init__(self):
        self.count += 1

if __name__ == '__main__':

    d1=Detector()
    d2=Detector()
    assert id(d1) == id(d2)
    print(f'd1: {d1.count}\n'
          f'd2: {d2.count}')
    if id(d1) == id(d2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")