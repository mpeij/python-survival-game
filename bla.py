objects = [
    [2, 5, "bla"],
    [3, 8, "blabla"]
]
player_x = int(input())
player_y = int(input())

def check_terrain():
    for object in objects:
        #TODO: Stop when found
        if object[0] == player_x and object[1] == player_y:
            draw_terrain(object)
        else:
            #generate_terrain(player_x, player_y)
            pass

def draw_terrain(object):
    print(object[0])
    print(object[1])
    print(object[2])

check_terrain()