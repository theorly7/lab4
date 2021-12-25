import random

class TitansItTheWalls:
    level = 1

    def __init__(self):
        self.hp = 50000
        self.damage = 0
        self.speed = 0
        self.height = 50
        self.pain = 0
        self.intellect = 0
        self.aggression = 0
        self.jump = 0

    def status(self):
        status = ['Zzz...']
        return status

class ThreetoFiveMeterTitanium:

    def __init__(self):
        self.hp = 1000
        self.damage = 125
        self.speed = 15
        self.height = random.randrange(3, 5, 1)
        self.pain = 0
        self.intellect = 1
        self.aggression = 80
        self.jump = 0

    def attack(self):
        print('KILL!')
        return f'3-5 Meter Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        return f'3-5 Meter Titanium get {damage} damage \n Current hp: {self.hp}'

    def status(self, sunlight):
        if sunlight == False:
            status = ['Zzz...']
        else:
            status = ['Aww...']
        return status

class SeventoTenMeterTitanium:

    def __init__(self):
        self.hp = 1000
        self.damage = 250
        self.speed = 30
        self.height = random.randrange(7, 10, 1)
        self.pain = 0
        self.intellect = 1
        self.aggression = 100
        self.jump = 0
        self.order = 0

    def attack(self):
        print('KILL!')
        return f'7-10 Meter Titanium attacked with {self.damage} damage'


    def get_damage(self, damage):
        self.hp -= damage
        return f'7-10 Meter Titanium get {damage} damage \n Current hp: {self.hp}'

    def status(self, sunlight):
        if sunlight == False:
            status = ['Zzz...']
        else:
            status = ['Aww...']
        return status

class FourteentoFifteenMeterTitanium:

    def __init__(self):
        self.hp = 1000
        self.damage = 400
        self.speed = 60
        self.height = random.randrange(14, 15, 1)
        self.pain = 0
        self.intellect = 1
        self.aggression = 80
        self.jump = 0

    def attack(self):
        print('KILL!')
        return f'14-15 Meter Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        return f'14-15 Meter Titanium get {damage} damage \n Current hp: {self.hp}'

    def status(self, sunlight):
        if sunlight == False:
            status = ['Zzz...']
        else:
            status = ['Aww...']
        return status

class CommonTitanium(ThreetoFiveMeterTitanium, SeventoTenMeterTitanium,
FourteentoFifteenMeterTitanium):
    level = 2

    def __init__(self):
        ThreetoFiveMeterTitanium.__init__(self)
        SeventoTenMeterTitanium.__init__(self)
        FourteentoFifteenMeterTitanium.__init__(self)

class Abnormal:
    level = 3

    def __init__(self):
        self.hp = 2000
        self.damage = 500
        self.speed = 100
        self.height = random.randrange(3, 15, 1)
        self.pain = 0
        self.intellect = 15
        self.aggression = 80
        self.jump = 70

    def attack(self):
        print('KILL!')
        return f'Abnormal Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        return f'Abnormal Titanium get {damage} damage \nCurrent hp: {self.hp}'

    def status(self, sunlight):
        if sunlight == False:
            status =['Zzz...']
        else:
            status =['Aww...']
        return status

class Deviant:
    level = 4

    def __init__(self):
        self.hp = 3000
        self.damage = 600
        self.speed = 60
        self.height = random.randrange(3, 7, 1)
        self.pain = 0
        self.intellect = 30
        self.aggression = 80
        self.jump = 80

    def attack(self):
        print('KILL!')
        return f'Deviant Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        return f'Deviant Titanium get {damage} damage \nCurrent hp: {self.hp}'

    def status(self, sunlight):
        if sunlight == False:
            status = ['Zzz...']
        else:
            status = ['Aww...']
        return status

class CollosalTitanium:

    def __init__(self):
        self.hp = 10000
        self.damage = 1500
        self.speed = 120
        self.height = 60
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 0

    def attack(self):
        print('I will kill you!')
        return f'Collosal Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Collosal Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class ArmoredTitanium:

    def __init__(self):
        self.hp = 30000
        self.damage = 800
        self.speed = 120
        self.height = 15
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 30

    def attack(self):
        print('I will kill you!')
        return f'Armored Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Armored Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class BestialTitanium:

    def __init__(self):
        self.hp = 7000
        self.damage = 600
        self.speed = 70
        self.height = 17
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 30

    def attack(self):
        print('I will kill you!')
        return f'Bestial Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Bestial Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class HammerTitanium:

    def __init__(self):
        self.hp = 6000
        self.damage = 900
        self.speed = 70
        self.height = 14
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 20

    def attack(self):
        print('I will kill you!')
        return f'Hammer Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Hammer Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class EffiminateTitanium:

    def __init__(self):
        self.hp = 6000
        self.damage = 800
        self.speed = 70
        self.height = 14
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 40

    def attack(self):
        print('I will kill you!')
        return f'Effiminate Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Effiminate Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'Her agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class AttackingTitanium:

    def __init__(self):
        self.hp = 8000
        self.damage = 900
        self.speed = 70
        self.height = 15
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 40

    def attack(self):
        print('I will kill you!')
        return f'Attacking Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Attacking Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class ToothyTitanium:

    def __init__(self):
        self.hp = 4000
        self.damage = 600
        self.speed = 40
        self.height = 5
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 100

    def attack(self):
        print('I will kill you!')
        return f'Toothy Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Toothy Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class CarrierTitanium:

    def __init__(self):
        self.hp = 3000
        self.damage = 200
        self.speed = 30
        self.height = 5
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 40

    def attack(self):
        print('I will kill you!')
        return f'Carrier Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Carrier Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class ProginatorTitanium:

    def __init__(self):
        self.hp = 8000
        self.damage = 900
        self.speed = 70
        self.height = 15
        self.pain = 0
        self.intellect = 100
        self.aggression = 10
        self.jump = 40
        self.order = 0

    def attack(self):
        print('I will kill you!')
        return f'Proginator Titanium attacked with {self.damage} damage'

    def get_damage(self, damage):
        self.hp -= damage
        self.aggression += 10
        return f'Proginator Titanium get {damage} damage \nCurrent hp: {self.hp} \n' \
               f'His agression upped to {self.aggression}'

    def status(self):
        status = ['I\'m active!']
        return status

class PeopleTitans(CollosalTitanium, ArmoredTitanium, AttackingTitanium, HammerTitanium,
EffiminateTitanium, CarrierTitanium, ToothyTitanium, BestialTitanium, ProginatorTitanium):
    level = 5

    def __init__(self):
        CollosalTitanium.__init__(self)
        ArmoredTitanium.__init__(self)
        AttackingTitanium.__init__(self)
        HammerTitanium.__init__(self)
        EffiminateTitanium.__init__(self)
        CarrierTitanium.__init__(self)
        ToothyTitanium.__init__(self)
        BestialTitanium.__init__(self)
        ProginatorTitanium.__init__(self)

CommonTitaniumLow = ThreetoFiveMeterTitanium()
CommonTitaniumMedium = SeventoTenMeterTitanium()
CommonTitaniumHigh = FourteentoFifteenMeterTitanium()
CommonTitanium = CommonTitanium()
TitansItTheWalls = TitansItTheWalls()
Abnormal = Abnormal()
Deviant = Deviant()
Collosal = CollosalTitanium()
Armored = ArmoredTitanium()
Hammer = HammerTitanium()
Effiminate = EffiminateTitanium()
Carrier = CarrierTitanium()
Toothy = ToothyTitanium()
Bestial = BestialTitanium()
Proginator = ProginatorTitanium()
Attacking = AttackingTitanium()
PeopleTitans = PeopleTitans()
print(Abnormal.get_damage(100))
print(Effiminate.get_damage(1000))
print(Attacking.status())
print(CommonTitaniumHigh.attack())

a = [CommonTitanium, TitansItTheWalls, Abnormal, Deviant, PeopleTitans]


max_level = 0
for titans in a:
    if titans.level > max_level:
        max_level = titans.level
print(f'Titan\'s max level is {max_level}')


















