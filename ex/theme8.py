class Transformer():
    def __init__(self, name):
        self.name = name

    def run(self):
        print('Run')
    
    def fire(self):
        print('Boom')

transformer = Transformer('Name')
transformer.fire()
print(transformer.name)

class Autobot(Transformer):
    def __init__(self, name, prime_status):
        super().__init__(name)
        self.prime_status = prime_status

    def fire(self):
        print('Kaboom')
    


autobot = Autobot('Bamblbee', False)
autobot.fire()

class Decepticon(Transformer):
    def transform(self, object):
        print(f'Transformed to {object}')


dec = Decepticon('Shokweiv')
dec.transform('tank')
dec.fire()
dec.run()
print(dec.name)

class Person():
    def __init__(self, name, age, hp, ksr):
        self.name = name
        self.age = age
        self.hp = hp
        self.ksr = ksr # KFC spawn rate
    
    def spawn(self):
        print('Я родился')
    
    def kick(self):
        ''' Скажет Smash! '''
        print('Smash!')
    
person1 = Person('Димас', 13, 5, 100)
print(f'Меня зовут {person1.name}, мне {person1.age}')
person1.spawn()

class Student(Person):
    def __init__(self, name, age, hp, ksr, war_ticket):
        super().__init__(name, age, hp, ksr)
        self.war_ticket = war_ticket

    def go_to_remi(self):
        print('Я пошёл в РЕМИ')
    
    def say_my_name(self):
        print(self.name)

class Teacher(Person):
    def oscarb(self, student):
        print(f'{student.name} придёшь ко мне после пары 💕')
    
    def kick(self):
        ''' Скажет что ты отчислен '''
        print('Отчислен')


student1 = Student('Игорь', 19, 2, 1, True)

teacher1 = Teacher('Олег', 45, 10, 3)

teacher1.oscarb(student1)
teacher1.kick()

import random

teams = ['white', 'blue', 'red']
heroes = []

white_soldiers = []

blue_soldiers = []

red_soldiers = []

class Unit():
    def __init__(self, team):
        self.id = random.randint(0, 1000000)
        self.team = team

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f'Герой из команды {self.team} повысел уровень')

class Soldier(Unit):
    def follow(self, hero):
        print(f'Солдат с номером {self.id} следует за героем с номером {hero.id}')


for team in teams:
    heroes.append(Hero(team))

for i in range(100):
    team = random.choice(teams)

    match team:
        case 'white':
            white_soldiers.append(Soldier(team))
        case 'blue':
            blue_soldiers.append(Soldier(team))
        case 'red':
            red_soldiers.append(Soldier(team))

white_length = len(white_soldiers)
blue_length = len(blue_soldiers)
red_length = len(red_soldiers)

max_team = max(white_length, blue_length, red_length)

for i, team in enumerate((white_soldiers, blue_soldiers, red_soldiers)):
    team_length = len(team)
    if team_length == max_team:
        heroes[i].level_up()

blue_soldiers[10].follow(heroes[1])
