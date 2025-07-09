class Dog:
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind

    def bark(self):
        print(f"{self.name}가 멍멍 짖어요!")

    def sit(self):
        print(f"{self.kind}는 앉기도 잘해요")

    def bite(self):
        print(f"{self.name}는 잘 물어요")


my_dog = Dog("망고", 3, "푸들")
my_dog.bark()

your_dog = Dog("지호", 17, "진돗개")
your_dog.sit()

jiho_dog = Dog("지호", 17, "진돗개")
your_dog.bite()