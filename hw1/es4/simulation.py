import random
for i in range(100000):
    value=0
    for i in range(200):
        value+=random.randint(160,190)
    value/=200
    if value<=170 or value>=180:
        print(value)