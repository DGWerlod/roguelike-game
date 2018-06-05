files = ["constants.py", "generator.py", "main.py", "rooms.py",
         "controls/keyboard.py", "controls/mouse.py",
         "img/images.py",
         "logic/collisions.py", "logic/graphics.py", "logic/matrices.py",
         "objects/actor.py", "objects/boss.py", "objects/bullet.py", "objects/character.py", "objects/circle.py",
         "objects/door.py", "objects/enemy.py", "objects/entity.py", "objects/hud.py", "objects/item.py", "objects/minimap.py",
         "objects/obstruction.py", "objects/player.py", "objects/rect.py", "objects/spawner.py", "objects/teleporter.py",
         "sound/sounds.py"]

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

total = 0
for f in files:
    total += file_len(f)

print(str(total) + " lines")
