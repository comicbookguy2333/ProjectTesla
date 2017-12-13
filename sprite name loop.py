sprite_num = 1
def add():
    global sprite_num
    sprite_num=sprite_num+1
    spritestr=str(sprite_num)
    print("class "+spritestr+"box(pygame.sprite.Sprite):")
    add1=input("add?")
    add1 = int(add1)
    if add1==1:
        add()
add()