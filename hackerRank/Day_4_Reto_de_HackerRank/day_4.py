class Person:
    def __init__(self, initialAge):
        # Verifica que la edad no sea negativa
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        # Imprime el mensaje correspondiente según la edad
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Incrementa la edad en 1
        self.age += 1

age = int(input("Digite la edad: "))
p = Person(age)
p.amIOld()
for j in range(0, 3):
    p.yearPasses()
p.amIOld()
print("")