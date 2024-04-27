import random
from tkinter import *


class CellType:
    EMPTY = ' '
    TREE = 'T'
    WATER = 'W'
    FIRE = 'F'
    STRONG_FIRE = 'S'


class Icons:
    HELLICOPTER = "./assets/helli_s.png"
    TREE = "./assets/tree_s.png"
    WATER = "./assets/water_s.png"
    EMPTY = "./assets/empty_s.png"
    FIRE = "./assets/fire_s.png"
    CROSS = "./assets/cross_s.png"


class HellCopter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.has_water = False


class Field:
    def __init__(self, width, height, forest_proba=0.4):
        self.width = width
        self.height = height
        self.field = self.generate_field(
            width, height, forest_proba
        )
        self.hellcopter = HellCopter()
    
    @staticmethod
    def generate_field(width, height, forest_proba):
        field = [[CellType.EMPTY for _ in range(width)] for _ in range(height)]

        # generate river
        river_cur = (random.randint(0, height - 1), 0)
        while (0 <= river_cur[0] < height) and (0 <= river_cur[1] < width):
            field[river_cur[0]][river_cur[1]] = CellType.WATER
            direction_bottom = random.random() >= 0.5
            if direction_bottom:
                river_cur = (river_cur[0] + 1, river_cur[1])
            else:
                river_cur = (river_cur[0], river_cur[1] + 1)

        for i in range(height):
            for j in range(width):
                if field[i][j] == CellType.EMPTY and random.random() <= forest_proba:
                    field[i][j] = CellType.TREE

        return field

    def render(self):
        result = []
        for i in range(self.height):
            row_icons = []
            for j in range(self.width):
                if self.hellcopter.y == i and self.hellcopter.x == j:
                    cell_icon = Icons.HELLICOPTER
                elif self.field[i][j] == CellType.EMPTY:
                    cell_icon = Icons.EMPTY
                elif self.field[i][j] == CellType.TREE:
                    cell_icon = Icons.TREE
                elif self.field[i][j] == CellType.FIRE:
                    cell_icon = Icons.FIRE
                elif self.field[i][j] == CellType.WATER:
                    cell_icon = Icons.WATER
                row_icons.append(cell_icon)
            result.append(row_icons)
        return result

    def helli_go_up(self):
        self.hellcopter.y = max(0, self.hellcopter.y - 1)

    def helli_go_down(self):
        self.hellcopter.y = min(self.height - 1, self.hellcopter.y + 1)

    def helli_go_left(self):
        self.hellcopter.x = max(0, self.hellcopter.x - 1)
    
    def helli_go_right(self):
        self.hellcopter.x = min(self.width - 1, self.hellcopter.x + 1)

    def helli_interact(self):
        current_helli_cell_type = self.field[self.hellcopter.y][self.hellcopter.x]
        if current_helli_cell_type == CellType.WATER:
            self.hellcopter.has_water = True
        elif self.hellcopter.has_water:
            self.hellcopter.has_water = False

            if current_helli_cell_type == CellType.FIRE:
                self.field[self.hellcopter.y][self.hellcopter.x] = CellType.TREE

    def _get_coordinates_of_type(self, t):
        return [
            (i, j) for i in range(self.height) for j in range(self.width)
            if self.field[i][j] == t
        ]

    def spawn_fire(self, count):
        # remove strongly burned trees
        strong_fire_coordinates = self._get_coordinates_of_type(CellType.STRONG_FIRE)
        for (i, j) in strong_fire_coordinates:
            self.field[i][j] = CellType.EMPTY

        # grow prefious fire
        fire_coordinates = self._get_coordinates_of_type(CellType.FIRE)
        for (i, j) in fire_coordinates:
            
            self.field[i][j] = CellType.STRONG_FIRE

            for i_delta, j_delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    0 <= i + i_delta < self.height and
                    0 <= j + j_delta < self.width and
                    self.field[i+i_delta][j+j_delta] == CellType.TREE
                ):
                    self.field[i+i_delta][j+j_delta] = CellType.FIRE

        # spawn new fire
        tree_coordinates = self._get_coordinates_of_type(CellType.TREE)
        fired_trees = random.sample(tree_coordinates, min(count, len(tree_coordinates)))
        for (i, j) in fired_trees:
            self.field[i][j] = CellType.FIRE


def main():
    # width, height = map(int, input("Введите ширину и высоту поля через пробел: ").split())
    width, height = 10, 10
    UPDATE_MS = 100
    CELL_SIZE_PX = 20
    SCREEN_WIDTH = max(4 * CELL_SIZE_PX, width * CELL_SIZE_PX)
    SCREEN_HEIGHT = (height + 2) * CELL_SIZE_PX
    SPAWN_FIRE_EVERY_N_SECONDS = 10
    FIRE_COUNTS = 3

    field = Field(width, height)

    root = Tk()
    canvas = Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    canvas.pack()

    icon_path_to_photoimage = {
        path: PhotoImage(file=path)
        for path in [
            Icons.EMPTY, Icons.FIRE, Icons.HELLICOPTER,
            Icons.TREE, Icons.WATER, Icons.CROSS
        ]
    }

    tick_i = 0
    spawn_fire_every_n_ticks = SPAWN_FIRE_EVERY_N_SECONDS * 1000 // UPDATE_MS

    def redraw():
        canvas.delete("all")
        for i, row in enumerate(field.render()):
            for j, path in enumerate(row):
                canvas.create_image(
                    j * CELL_SIZE_PX,
                    i * CELL_SIZE_PX,
                    anchor=NW,
                    image=icon_path_to_photoimage[path]
                )
        
        # draw icon bar
        water_icon_position_x = 0
        water_icon_position_y = (height + 1) * CELL_SIZE_PX
        canvas.create_image(
            water_icon_position_x, water_icon_position_y,
            anchor=NW,
            image=icon_path_to_photoimage[
                Icons.WATER if field.hellcopter.has_water else Icons.CROSS
            ]
        )

    def tick():
        nonlocal tick_i

        if tick_i % spawn_fire_every_n_ticks == 0:
            field.spawn_fire(FIRE_COUNTS)

        redraw()

        tick_i += 1
        root.after(UPDATE_MS, tick)
    
    def on_key_press(event):
        if event.keycode == 116:
            field.helli_go_down()
        elif event.keycode == 111:
            field.helli_go_up()
        elif event.keycode == 113:
            field.helli_go_left()
        elif event.keycode == 114:
            field.helli_go_right()
        elif event.keycode == 65:
            field.helli_interact()
        print(event)

    root.bind("<KeyPress>", on_key_press)
    root.after(0, tick)
    mainloop()


if __name__ == "__main__":
    main()
