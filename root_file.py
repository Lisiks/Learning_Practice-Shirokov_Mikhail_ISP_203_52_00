import tkinter
from tkinter import ttk


class MyRoot:
    """ Класс для создания и настройки окна приложения"""

    def __init__(self, title, icon_file):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.root.state('zoomed')
        icon = tkinter.PhotoImage(file=icon_file)
        self.root.iconphoto(False, icon)
        self.H = self.root.winfo_height()
        self.W = self.root.winfo_width()
        self.root.minsize(self.W, self.H)

    def run(self):
        self.root.mainloop()


Window = MyRoot('Miner', 'icon.png')


GM = []
x_cord = 100
y_cord = 300
row = []
while y_cord < Window.H - 200:
    row.append([x_cord + 50, y_cord + 50, 0, ''])
    x_cord += 100
    if x_cord >= Window.W-200:
        s = row.copy()
        GM.append(s)
        x_cord = 100
        y_cord += 100
        row.clear()


class PlayingField:
    Game_matrix = GM
    Game_matrix_row_count = len(Game_matrix)
    Game_matrix_column_count = len(Game_matrix[0])

    Game_canvas = tkinter.Canvas(Window.root, width=Window.W, height=Window.H, bg='lime')

    __Level = 1
    __Level_hash = {
        1: (((1, 1), (1, 2), (4, 1), (4, 2), (1, 14), (1, 15), (4, 14), (4, 15)),
            ((2, 4), (3, 4), (3, 5), (2, 6), (2, 5), (3, 6))),
        2: ((), ()),
        3: ((), ()),
        4: ((), ()),
        5: ((), ())
    }

    @classmethod
    def next_level(cls, level_number):
        cls.Game_matrix = GM
        cls.__Level = level_number
        cls.generate_level()

    @classmethod
    def generate_level(cls):
        for i in range(len(cls.Game_matrix)):
            for j in range(len(cls.Game_matrix[i])):
                if (i, j) in cls.__Level_hash[cls.__Level][0]:
                    cls.Game_matrix[i][j][2] = cls.Game_canvas.create_image(cls.Game_matrix[i][j][0], cls.Game_matrix[i][j][1], anchor='center', image=undestroyable_wall_image)
                    cls.Game_matrix[i][j][3] = 'undestroyable'
                elif (i, j) in cls.__Level_hash[cls.__Level][1]:
                    cls.Game_matrix[i][j][2] = cls.Game_canvas.create_image(cls.Game_matrix[i][j][0], cls.Game_matrix[i][j][1], anchor='center', image=destroyable_wall_image)
                    cls.Game_matrix[i][j][3] = 'destroyable'


PlayingField.Game_canvas.pack(anchor='center', expand=1)


class Entity:
    def __init__(self, matrix_pos_i, matrix_pos_j, image):
        self.matrix_pos_i = matrix_pos_i
        self.matrix_pos_j = matrix_pos_j
        self.image = tkinter.PhotoImage(file=image)
        self.image_item = None

    def entity_pack(self, canvas):
        x_pos = PlayingField.Game_matrix[self.matrix_pos_i][self.matrix_pos_j][0]
        y_pos = PlayingField.Game_matrix[self.matrix_pos_i][self.matrix_pos_j][1]
        self.image_item = canvas.create_image(x_pos, y_pos, anchor='center', image=self.image)


class Player(Entity):
    def __init__(self, image, matrix_pos_i, matrix_pos_j):
        super().__init__(matrix_pos_i, matrix_pos_j, image)

    def player_action(self, event):
        if ((str(event.char).lower() in ('d', 'в')) and (self.matrix_pos_j + 1 < PlayingField.Game_matrix_column_count)
                and not (PlayingField.Game_matrix[self.matrix_pos_i][self.matrix_pos_j + 1][2])):
            self.matrix_pos_j += 1
            PlayingField.Game_canvas.move(self.image_item, 100, 0)

        elif ((str(event.char).lower() in ('a', 'ф')) and (self.matrix_pos_j - 1 >= 0)
              and not (PlayingField.Game_matrix[self.matrix_pos_i][self.matrix_pos_j - 1][2])):
            self.matrix_pos_j -= 1
            PlayingField.Game_canvas.move(self.image_item, -100, 0)

        elif ((str(event.char).lower() in ('w', 'ц')) and (self.matrix_pos_i - 1 >= 0)
              and not (PlayingField.Game_matrix[self.matrix_pos_i - 1][self.matrix_pos_j][2])):
            self.matrix_pos_i -= 1
            PlayingField.Game_canvas.move(self.image_item, 0, -100)

        elif ((str(event.char).lower() in ('s', 'ы')) and (self.matrix_pos_i + 1 < PlayingField.Game_matrix_row_count)
              and not (PlayingField.Game_matrix[self.matrix_pos_i + 1][self.matrix_pos_j][2])):
            self.matrix_pos_i += 1
            PlayingField.Game_canvas.move(self.image_item, 0, 100)

        elif str(event.char).lower() in ('e', 'у'):
            Bombs.bomb_has_been_planted(self.matrix_pos_i, self.matrix_pos_j)


class Bombs:
    @classmethod
    def explotions(cls, bomb_i, bomb_j):
        for i in range(bomb_i + 1, bomb_i + cls.__bomb_range + 1):
            if (i < PlayingField.Game_matrix_row_count) and (PlayingField.Game_matrix[i][bomb_j][3] == 'destroyable'):
                PlayingField.Game_canvas.delete(PlayingField.Game_matrix[i][bomb_j][2])
                PlayingField.Game_matrix[i][bomb_j][2] = 0
                PlayingField.Game_matrix[i][bomb_j][3] = ''

        for i in range(bomb_i - cls.__bomb_range, bomb_i):
            if (i > 0) and (PlayingField.Game_matrix[i][bomb_j][3] == 'destroyable'):
                PlayingField.Game_canvas.delete(PlayingField.Game_matrix[i][bomb_j][2])
                PlayingField.Game_matrix[i][bomb_j][2] = 0
                PlayingField.Game_matrix[i][bomb_j][3] = ''

        for j in range(bomb_j + 1, bomb_j + cls.__bomb_range + 1):
            if (j < PlayingField.Game_matrix_column_count) and (PlayingField.Game_matrix[bomb_i][j][3] == 'destroyable'):
                PlayingField.Game_canvas.delete(PlayingField.Game_matrix[bomb_i][j][2])
                PlayingField.Game_matrix[bomb_i][j][2] = 0
                PlayingField.Game_matrix[bomb_i][j][3] = ''

        for j in range(bomb_j - cls.__bomb_range, bomb_j):
            if (j < len(PlayingField.Game_matrix[0])) and (PlayingField.Game_matrix[bomb_i][j][3] == 'destroyable'):
                PlayingField.Game_canvas.delete(PlayingField.Game_matrix[bomb_i][j][2])
                PlayingField.Game_matrix[bomb_i][j][2] = 0
                PlayingField.Game_matrix[bomb_i][j][3] = ''

        PlayingField.Game_canvas.delete(cls.__bombs_array.pop(0))

    __max_bomb = 1
    __bomb_range = 1
    __bombs_array = []
    __bombs_image = tkinter.PhotoImage(file='Бимба.png')

    @classmethod
    def bomb_has_been_planted(cls, bomb_i, bomb_j):
        if len(cls.__bombs_array) < cls.__max_bomb:
            cls.__bombs_array.append(PlayingField.Game_canvas.create_image(PlayingField.Game_matrix[bomb_i][bomb_j][0], PlayingField.Game_matrix[bomb_i][bomb_j][1], anchor='center', image=cls.__bombs_image))
            Window.root.after(2000, lambda: cls.explotions(bomb_i, bomb_j))


Main_player = Player('Player.png', 0, 0)
Main_player.entity_pack(PlayingField.Game_canvas)


undestroyable_wall_image = tkinter.PhotoImage(file='undestroyable_wall.png')
destroyable_wall_image = tkinter.PhotoImage(file='destroyable_wall.png')
PlayingField.generate_level()


Window.root.bind('<KeyPress>', lambda e: Main_player.player_action(e))

if __name__ == '__main__':
    Window.run()
