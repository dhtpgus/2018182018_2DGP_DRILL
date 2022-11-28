class Npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y


yuri = Npc('yuri', 100, 100)
print(yuri.__dict__)

yuri.__dict__['age'] = 30 # 예제 변수를 만드는 또하나의 방법
yuri.name, yuri.x, yuri.y = 'tom', 4, 5
new_data = {'name':'jeny', 'x':5, 'y':100, 'age':30}
yuri.__dict__.update(new_data)

print(yuri.name,yuri.x,yuri.y,yuri.age)