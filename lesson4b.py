motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print(motorcycles[1])
print(motorcycles[0])
print(motorcycles[2])

motorcycles[0] = 'Hero'
print(motorcycles)

fruits = []
fruits.append('orange')
fruits.append('mango')
fruits.append('banana')
print(fruits)

fruits.insert(1,'apple')
print('After Sort  :')
fruits.sort()

print('After Remove :')
fruits.remove('apple')
print(fruits)
