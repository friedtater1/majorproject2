import pygame
import random



pygame.init()

screen1=pygame.display.set_mode((1200,1000))


class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
    def swap(self,new_image):
        self.image=new_image
    def scale(self,base):
        self.image=pygame.transform.scale(self.image,(((base.rect.x)*1.5),((base.rect.y)*1.5)))

class enemys(pygame.sprite.Sprite):
     def __init__(self,image,spot,health,attacklist,misclist,status_effect):
        super().__init__()
        self.image=image
        self.spot=spot
        self.health=health
        self.attacklist=attacklist
        self.misclist=misclist
        self.status_effect=status_effect
        self.rect=self.image.get_rect(center=spot)
     def attack(self,player,attack):
        if random.randint(1, 100)<=attack.hit_chance:
            player.health-=attack.damage
            if attack.status_effect!="none":
                player.status_effect=attack.status_effect

class text_display(pygame.sprite.Sprite):
    def __init__(self, size, rgb, message, midpoint, location,bg_button):
        super().__init__()
        font = pygame.font.SysFont('Lucida Sans', size)
        image = font.render(message, True, rgb)
        self.image = image
        if midpoint == 'center':
            self.rect = image.get_rect(center = location)
        elif midpoint == 'left':
            self.rect = image.get_rect(midleft = location)
        elif midpoint == 'right':
            self.rect = image.get_rect(midright = location)
        self.bg_button = bg_button
        self.bg_button.rect = self.bg_button.image.get_rect(center = location)
        self.bg_button.height = self.rect.height
        self.bg_button.width = self.rect.width

class player(pygame.sprite.Sprite):
     def __init__(self,spritesheet,spot,health,mp,weapons,equiped_weapon,items,offensivemagic,defensivemagic):
          super().__init__()
          self.spritesheet=spritesheet
          self.spot=spot
          self.health=health
          self.mp=mp
          self.weapons=weapons
          self.equiped_weapon=equiped_weapon
          self.items=items
          self.offensivemagic=offensivemagic
          self.defensivemagic=defensivemagic
          self.rect=self.spritesheet.get_rect(center=spot)
     def attack(self,enemy,crit):
            if random.randint(1, 100)>=self.equiped_weapon.crit_chance:
                enemy.health-=self.equiped_weapon.att*crit
            else:
                enemy.health-=self.equiped_weapon.att
     def usepotion(self,potion):
        if potion.item_type=="restore":
            if self.health<100:
                potion.heal(self)
                if self.health>100:
                    self.health=100
        elif potion.item_type=="buffattack":
            potion.buff(self)
        elif potion.item_type=="buffcrit":
            potion.buff(self)



class weapon(pygame.sprite.Sprite):
    def __init__(self, name, desc,image,type, att, crit_chance,spawn):
        super().__init__()
        self.name = name
        self.desc = desc
        self.image=image
        self.type=type
        self.att = att
        self.crit_chance = crit_chance #IN PERCENTAGE
        self.rect=self.image.get_rect(center=spawn)

axe=pygame.image.load("weaponimages/axe.png").convert()
diamondsword=pygame.image.load("weaponimages/diamondsword.png").convert_alpha()

allweapons={"diamondsword":weapon("Diamond Sword","OHHHHH DIAMONDS LETS GOOOOO",diamondsword,"attack",25,75,(0,0)),
            "axe":weapon("Axe","a useful tool for chopping wood, or in most of your cases, cutting down your enemies",axe,"attack",0.15,25,(0,0))}

class armour(pygame.sprite.Sprite):
    def __init__(self,name, desc, item_type,quantity,image,defense, spawn):
        super().__init__()
        self.name=name
        self.desc=desc
        self.item_type=item_type
        self.quantity=quantity
        self.image=image
        self.defense = defense
        self.rect=self.image.get_rect(center=spawn)

class restoreitem(pygame.sprite.Sprite):
    def __init__(self,name,image,type,price,stats,uses,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
        self.name=name
        self.type=type
        self.price=price
        self.stats=stats
        self.uses=uses
    def heal(self,player):
        player.health+=self.stats
    
class buffattackitem(pygame.sprite.Sprite):
    def __init__(self,name,image,price,type,stats,uses,duration,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.name=name
        self.price=price
        self.type=type
        self.stats=stats
        self.uses=uses
        self.duration=duration
        self.rect=self.image.get_rect(center=spawn)
    def buff(self,player):
        if self.uses>0:
            player.attack+=self.stats

class buffcrititem(pygame.sprite.Sprite):
    def __init__(self,name,image,price,type,stats,uses,duration,spawn):
        self.image=image
        self.spawn=spawn
        self.name=name
        self.price=price
        self.type=type
        self.stats=stats
        self.uses=uses
        self.duration=duration
        self.rect=self.image.get_rect(center=spawn)
    def buff(self,player):
        if self.uses>0:
            player.critchance+=self.stats

healthpotion=pygame.image.load("potionimages/redpotion.jpeg").convert_alpha()
attackbuff=pygame.image.load("potionimages/bluepotion.jpeg").convert_alpha()
critbuff=pygame.image.load("potionimages/rainbowpotion.png").convert_alpha()


allpotions={"healthpotion":restoreitem("Healing",healthpotion,"healing",25,50,1,(0,0)),
            "attackbuff":buffattackitem("Attackbuff",attackbuff,"buff",25,10,3,5,(0,0)),
            "critbuff":buffcrititem("Critbuff",critbuff,"buff",25,0.1,3,5,(0,0))}

class magic:
    def __init__(self, name, desc, cost,damage,hitchance,status_effect,status_effect_damage,timer,placeholdertimer):
        self.name = name
        self.desc = desc
        self.mp_cost = cost
        self.damage = damage
        self.hit_chance = hitchance
        self.status_effect = status_effect
        self.status_effect_damage = status_effect_damage
        self.timer = timer
        self.placeholdertimer = placeholdertimer
    def timerstarter(self,turn_counter):
        self.placeholdertimer=turn_counter
    def timercounter(self,turn_counter):
        if turn_counter-self.placeholdertimer>=self.timer:
            self.status_effect="none"
    def apply(self,player,enemy):
        if player.mp>=self.mp_cost:
            player.mp-=self.mp_cost
            if random.randint(1, 100)<=self.hit_chance:
                enemy.health-=self.damage
    def timercheck(self,enemy,turn_counter):
        if enemy.status_effect!="none":
            self.timercounter(turn_counter)
    

def enemydesignation(x,offensivetypedictionary,defensivetypedictionary,enemy):
    if x==1:
        enemy.attacklist.append(offensivetypedictionary["slash"])
        enemy.misclist.append(offensivetypedictionary["boost"])
    elif x==2:
        enemy.attacklist.append(defensivetypedictionary["debuff"])
        enemy.misclist.append(defensivetypedictionary["heal"])

def enemyturn(enemylist,player,enemyturncounter,choice):
    for x in range(len(enemylist)):
        focusenemy=random.randint(0,len(enemylist)-1)
        enemy=enemylist[focusenemy]
        if choice==1:
            if enemy.health>0:
                if random.randint(1, 100)<=50:
                    enemy.attack(player,random.choice(enemy.attacklist))
                    enemyturncounter+=1
        elif choice==2:
            if enemy.health>0:
                random.choice(enemy.misclist).apply(enemy,player)
    for x in enemy.attacklist:
        x.timercheck(player,enemyturncounter)
    for x in enemy.misclist:
        x.timercheck(enemy,enemyturncounter)
    





Offensiveattackdictionary={"slash":magic("Slash","A basic slash attack",10,"offensive",15,"bleed"),
                             "stab":magic("Stab","A basic stab attack",10,"offensive",10,"poison")}
Defensiveattackdictionary={"debuff":magic("Debuff","A basic debuff attack",10,"defensive",0,"slow"),
                            "heal":magic("Heal","A basic heal attack",10,"defensive",50,"regen")}

allmagic={"fireball":magic("Fireball","A basic fireball attack",10,25,80,"burn",5,5),
          "iceblast":magic("Ice Blast","A basic ice blast attack",10,10,65,"freeze",15,3),
          "lightning":magic("Lightning","A basic lightning attack",10,20,55,"shock",10,2)}

def spelltypecheck(magic,player):
    if magic.magic_type=="offensive":
        player.attacklist.append(magic)
    elif magic.magic_type=="defensive":
        player.misclist.append(magic)

def inventorycheck(dictw,dicti,dictm,player):
    templistw=0
    templisti=0
    templistm=0
    with open("weaponlist.txt","r") as f:
        templistw=(f.readline()).split(",")
    with open("inventory.txt","r") as f:
        templisti=(f.readline()).split(",")
    with open("magiclist.txt","r") as f:
        templistm=(f.readline()).split(",")
    for x in templistw:
        if x in dictw:
            player.weapons.append(dictw[x])
    for x in templisti:
        if x in dicti:
            player.items.append(dicti[x])
    for x in templistm:
        if x in dictm:
            player.magics.append(dictm[x])
def background():
    screen1.blit(backing,(0,0))
    pg.draw(screen1)
    enemy.draw(screen1)

def selectmenu(enemylist,player):
    basemenu=pygame.sprite.Group()
    attack=button(pygame.image.load("componentscomb/attackmenu.png").convert(), (300,500))
    item=button(pygame.image.load("componentscomb/itemmenu.png").convert(), (700,500))
    healthtrackplayer=button(pygame.image.load("componentscomb/healthtrackmenu.png").convert(), (500,500))
    healthtrackenemy=button(pygame.image.load("componentscomb/healthtrackmenu.png").convert(), (500,300))

    for x in enemylist:
        if x.health<=0:
            enemylist.remove(x)
    
    
    

    basemenu.add(attack)
    basemenu.add(item)
    basemenu.add(healthtrackplayer)
    basemenu.add(healthtrackenemy)
    basemenu.draw(screen1)


def combatmenu(x):
    if x==1:
        actionm.swap(pygame.image.load("componentscomb/attackmenu.png").convert())
    elif x==2:
        actionm.swap(pygame.image.load("componentscomb/magicmenu.png").convert())
    elif x==3:
        actionm.swap(pygame.image.load("componentscomb/itemmenu.png").convert())
    elif x==4:
        actionm.swap(pygame.image.load("componentscomb/runmenu.png").convert())

backing=pygame.image.load("componentschar/grass.jpeg").convert()
backing=pygame.transform.scale(backing,(1200,1000))





zombie1=pygame.image.load("componentschar/zombie.png").convert_alpha()
hitsound=pygame.mixer.Sound("soundeff/sword.mp3")

man=pygame.image.load("componentschar/char_left.png").convert()
actionmenu=pygame.image.load("componentscomb/actionmenu.png").convert()
healthtrack=pygame.image.load("componentscomb/healthtrackmenu.png").convert()

pygame.mixer.music.load("music/dummy.mp3")
pygame.mixer.music.play(loops=-1)

#list of all potential spots for enemies to spawn in combat
spawnlistenemy=[(250,350),(250,450),(250,250),(150,350)]

pg=pygame.sprite.Group()
enemy=pygame.sprite.Group()
dude=player(man,(800,350))
erm=enemys(zombie1,(250,350))




menu=pygame.sprite.Group()
actionm=button(actionmenu,(300,500))
healthm=button(healthtrack,(600,500))
menu.add(actionm)
menu.add(healthm)
enemy.add(erm)
pg.add(dude)


#crit is a constant multiplier for critical hits, set to 2 for double damage
crit=2


gameactive = True
while gameactive:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                hitsound.play()
            elif event.button==3:
                gameactive = False


    
    background()
    menu.draw(screen1)
    
    pygame.display.update()
    pygame.time.Clock().tick(60)

