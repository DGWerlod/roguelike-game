from img import images
from objects.actor import Actor

# Key: Width, Height, HP, Fire rate in ticks (1/60), Damage
data = {
    "apple": [3,40,1],
    "cherry": [1,20,1],
    "banana": [5,60,1],
    "peep": [15,60,2],
    "bunny": [1,60,1]
}

for e in data:
    data[e].insert(0, images.enemies[e].get_width())
    data[e].insert(1, images.enemies[e].get_height())

class Enemy(Actor):
    def __init__(self,name="enemy",spd=[0,0]):
        super().__init__(0,0,data[name][0],data[name][1],None,None,data[name][2],spd,name)
        self.atkSpd = data[name][3]
        self.attackCD = data[name][3]
        self.dmg = data[name][4]

    def setup(self):
        self.img = images.enemies[self.name]

    def go(self, ctx, room, target):
        super().go(ctx,room)
        if self.attackCD > 0:
            self.attackCD -= 1
            return None
        else:
            self.attackCD = self.atkSpd
            return self.attack(target)
