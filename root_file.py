import tkinter
from random import choice
import threading






class MyRoot(tkinter.Tk):
    """ Класс для создания и настройки окна приложения"""



    def __init__(self, title, icon_file):
        super().__init__()

        self.title(title)
        self.state('zoomed')
        icon = tkinter.PhotoImage(file=icon_file)
        self.iconphoto(False, icon)
        self.H = self.winfo_height()
        self.W = self.winfo_width()
        self.minsize(self.W, self.H)

        self.img = {
            'menu': tkinter.PhotoImage(file='menu_bg.png'),
            'interface': tkinter.PhotoImage(file='interface.png'),
            'exit': tkinter.PhotoImage(file='exit.png'),
            'bomb': tkinter.PhotoImage(file='bomb.png'),
            'animation': {
                    'player': {
                        'left': [
                            tkinter.PhotoImage(file='Player/Player_left_1_3.png'),
                            tkinter.PhotoImage(file='Player/Player_left_2.png'),
                            tkinter.PhotoImage(file='Player/Player_left_1_3.png'),
                            tkinter.PhotoImage(file='Player/Player_left_4_8.png'),
                            tkinter.PhotoImage(file='Player/Player_left_5_7.png'),
                            tkinter.PhotoImage(file='Player/Player_left_6.png'),
                            tkinter.PhotoImage(file='Player/Player_left_5_7.png'),
                            tkinter.PhotoImage(file='Player/Player_left_4_8.png')
                            ],
                        'right': [
                            tkinter.PhotoImage(file='Player/Player_right_1_3.png'),
                            tkinter.PhotoImage(file='Player/Player_right_2.png'),
                            tkinter.PhotoImage(file='Player/Player_right_1_3.png'),
                            tkinter.PhotoImage(file='Player/Player_right_4_8.png'),
                            tkinter.PhotoImage(file='Player/Player_right_5_7.png'),
                            tkinter.PhotoImage(file='Player/Player_right_6.png'),
                            tkinter.PhotoImage(file='Player/Player_right_5_7.png'),
                            tkinter.PhotoImage(file='Player/Player_right_4_8.png')
                            ]
                    },
                },
            'des_wal': {
                1: tkinter.PhotoImage(file='destroyable_wall.png'),
                2: tkinter.PhotoImage(file='destroyable_wall.png'),
                3: tkinter.PhotoImage(file='destroyable_wall.png'),
                4: tkinter.PhotoImage(file='destroyable_wall.png'),
                5: tkinter.PhotoImage(file='destroyable_wall.png'),
                },
            'und_des_wal': {
                1: tkinter.PhotoImage(file='destroyable_wall.png'),
                2: tkinter.PhotoImage(file='destroyable_wall.png'),
                3: tkinter.PhotoImage(file='destroyable_wall.png'),
                4: tkinter.PhotoImage(file='destroyable_wall.png'),
                5: tkinter.PhotoImage(file='destroyable_wall.png'),
            },
            'field': {
                1: None,
                2: None,
                3: None,
                4: None,
                5: None
            }
        }

        self.Main_menu_frame = tkinter.Frame(master=self, width=1920, height=1080)
        self.Game_frame = tkinter.Frame(master=self)

        self.Options_frame = tkinter.Frame(master=self)
        self.Records_frame = tkinter.Frame(master=self)
        self.Game_over_frame = tkinter.Frame(master=self)

        self.__Menu_canvas = tkinter.Canvas(master=self.Main_menu_frame, width=self.W, height=self.H)
        self.__Menu_canvas.pack(anchor='nw')
        self.__Menu_canvas.create_image(0, 0, anchor='nw', image=self.img['menu'])

        self.__Menu_canvas.create_window(self.W//2, self.H-80, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Выход', width=80, height=2, bg='#694532', command=exit, font=('impact', 15),
            activeforeground='white', activebackground='#523627', borderwidth=3, fg='white'))

        self.__Menu_canvas.create_window(self.W//2, self.H-160, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Рекорды', width=80, height=2, bg='#694532',
            command=lambda: MyRoot.change_frame(self.Main_menu_frame, self.Records_frame),
            font=('impact', 15), activeforeground='white', activebackground='#523627', borderwidth=3, fg='white'))

        self.__Menu_canvas.create_window(self.W//2, self.H-240, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Настройки', width=80, height=2, bg='#694532',
            command=lambda: MyRoot.change_frame(self.Main_menu_frame, self.Options_frame), font=('impact', 15),
            activeforeground='white', activebackground='#523627', borderwidth=3, fg='white'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 320, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Играть', width=80, height=2, bg='#694532',
            command=self.play_button, font=('impact', 15),
            activeforeground='white', activebackground='#523627', borderwidth=3, fg='white'))

        self.Main_menu_frame.pack()

        tkinter.Button(master=self.Options_frame, text='Menu',
                       command=lambda f1=self.Options_frame, f2=self.Main_menu_frame: MyRoot.change_frame(f1, f2)
                       ).pack(side='left', padx=20, pady=20)
        tkinter.Button(master=self.Records_frame, text='Menu',
                       command=lambda f1=self.Records_frame, f2=self.Main_menu_frame: MyRoot.change_frame(f1, f2)
                       ).pack(side='left', padx=20, pady=20)

        tkinter.Button(master=self.Game_over_frame, text='Menu',
                       command=lambda f1=self.Game_over_frame, f2=self.Main_menu_frame: MyRoot.change_frame(f1, f2)
                       ).pack(side='left', padx=20, pady=20)




    @staticmethod
    def change_frame(frame1, frame2):
        frame1.forget()
        frame2.pack(fill='both')

    def play_button(self):
        self.Main_menu_frame.forget()
        self.Game_frame.pack()
        PlayingField.play_level(1)


Window = MyRoot('Бомбермен', 'bomb.png')


class PlayingField:
    """ Класс, отвечающий за события, происходящие на игровом поле"""
    Game_matrix = []
    Game_canvas = tkinter.Canvas(master=Window.Game_frame, width=Window.W, height=Window.H, bg='lime')
    Game_canvas.pack(anchor='center', expand=1)
    exit_cords = None

    Level = 0
    __Level_hash = {
        1: (((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15)),
            ((2, 6), (2, 7), (2, 8), (3, 6), (3, 7), (3, 8))),
        2: ((), ((2, 3), (3, 4))),
        3: ((), ((2, 3),)),
        4: ((), ((2, 3),)),
        5: ((), ((2, 3),))
    }

    @classmethod
    def play_level(cls, level_number):
        cls.Level = level_number
        cls.Game_canvas.delete('all')
        Bombs.clear_bomb()
        cls.set_default_matrix()

        cls.Game_canvas.create_window(114, 917, anchor='nw', width=622, height=88, window=tkinter.Button(text='Выход в главное меню',
                bg='#696969', fg='white', font=('impact', 15), activeforeground='white',
                activebackground='#5E5E5E', command=lambda: Window.change_frame(Window.Game_frame, Window.Main_menu_frame)))

        cls.Game_canvas.create_image(0, 0, anchor='nw', image=Window.img['interface'])
        cls.exit_cords = choice(cls.__Level_hash[level_number][1])
        cls.generate_level()
        Main_player.player_pack(cls.Game_canvas, 0, 0, Main_player.animation['right'][-1])
        Window.bind('<KeyPress>', Main_player.player_action)



    @classmethod
    def generate_level(cls):
        for i in range(len(cls.Game_matrix)):
            for j in range(len(cls.Game_matrix[i])):
                if (i, j) in cls.__Level_hash[cls.Level][0]:
                    cls.Game_matrix[i][j][2] = cls.Game_canvas.create_image(cls.Game_matrix[i][j][0], cls.Game_matrix[i][j][1], anchor='center', image=Window.img['und_des_wal'][cls.Level])
                    cls.Game_matrix[i][j][3] = 'undestroyable'
                elif (i, j) in cls.__Level_hash[cls.Level][1]:
                    cls.Game_matrix[i][j][2] = cls.Game_canvas.create_image(cls.Game_matrix[i][j][0], cls.Game_matrix[i][j][1], anchor='center', image=Window.img['des_wal'][cls.Level])
                    cls.Game_matrix[i][j][3] = 'destroyable'

    @classmethod
    def set_default_matrix(cls):
        cls.Game_matrix.clear()
        x_cord = 100
        y_cord = 300
        row = []

        while y_cord < Window.H - 200:
            row.append([x_cord + 100 // 2, y_cord + 100 // 2, 0,''])
            x_cord += 100
            if x_cord >= Window.W - 200:
                s = row.copy()
                cls.Game_matrix.append(s)
                x_cord = 100
                y_cord += 100
                row.clear()

    @classmethod
    def move_is(cls, p_i, p_j):
        return True if (0 <= p_i < 6) and (0 <= p_j < 17) and (cls.Game_matrix[p_i][p_j][2] == 0) else False



    @classmethod
    def spaun_exit(cls):
        if cls.Game_matrix[cls.exit_cords[0]][cls.exit_cords[1]][2] == 0:
            cls.Game_canvas.create_image(cls.Game_matrix[cls.exit_cords[0]][cls.exit_cords[1]][0], cls.Game_matrix[cls.exit_cords[0]][cls.exit_cords[1]][1], image=Window.img['exit'])

    @classmethod
    def game_over(cls, game_rezult):
        Window.change_frame(Window.Game_frame, Window.Game_over_frame)

    @classmethod
    def exit_level(cls, player_i, player_j):
        if player_i == cls.exit_cords[0] and player_j == cls.exit_cords[1]:
            Window.unbind('<KeyPress>')
            if cls.Level < 5:
                cls.play_level(cls.Level + 1)
            else:
                cls.game_over('win')


class Entity:
    """ Класс для различных существ - игрока и врагов"""
    def __init__(self,right_image_list, left_image_list, matrix_pos_i=0, matrix_pos_j=0):
        self.matrix_pos_i = matrix_pos_i
        self.matrix_pos_j = matrix_pos_j
        self.x = None
        self.y = None
        self.animation = {'right': right_image_list, 'left': left_image_list}
        self.image_item = None
        self.orientation = 'right'
        self.on_moving = False

    def entity_pack(self, canvas, pos_i, pos_j, image):
        self.x = PlayingField.Game_matrix[pos_i][pos_j][0]
        self.y = PlayingField.Game_matrix[pos_i][pos_j][1]
        self.matrix_pos_i = pos_i
        self.matrix_pos_j = pos_j
        self.image_item = canvas.create_image(self.x, self.y, anchor='center', image=image)
        self.orientation = 'right'

    def moving_animation(self, canvas, distance, vector, cords):
        def time_iteration(i):
            if i < len(self.animation[vector]):
                self.x += distance / len(self.animation[vector]) if cords == 'X' else 0
                self.y += distance / len(self.animation[vector]) if cords == 'Y' else 0
                canvas.delete(self.image_item)
                self.image_item = canvas.create_image(self.x, self.y, anchor='center', image=self.animation[vector][i])
                Window.after(40, lambda: time_iteration(i + 1))
            else:
                PlayingField.exit_level(self.matrix_pos_i, self.matrix_pos_j)
                self.on_moving = False

        self.orientation = vector
        time_iteration(0)


class Player(Entity):
    """ Класс игрока """
    def __init__(self, right_image_list, left_image_list):
        super().__init__(right_image_list, left_image_list)
        self.HP = None

    def player_pack(self, canvas, pos_i, pos_j, image):
        self.entity_pack(canvas, pos_i, pos_j, image)
        self.HP = 3

    def get_hit(self, danger_i, danger_j):
        if (danger_i == self.matrix_pos_i) and (danger_j == self.matrix_pos_j):
            self.HP -= 1
            if self.HP <= 0:
                PlayingField.game_over('loose')

    def player_action(self, event):
        if (event.char.lower() in ('d', 'в')) and PlayingField.move_is(self.matrix_pos_i, self.matrix_pos_j+1) and not self.on_moving:
            self.on_moving = True
            self.matrix_pos_j += 1
            self.moving_animation(PlayingField.Game_canvas, 100, 'right', 'X')

        elif (event.char.lower() in ('a', 'ф')) and PlayingField.move_is(self.matrix_pos_i, self.matrix_pos_j-1) and not self.on_moving:
            self.on_moving = True
            self.matrix_pos_j -= 1
            self.moving_animation(PlayingField.Game_canvas, -100, 'left', 'X')

        elif (event.char.lower() in ('w', 'ц')) and PlayingField.move_is(self.matrix_pos_i-1, self.matrix_pos_j) and not self.on_moving:
            self.on_moving = True
            self.matrix_pos_i -= 1
            self.moving_animation(PlayingField.Game_canvas, -100, self.orientation, 'Y')

        elif (event.char.lower() in ('s', 'ы')) and PlayingField.move_is(self.matrix_pos_i+1, self.matrix_pos_j) and not self.on_moving:
            self.on_moving = True
            self.matrix_pos_i += 1
            self.moving_animation(PlayingField.Game_canvas, 100, self.orientation, 'Y')

        elif event.char.lower() in ('e', 'у'):
            Bombs.bomb_has_been_planted(self.matrix_pos_i, self.matrix_pos_j)


class Bombs:
    """Класс описывающий бомбы и основные функции с ними"""
    @classmethod
    def explotions(cls, bomb_i, bomb_j):
        if len(cls.__bombs_array) != 0:
            for i in range(bomb_i + 1, bomb_i + cls.__bomb_range + 1):
                Main_player.get_hit(i, bomb_j)
                if (i < 6) and (PlayingField.Game_matrix[i][bomb_j][3] == 'destroyable'):
                    PlayingField.Game_canvas.delete(PlayingField.Game_matrix[i][bomb_j][2])
                    PlayingField.Game_matrix[i][bomb_j][2] = 0
                    PlayingField.Game_matrix[i][bomb_j][3] = ''
                    break

            for i in range(bomb_i - 1, bomb_i - cls.__bomb_range - 1, -1):
                Main_player.get_hit(i, bomb_j)
                if (i > 0) and (PlayingField.Game_matrix[i][bomb_j][3] == 'destroyable'):
                    PlayingField.Game_canvas.delete(PlayingField.Game_matrix[i][bomb_j][2])
                    PlayingField.Game_matrix[i][bomb_j][2] = 0
                    PlayingField.Game_matrix[i][bomb_j][3] = ''
                    break

            for j in range(bomb_j + 1, bomb_j + cls.__bomb_range + 1):
                Main_player.get_hit(bomb_i, j)
                if (j < 17) and (PlayingField.Game_matrix[bomb_i][j][3] == 'destroyable'):
                    PlayingField.Game_canvas.delete(PlayingField.Game_matrix[bomb_i][j][2])
                    PlayingField.Game_matrix[bomb_i][j][2] = 0
                    PlayingField.Game_matrix[bomb_i][j][3] = ''
                    break

            for j in range(bomb_j - 1, bomb_j - cls.__bomb_range - 1, -1):
                Main_player.get_hit(bomb_i, j)
                if (j < len(PlayingField.Game_matrix[0])) and (PlayingField.Game_matrix[bomb_i][j][3] == 'destroyable'):
                    PlayingField.Game_canvas.delete(PlayingField.Game_matrix[bomb_i][j][2])
                    PlayingField.Game_matrix[bomb_i][j][2] = 0
                    PlayingField.Game_matrix[bomb_i][j][3] = ''
                    break

            PlayingField.spaun_exit()
            PlayingField.Game_canvas.delete(cls.__bombs_array.pop(0))

    __max_bomb = 1
    __bomb_range = 1
    __bombs_array = []

    @classmethod
    def bomb_has_been_planted(cls, bomb_i, bomb_j):
        if len(cls.__bombs_array) < cls.__max_bomb:
            cls.__bombs_array.append(PlayingField.Game_canvas.create_image(PlayingField.Game_matrix[bomb_i][bomb_j][0], PlayingField.Game_matrix[bomb_i][bomb_j][1], anchor='center', image=Window.img['bomb']))
            Window.after(2000, lambda: cls.explotions(bomb_i, bomb_j))

    @classmethod
    def clear_bomb(cls):
        cls.__bombs_array.clear()


Main_player = Player(Window.img['animation']['player']['right'], Window.img['animation']['player']['left'])


if __name__ == '__main__':
    Window.mainloop()
