from utils import get_data

data = [list(i) for i in get_data('in.txt')]
start = (0, 0)

energized = set()

char_map = {
    (0,1): '>',
    (0,-1): '<',
    (1,0): 'V',
    (-1,0): '^',
}

def print_grid(p, xx, yy):
    global data, char_map
    xi, yi = p
    for i in range(len(data)):
        for j in range(len(data[0])):
            if (i, j) == p:
                ch = char_map[(xx,yy)]
                print(ch, end='')
            else:
                print(data[i][j], end='')
        print()
    print()

splits = set()

def move_beam(pos, d):
    x,y = pos
    dx,dy = d
    while x >= 0 and x < len(data) and y < len(data[0]) and y >= 0:
        piece = data[x][y]
        energized.add((x,y))
        #print_grid((x,y), dx, dy)
        match piece:
            case '.':
                x += dx
                y += dy
            case '|':
                if dx in (-1, 1):
                    x += dx
                    y += dy
                else:
                    if (x,y) not in splits:
                        splits.add((x,y))
                        print(f'Split Verically {(x,y)}')
                        move_beam((x+1, y), (1, 0))
                        move_beam((x-1, y), (-1, 0))
                    return
            case '-':
                if dy in (-1, 1):
                    x += dx
                    y += dy
                else:
                    if (x,y) not in splits:
                        print(f'Split Horzi {(x, y)}')
                        splits.add((x,y))
                        move_beam((x, y+1), (0, 1))
                        move_beam((x, y-1), (0, -1))
                    return
            case '\\':
                if dx == -1:
                    dx = 0
                    dy = -1
                elif dx == 1:
                    dx = 0
                    dy = 1
                elif dy == -1:
                    dx = -1
                    dy = 0
                elif dy == 1:
                    dx = 1
                    dy = 0
                x += dx
                y += dy
            case '/':
                if dx == -1:
                    dx = 0
                    dy = 1
                elif dx == 1:
                    dx = 0
                    dy = -1
                elif dy == -1:
                    dx = 1
                    dy = 0
                elif dy == 1:
                    dx = -1
                    dy = 0
                x += dx
                y += dy

move_beam(start, (0, 1))
print(len(energized))