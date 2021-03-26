import yaml
class Animal:
    # def __init__(self):
    #     self.name:str
    #     self.color:str
    #     self.age:str
    #     self.gender:str

    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    def voice(self):
        print("会叫")

    def run(self):
        print("会跑")

class Cat(Animal):
    def __init__(self,name,color,age,gender):
        self.hair="短毛"
        super().__init__(name,color,age,gender)

    def cat_mouse(self,something):
        return f"抓到了{something}"

    def voice(self):
        print("卖萌,喵喵叫")

class Dog(Animal):
    def __init__(self,name,color,age,gender):
        self.hair="长毛"
        super().__init__(name,color,age,gender)

    def watch(self):
        print("会看家")

    def vioce(self):
        print("汪汪叫")


if __name__ == '__main__':

    cat=Cat(name="小喵",color="黑色",gender="雌性",age="2岁")
    print(f"{cat.name}是一只{cat.color}的{cat.gender}的{cat.hair}猫,今年{cat.age},今天终于{cat.cat_mouse('老鼠')}")

    print("*******************************************")

    dog=Dog("小汪","黄色","1岁","雄性")
    dog.watch()
    print(dog.name,dog.color,dog.age,dog.gender,dog.hair)


with open("./animals.yaml",encoding='utf-8') as f:
    str1=yaml.safe_load(f)
    print(str1)
    f.close()