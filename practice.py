fruit = ["apple", "banana", "orange"]
car = ["porsche", "sonata", "altima"]

print(list(zip(fruit, car)))

mixed = [('apple', 'porsche'), ('banana', 'sonata'), ('orange', 'altima')]
print(list(zip(*mixed)))

fruit2, car2 = zip(*mixed)
print(fruit2)
print(car2)