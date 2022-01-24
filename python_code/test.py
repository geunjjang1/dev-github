
class Unit:
    def __init__(self,name,hp): 
        self.name =name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self,name,hp,damage): 
        Unit.__init__(self,name,hp)
        self.damage = damage 
        print ("{0} 유닛이 생성되었습니다.".format(\
                self.name))

class flyable: 
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    #def fly(self,name,location): 
     #   print(f"{name},{location},{self.flying_speed}")

class flyableattackunit(AttackUnit,flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage) 
        flyable.__init__(self,flying_speed) 


valkyrie = flyableattackunit("발",200,6,5)
#:valkyrie.fly(valkyrie.name,"3")

