class A:
    # Variável de classe
    vc = 123

    def __init__(self):
        # Variável de instância
        self.vc = 321

a1 = A()
a2 = A()

a1.vc = 321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
print()

print(a1.vc, a2.vc, A.vc)
