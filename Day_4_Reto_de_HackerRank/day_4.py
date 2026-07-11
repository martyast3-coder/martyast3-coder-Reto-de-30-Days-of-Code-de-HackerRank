class Person:
    def __init__(self, initialAge):
        # Validar si la edad inicial es negativa
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        # Evaluar la edad actual e imprimir el mensaje correcto./.
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Incrementar la edad en 1
        self.age += 1

t = int(input())