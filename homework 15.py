#Narek

import math
   
def nums(n):
    my_num = 0
    for i in range(1, n+1):
        digits = 1
        current_num = i
        while current_num / 10 > 1:
            digits+=1
            current_num=current_num/10
        my_num = my_num * (10 ** digits) + i
    return my_num
print(nums(13))

#Ruben

class Weapon:
    def __init__(self,name,damage,we_range):
        self.name = name
        self.damage = damage
        self.we_range = we_range
        
    def hit(self,actor,target):
        if target.is_alive():
            actor_coords = actor.get_coords()
            target_coors = target.get_coords()
            if self.we_range < ((actor_coords[0] - target_coors[0]) ** 2 + (actor_coords[1] - target_coors[1]) ** 2) ** 0.5:
                print(f"target is too far for weapon {self.name}")
            else:
                print(f"enemy was hit from weapon {self.name} , damage is {self.damage}")
            target.get_damage(self.damage)
        
        else:
            print("the enemy is already defeated")
    def __str__(self):
        return self.name
            
class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y = pos_x, pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return bool(self.hp)

    def get_damage(self, amount):
        if self.hp <= amount:
            self.hp = 0
        else:
            self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y
    
class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.current_weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.current_weapon.hit(self, target)
        else:
            print("i can hit only main hero")

    def __str__(self):
        return f"enemy is in the position ({self.pos_x,self.pos_y}) with weapon {self.current_weapon}"
class MainHero(BaseCharacter): 
    def __init__(self, pos_x, pos_y, name, hp):
        self.name = name
        self.weapon = []
        self.max_hp = 200
        super().__init__(pos_x, pos_y, hp)

    def hit(self, target):
        if isinstance(target, BaseEnemy):
            if len(self.weapon) == 0:
                print("i am unarmed")
            else:
                self.weapon[0].hit(self, target)
        else:
            print("i can hit only enemy")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon.append(weapon)
            print(f"picked up {weapon}")
        else:
            print("it’s not a Weapon")

    def next_weapon(self):
        if len(self.weapon) > 1:
            self.weapon.append(self.weapon.pop(0))
            print(f"i take weapon {self.weapon[0]}")
        elif len(self.weapon) == 1:
            print("i have one weapon")
        else:
            print("i am unarmed")

    def heal(self, amount):
        if self.hp + amount >= self.max_hp:
            self.hp = 200
        else:
            self.hp += amount
        print(f"now my health is hp {self.hp}")
        
weapon1 = Weapon("mech",5,1)
weapon2 = Weapon("erkar mech",7,2)
weapon3 = Weapon('luk',3,10)
weapon4 = Weapon('pushka',1000,1000)
princess = BaseCharacter(100,100,100)
archer = BaseEnemy(50,50,weapon3,100)
armored_swordsman = BaseEnemy(10,10,weapon2,500)
archer.hit(armored_swordsman)
armored_swordsman.move(10,10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0,0,"artur",200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)