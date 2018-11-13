from objects.enemy import Enemy

class Spawner(Enemy):
    def __init__(self,name="enemy",spawnSpd=120,maxChildren=1,spd=[0,0]):
        super().__init__(name,spd)
        self.spawnSpd = spawnSpd
        self.spawnCD = self.spawnSpd//2
        self.isSterile = False
        self.childCount = maxChildren

    def setup(self):
        super().setup()

    def go(self, ctx, room, target):
        if not self.isSterile:
            if self.spawnCD > 0:
                self.spawnCD -= 1
            else:
                self.spawnCD = self.spawnSpd
                self.childCount -= 1
                if self.childCount == 0:
                    self.sterilize()
        return super().go(ctx,room,target)

    def sterilize(self):
        self.isSterile = True
