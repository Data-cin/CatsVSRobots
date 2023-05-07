from classes.Decoration import Decoration
from classes.Water import Water
from classes.Exit import Exit
from classes.ItemBox import ItemBox
# classe world com método que recebe os dados dos arquivos csv e desenha os niveis de acordo com as informaçoes
class World():
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data, img_list, TILE_SIZE, water_group, decoration_group, \
                      Soldier, HealthBar, enemy_group, item_boxes, item_box_group, exit_group):
        self.level_length = len(data[0])
        #iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE)
                        water_group.add(water)
                    elif tile >= 11 and tile <= 14:
                        decoration = Decoration(img, x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 15: #create player
                        player = Soldier('player', x*TILE_SIZE, y*TILE_SIZE, 2.2, 5, 20, 10)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 16:
                        enemy = Soldier('enemy', x*TILE_SIZE, y*TILE_SIZE, 1.65, 2, 20)
                        enemy_group.add(enemy) 
                    elif tile == 17:#create ammo box
                        item_box = ItemBox('Ammo', x*TILE_SIZE, y*TILE_SIZE, item_boxes, TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 18:#create grenade box
                        item_box = ItemBox('Grenade', x*TILE_SIZE, y*TILE_SIZE, item_boxes, TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 19:#create health box
                        item_box = ItemBox('Health', x*TILE_SIZE, y*TILE_SIZE, item_boxes, TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 20:#create exit
                        exit = Exit(img, x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE)
                        exit_group.add(exit)
        return player, health_bar
    
    def draw(self, screen_scroll, screen):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])