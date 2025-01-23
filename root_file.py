import tkinter
from tkinter import ttk


class MyRoot(tkinter.Tk):
    def __init__(self, tittle, icon_file):
        super().__init__()
        self.title(tittle)
        self.state('zoomed')
        icon = tkinter.PhotoImage(file=icon_file)
        self.iconphoto(False, icon)
        self.minsize(self.winfo_width(), self.winfo_height())


root = MyRoot('Miner', 'icon.png')
W = root.winfo_width()
H = root.winfo_height()

gm = {}
x_cord = 100
y_cord = 300
row = 0
stolb = 0
while y_cord < H - 200:
    gm[f'{row}.{stolb}'] = (x_cord, y_cord, x_cord+99, y_cord+99)
    stolb += 1
    x_cord += 100
    if x_cord >= W-200:
        x_cord = 100
        y_cord += 100
        row += 1
        stolb = 0


class PlayingField(tkinter.Canvas):
    Game_matrix = gm

    @classmethod
    def checkt_game_position(cls, x_position, y_position):
        for k, j in cls.Game_matrix.items():
            if (j[0] < x_position < j[2]) and (j[1] < y_position < j[3]):
                return k

    def __init__(self):
        super().__init__()
        self['bg'] = 'lime'
        self['width'] = W
        self['height'] = H


Main_canvas = PlayingField()
Main_canvas.pack(anchor='sw', expand=1)


class Entity:
    def __init__(self, x_pos, y_pos, image):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = tkinter.PhotoImage(file=image)
        self.image_item = None

    def entity_pack(self, canvas):
        self.image_item = canvas.create_image(self.x_pos, self.y_pos, anchor='center', image=self.image)


class Player(Entity):
    def __init__(self, image, x, y):
        super().__init__(x, y, image)

    def move(self, canvas, attribute, value):
        if (attribute == 'x') and (20 < self.x_pos + value < W - 20):
            canvas.move(self.image_item, value, 0)
            self.x_pos += value
        elif (attribute == 'y') and (20 < self.y_pos + value < H - 20):
            canvas.move(self.image_item, 0, value)
            self.y_pos += value

        lbl['text'] = PlayingField.checkt_game_position(self.x_pos, self.y_pos)




def moving_bind(event):
    char = str(event.char).lower()
    if char in ['a', 'ф']:
        Main_player.move(Main_canvas, 'x', -20)
    elif char in ['d', 'в']:
        Main_player.move(Main_canvas, 'x', 20)
    elif char in ['s', 'ы']:
        Main_player.move(Main_canvas, 'y', 20)
    elif char in ['w', 'ц']:
        Main_player.move(Main_canvas, 'y', -20)


for i in PlayingField.Game_matrix.values():
    Main_canvas.create_rectangle(i[0], i[1], i[2], i[3])


Main_player = Player('Player.png', PlayingField.Game_matrix['0.0'][0] + 50, PlayingField.Game_matrix['0.0'][1] + 50)
Main_player.entity_pack(Main_canvas)



lbl = ttk.Label(text='None', font='Arial 20', background='lime')
Main_canvas.create_window(100, 100, anchor='center', window=lbl, width=100, height=50)

root.bind('<KeyPress>', moving_bind)

root.mainloop()
