__author__ = 'Noah'

import tkinter as tk

canvas_size = 400
colors = ['white', 'red', 'green', 'cyan', 'yellow', 'purple', 'gray24', 'brown', 'dark green', 'blue']


class App:
    def __init__(self, seed):

        # world stuff
        self.seed = seed
        self.world = {}
        self.min_x = self.min_y = self.max_x = self.max_y = 0
        self.x = self.y =self.counter = 0
        self.dir = 3
        self.current_size = 5

        # canvas stuff
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size)
        self.canvas.pack()
        self.root.focus_set()
        self.root.after(1, self.update_clock)
        self.root.mainloop()

    def get_field(self, x, y):
        if x in self.world and y in self.world[x]:
            return self.world[x][y]
        return 0

    def set_field(self, x, y, value):
        if x not in self.world:
            if x < self.min_x:
                self.min_x = x
            elif x > self.max_x:
                self.max_x = x
            self.world[x] = {}
        if y not in self.world:
            if y < self.min_y:
                self.min_y = y
            elif y > self.max_y:
                self.max_y = y
        self.world[x][y] = value

    def update_clock(self):
        current_field = self.get_field(self.x, self.y)
        self.set_field(self.x, self.y, (current_field + 1) % len(self.seed))

        current_action = self.seed[(current_field + 1) % len(self.seed)]

        self.dir = (self.dir - current_action) % 4

        if self.dir == 0:
            self.x -= 1
        elif self.dir == 1:
            self.y += 1
        elif self.dir == 2:
            self.x += 1
        elif self.dir == 3:
            self.y -= 1

        self.counter = (self.counter + 1) % 10

        if self.current_size < 10 or self.counter == 0:
            self.draw()

        if self.current_size < 10:
            self.root.after(10, self.update_clock)
        else:
            self.root.after(1, self.update_clock)

    def get_color(self, x, y):
        if x in self.world and y in self.world[x]:
            return colors[self.world[x][y]]
        return 'grey'

    def draw(self):
        self.canvas.delete('all')

        if abs(self.min_x) > self.current_size-2 or abs(self.max_x) > self.current_size-2 or \
                abs(self.min_y) > self.current_size-2 or abs(self.max_y) > self.current_size-2:
            self.current_size += 5

        tile_size = round((canvas_size / self.current_size) / 2)
        for x in range(-self.current_size, self.current_size):
            for y in range(-self.current_size, self.current_size):
                start_x = (x + self.current_size) * tile_size
                start_y = (y + self.current_size) * tile_size
                color = self.get_color(x, y)
                outcolor = 'black'
                if self.current_size > 20:
                    outcolor = color
                self.canvas.create_rectangle(start_x, start_y, start_x + tile_size - 1, start_y + tile_size - 1,
                                             fill=color, outline=outcolor)


app = App([1, 1, 1, -1, 1, -1, 1])
#app = App([1, -1])
