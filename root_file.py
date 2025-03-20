import tkinter
import random
import threading
from time import sleep


class MyRoot(tkinter.Tk):
    """ Класс для создания и настройки окна приложения"""

    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.state('zoomed')
        self.img = {
            'menu': tkinter.PhotoImage(file='Images/menu_bg.png'),
            'interface': tkinter.PhotoImage(file='Images/interface.png'),
            'empy_heart': tkinter.PhotoImage(file='Images/empy_heart.png'),
            'bomb': tkinter.PhotoImage(file='Images/bomb.png'),
            'animation': {
                'player': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_left_4_8.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Player/Player_right_4_8.png')
                    )
                },
                'green_slime': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Left_6.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Green_Slime/Green_Slime_Right_6.png')
                    )
                },
                'slime': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_Left_6.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Slime/Slime_right_6.png')
                    )
                },
                'lava_slime': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Left_6.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_2_4.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_1_5.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Lava_Slime/Lava_Slime_Right_6.png')
                    )
                },
                'skeleton': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_left_4_8.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Skeleton/Skeleton_right_4_8.png')
                    ),
                },
                'zombie': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_left_4_8.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Zombie/Zombie_right_4_8.png')
                    ),
                },
                'wither': {
                    'left': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_left_4_8.png')
                    ),
                    'right': (
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_2.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_1_3.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_4_8.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_6.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_5_7.png'),
                        tkinter.PhotoImage(file='Images/Animations/Enemys/Wither/Wither_right_4_8.png')
                    ),
                },
            },
            'exit': {
                'active': tkinter.PhotoImage(file='Images/PlayingField/exit/active_exit.png'),
                'not_active': tkinter.PhotoImage(file='Images/PlayingField/exit/unactive_exit.png')
            },
            'des_wal': {
                1: tkinter.PhotoImage(file='Images/PlayingField/destroyable_wall/dw_1.png'),
                2: tkinter.PhotoImage(file='Images/PlayingField/destroyable_wall/dw_2.png'),
                3: tkinter.PhotoImage(file='Images/PlayingField/destroyable_wall/dw_3.png'),
                4: tkinter.PhotoImage(file='Images/PlayingField/destroyable_wall/dw_4.png'),
                5: tkinter.PhotoImage(file='Images/PlayingField/destroyable_wall/dw_5.png')
            },
            'und_des_wal': {
                1: tkinter.PhotoImage(file='Images/PlayingField/undestroyable_wall/ud_1.png'),
                2: tkinter.PhotoImage(file='Images/PlayingField/undestroyable_wall/ud_2.png'),
                3: tkinter.PhotoImage(file='Images/PlayingField/undestroyable_wall/ud_3.png'),
                4: tkinter.PhotoImage(file='Images/PlayingField/undestroyable_wall/ud_4.png'),
                5: tkinter.PhotoImage(file='Images/PlayingField/undestroyable_wall/ud_5.png')
            },
            'field': {
                1: tkinter.PhotoImage(file='Images/PlayingField/Field/Field1.png'),
                2: tkinter.PhotoImage(file='Images/PlayingField/Field/Field2.png'),
                3: tkinter.PhotoImage(file='Images/PlayingField/Field/Field3.png'),
                4: tkinter.PhotoImage(file='Images/PlayingField/Field/Field4.png'),
                5: tkinter.PhotoImage(file='Images/PlayingField/Field/Field5.png')
            },
            'powers': {
                'HP': tkinter.PhotoImage(file='Images/PlayingField/Powers/Life_power.png'),
                'bomb_range': tkinter.PhotoImage(file='Images/PlayingField/Powers/Range_power.png'),
                'max_bomb': tkinter.PhotoImage(file='Images/PlayingField/Powers/Max_power.png'),
                'speed': tkinter.PhotoImage(file='Images/PlayingField/Powers/Speed_power.png')
            }
        }
        self.iconphoto(False, self.img['bomb'])
        self.H = self.winfo_height()
        self.W = self.winfo_width()
        self.minsize(self.W, self.H)

        self.Options_frame = tkinter.Frame(master=self)
        self.Records_frame = tkinter.Frame(master=self)
        self.Game_over_frame = tkinter.Frame(master=self)

        self.Game_frame = tkinter.Frame(master=self, background='black')
        self.Main_menu_frame = tkinter.Frame(master=self, width=1920, height=1080)
        self.__Menu_canvas = tkinter.Canvas(master=self.Main_menu_frame, width=self.W, height=self.H)
        self.__Menu_canvas.pack(anchor='nw')
        self.__Menu_canvas.create_image(0, 0, anchor='nw', image=self.img['menu'])

        self.__Menu_canvas.create_window(self.W // 2, self.H - 160, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Выход', width=80, height=2, bg='#B35514', command=exit,
            font=('impact', 17), activeforeground='#FFDF60', activebackground='#A34D12', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 240, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Рекорды', width=80, height=2, bg='#B85715',
            command=lambda: MyRoot.change_frame(self.Main_menu_frame, self.Records_frame),
            font=('impact', 17), activeforeground='#FFDF60', activebackground='#A85013', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 320, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Настройки', width=80, height=2, bg='#BD5A15',
            command=lambda: MyRoot.change_frame(self.Main_menu_frame, self.Options_frame), font=('impact', 17),
            activeforeground='#FFDF60', activebackground='#AD5213', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 400, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Играть', width=80, height=2, bg='#C75E16',
            command=self.play_button, font=('impact', 17),
            activeforeground='#FFDF60', activebackground='#B35514', borderwidth=1, fg='#FFD88E'))

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
        self.Game_frame.pack(fill='both')
        PlayingField.play_level(1)


Window = MyRoot('Бомбермен')


class PlayingField:
    """ Класс, отвечающий за события, происходящие на игровом поле"""

    @classmethod
    def clear_matrix(cls):
        for i in range(len(cls.Game_matrix)):
            for j in range(len(cls.Game_matrix[i])):
                cls.Game_matrix[i][j][1], cls.Game_matrix[i][j][2] = 0, ''

    @staticmethod
    def generate_matrix():
        result = list()
        x_cord = 110
        y_cord = 300
        row = list()

        while y_cord < Window.H - 200:
            row.append([(x_cord + 100 // 2, y_cord + 100 // 2), 0, ''])
            x_cord += 100
            if x_cord >= Window.W - 200:
                s = row.copy()
                result.append(s)
                x_cord = 110
                y_cord += 100
                row.clear()
        return result

    Game_matrix = generate_matrix()
    Game_canvas = tkinter.Canvas(master=Window.Game_frame, width=Window.W, height=Window.H, bg='lime')
    Game_canvas.pack()

    __bombs_array = list()
    __Enemy_list = list()
    __Empy_heart_list = list()
    __labels = dict()
    __item_counter = {'speed': 0, 'max_bomb': 0, 'bomb_range': 0, 'score': 0}

    __exit_item = {'i': 0, 'j': 0, 'image_item': 0, 'state': 'NotSpawn'}
    __Level = 0
    __Level_hash = {
        1: {
            'undestroyable': ((1, 2), (1, 3), (1, 13), (1, 14),
                              (2, 6), (2, 7),
                              (3, 10), (3, 11),
                              (4, 2), (4, 3), (4, 13), (4, 14)),
            'destroyable': ((0, 1), (0, 2), (0, 3), (0, 7), (0, 8), (0, 9), (0, 13), (0, 14), (0, 15),
                            (1, 1), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 12), (1, 15),
                            (2, 2), (2, 3), (2, 4), (2, 5), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14),
                            (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 12), (3, 13), (3, 14),
                            (4, 1), (4, 4), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 12), (4, 15),
                            (5, 1), (5, 2), (5, 3), (5, 7), (5, 8), (5, 9), (5, 13), (5, 14), (5, 15))
            },
        2: {
            'undestroyable': ((1, 1), (1, 2), (1, 7), (1, 8), (1, 13), (1, 14),
                              (4, 3), (4, 4), (4, 5), (4, 6), (4, 9), (4, 10), (4, 11), (4, 12), (4, 15)),
            'destroyable': ((0, 2), (0, 4), (0, 6), (0, 7), (0, 10), (0, 12), (0, 13),
                            (1, 3), (1, 6), (1, 9), (1, 12), (1, 15),
                            (2, 1), (2, 2), (2, 7), (2, 8), (2, 9), (2, 14), (2, 15),
                            (3, 0), (3, 4), (3, 5), (3, 6), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13),
                            (4, 2), (4, 8), (4, 16),
                            (5, 0), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10), (5, 11), (5, 15), (5, 16))
            },
        3: {
            'undestroyable': ((0, 5), (0, 8), (0, 11),
                              (1, 1), (1, 2), (1, 3), (1, 5), (1, 11), (1, 13), (1, 14), (1, 15),
                              (2, 7), (2, 9),
                              (3, 8),
                              (4, 1), (4, 2), (4, 3), (4, 5), (4, 11), (4, 13), (4, 14), (4, 15),
                              (5, 5), (5, 8), (5, 11)),
            'destroyable': ((0, 12), (0, 13), (0, 14), (0, 15), (0, 16),
                            (1, 0), (1, 4), (1, 7), (1, 8), (1, 9), (1, 12),
                            (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14),
                            (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13),
                            (4, 4), (4, 7), (4, 8), (4, 9), (4, 12), (4, 16),
                            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4)),

            },
        4: {
            'undestroyable': ((0, 8), (0, 9), (0, 10),
                              (1, 1), (1, 2), (1, 3), (1, 13), (1, 14), (1, 15),
                              (2, 5), (2, 6),
                              (3, 9), (3, 10), (3, 11), (3, 12),
                              (4, 2), (4, 3), (4, 4), (4, 6), (4, 7), (4, 14), (4, 15)),
            'destroyable': ((0, 2), (0, 3), (0, 11), (0, 15), (0, 16),
                            (1, 4), (1, 6), (1, 7), (1, 9), (1, 10), (1, 11), (1, 16),
                            (2, 0), (2, 7), (2, 10), (2, 11), (2, 12), (2, 13),
                            (3, 1), (3, 2), (3, 3), (3, 5), (3, 13),
                            (4, 1), (4, 8), (4, 10), (4, 11), (4, 16),
                            (5, 3), (5, 4), (5, 6), (5, 7), (5, 13), (5, 15), (5, 16))
            },
        5: {
            'undestroyable': ((1, 1), (1, 3), (1, 5), (1, 7), (1, 9), (1, 11), (1, 13), (1, 15),
                              (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (4, 11), (4, 13), (4, 15)),
            'destroyable': ((0, 2), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 12), (0, 14), (0, 16),
                            (1, 2), (1, 12), (1, 14), (1, 16), (1, 6), (1, 8), (1, 10),
                            (2, 0), (2, 1), (2, 2), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 6), (2, 7), (2, 8),
                            (2, 9), (2, 10),
                            (3, 2), (3, 3), (3, 4), (3, 14),
                            (4, 2), (4, 6), (4, 8), (4, 10), (4, 14),
                            (5, 2), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 14))

            }
    }

    @classmethod
    def play_level(cls, level_number):
        cls.__Level = level_number
        cls.generate_level()
        cls.set_interface()
        threading.Thread(target=cls.enemy_animate, daemon=True).start()

        Main_player.set_default_characters()
        Main_player.player_pack(0, 0)
        Window.bind('<KeyPress>', Main_player.player_action)

    @classmethod
    def level_exit(cls, item):
        Window.unbind('<KeyPress>')
        cls.__bombs_array.clear()
        cls.__Enemy_list.clear()
        cls.Game_canvas.delete('all')
        cls.clear_matrix()
        if item == 'next':
            if cls.__Level < 5:
                cls.play_level(cls.__Level + 1)
            else:
                Window.change_frame(Window.Game_frame, Window.Game_over_frame)
        elif item == 'lose':
            Window.change_frame(Window.Game_frame, Window.Game_over_frame)
        else:
            Window.change_frame(Window.Game_frame, Window.Main_menu_frame)

    @classmethod
    def set_interface(cls):
        cls.Game_canvas.create_window(110, 913, anchor='nw', width=622, height=87,
                                      window=tkinter.Button(text='Выход в главное меню', bg='#E07A04', fg='#FFD88E',
                                                            font=('impact', 17),
                                                            activeforeground='#FFDF60', activebackground='#BF6A04',
                                                            command=lambda: cls.level_exit('exit')
                                                            )
                                      )
        cls.Game_canvas.create_image(0, 0, anchor='nw', image=Window.img['interface'])
        cls.__Empy_heart_list.clear()
        cls.__labels.clear()

        cls.__item_counter['max_bomb'] = 0
        cls.__item_counter['speed'] = 0
        cls.__item_counter['bomb_range'] = 0
        if cls.__Level == 1:
            cls.__item_counter['score'] = 0

        cls.__labels['max_bomb'] = cls.Game_canvas.create_text(545, 240, text=str(cls.__item_counter['max_bomb']), font='Impact 12', fill='#B06003')
        cls.__labels['speed'] = cls.Game_canvas.create_text(635, 240, text=str(cls.__item_counter['speed']), font='Impact 12', fill='#B06003')
        cls.__labels['bomb_range'] = cls.Game_canvas.create_text(730, 240, text=str(cls.__item_counter['bomb_range']), font='Impact 12', fill='#B06003')
        cls.__labels['score'] = cls.Game_canvas.create_text(1460, 150, text='Счет:'+str(cls.__item_counter['score']), font='Impact 45', fill='#B06003')

    @classmethod
    def generate_level(cls):
        cls.Game_canvas.create_image(100, 290, anchor='nw', image=Window.img['field'][cls.__Level])

        for i in range(len(cls.Game_matrix)):
            for j in range(len(cls.Game_matrix[i])):
                if (i, j) in cls.__Level_hash[cls.__Level]['undestroyable']:
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0], anchor='center', image=Window.img['und_des_wal'][cls.__Level])
                    cls.Game_matrix[i][j][2] = 'undestroyable'
                elif (i, j) in cls.__Level_hash[cls.__Level]['destroyable']:
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0], anchor='center', image=Window.img['des_wal'][cls.__Level])
                    cls.Game_matrix[i][j][2] = 'destroyable'

        cls.__exit_item['i'], cls.__exit_item['j'] = random.choice(cls.__Level_hash[cls.__Level]['destroyable'])
        cls.__exit_item['image_item'] = 0
        cls.__exit_item['state'] = 'NotSpawn'

        match cls.__Level:
            case 1:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['slime'], 0, 5, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], 0, 11, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], 5, 11, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], 3, 16, 0.06, 0.2)])
            case 2:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['green_slime'], 1, 4, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], 1, 10, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], 1, 16, 0.06, 0.17),
                                         Enemy(Window.img['animation']['skeleton'], 4, 7, 0.06, 0.07),
                                         Enemy(Window.img['animation']['skeleton'], 5, 13, 0.06, 0.07)])
            case 3:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['zombie'], 3, 1, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], 0, 9, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], 5, 6, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], 3, 16, 0.05, 0.13),
                                         Enemy(Window.img['animation']['green_slime'], 0, 6, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], 5, 9, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], 3, 15, 0.06, 0.17)])
            case 4:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['slime'], 4, 0, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], 3, 16, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], 5, 9, 0.06, 0.2),
                                         Enemy(Window.img['animation']['zombie'], 2, 3, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], 0, 13, 0.05, 0.13),
                                         Enemy(Window.img['animation']['skeleton'], 3, 7, 0.06, 0.07),
                                         Enemy(Window.img['animation']['skeleton'], 5, 8, 0.06, 0.07)])
            case 5:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['lava_slime'], 4, 0, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], 0, 4, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], 4, 16, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], 5, 12, 0.06, 0.1),
                                         Enemy(Window.img['animation']['wither'], 3, 6, 0.06, 0.05),
                                         Enemy(Window.img['animation']['wither'], 3, 8, 0.06, 0.05),
                                         Enemy(Window.img['animation']['wither'], 3, 10, 0.06, 0.05)])


    @classmethod
    def enemy_animate(cls):
        for enemy in cls.__Enemy_list:
            enemy.entity_pack()

        while cls.__Enemy_list:
            for enemy in cls.__Enemy_list:
                if Main_player.collidirect(*enemy.get_cords(), ranges=40):
                    Main_player.get_hit()
                threading.Thread(target=enemy.enemy_moving, daemon=True).start()

    @classmethod
    def pack_enpy_heart(cls):
        if len(cls.__Empy_heart_list) == 0:
            cls.__Empy_heart_list.append(cls.Game_canvas.create_image(690, 95, image=Window.img['empy_heart']))
        else:
            cls.__Empy_heart_list.append(cls.Game_canvas.create_image(600, 95, image=Window.img['empy_heart']))

    @classmethod
    def move_is_correct(cls, p_i, p_j):
        if (0 <= p_i < 6) and (0 <= p_j < 17) and not (cls.Game_matrix[p_i][p_j][2] in ('undestroyable', 'destroyable')):
            return True
        else:
            return False

    @classmethod
    def check_for_exit_level(cls, player_i, player_j):
        if ((player_i, player_j) == (cls.__exit_item['i'], cls.__exit_item['j'])) and cls.__exit_item['state'] == 'active':
            cls.level_exit('next')

    @classmethod
    def spaun_power(cls, i, j):
        if (i, j) != (cls.__exit_item['i'], cls.__exit_item['j']):
            match random.randint(1, 16):
                case 4:
                    cls.Game_matrix[i][j][2] = 'HP'
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0],
                                                                            image=Window.img['powers']['HP'])
                case 8:
                    cls.Game_matrix[i][j][2] = 'max_bomb'
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0],
                                                                            image=Window.img['powers']['max_bomb'])
                case 12:
                    cls.Game_matrix[i][j][2] = 'bomb_range'
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0],
                                                                            image=Window.img['powers']['bomb_range'])
                case 16:
                    cls.Game_matrix[i][j][2] = 'speed'
                    cls.Game_matrix[i][j][1] = cls.Game_canvas.create_image(*cls.Game_matrix[i][j][0],
                                                                            image=Window.img['powers']['speed'])

    @classmethod
    def collect_powers(cls, player_i, player_j):
        if cls.Game_matrix[player_i][player_j][2] != '':
            match cls.Game_matrix[player_i][player_j][2]:
                case 'HP':
                    if Main_player.get_characters('HP') < 3:
                        Main_player.set_characters('HP', 1)
                        cls.Game_canvas.delete(cls.__Empy_heart_list.pop())
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''

                case 'max_bomb':
                    Main_player.set_characters('max_bomb', 1)
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''

                    cls.__item_counter['max_bomb'] += 1
                    cls.Game_canvas.delete(cls.__labels['max_bomb'])
                    cls.__labels['max_bomb'] = cls.Game_canvas.create_text(545, 240, text=str(cls.__item_counter['max_bomb']), font='Impact 12', fill='#B06003')

                case 'speed':
                    if Main_player.get_characters('speed') > 0.01:
                        Main_player.set_characters('speed', -0.005)
                        
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''

                    cls.__item_counter['speed'] += 1
                    cls.Game_canvas.delete(cls.__labels['speed'])
                    cls.__labels['speed'] = cls.Game_canvas.create_text(635, 240, text=str(cls.__item_counter['speed']), font='Impact 12', fill='#B06003')

                case 'bomb_range':
                    Main_player.set_characters('bomb_range', 1)
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''

                    cls.__item_counter['bomb_range'] += 1
                    cls.Game_canvas.delete(cls.__labels['bomb_range'])
                    cls.__labels['bomb_range'] = cls.Game_canvas.create_text(730, 240, text=str(cls.__item_counter['bomb_range']), font='Impact 12', fill='#B06003')

    @classmethod
    def explotions(cls, bomb_i, bomb_j):
        if len(cls.__bombs_array) != 0:
            bomb_range = Main_player.get_characters('bomb_range')
            array_for_entity_killing = list()
            for i in range(bomb_i, bomb_i + bomb_range + 1):
                if (i < 6) and (cls.Game_matrix[i][bomb_j][2] != 'undestroyable'):
                    array_for_entity_killing.append((i, bomb_j))
                    if cls.Game_matrix[i][bomb_j][2] == 'destroyable':
                        cls.Game_canvas.delete(cls.Game_matrix[i][bomb_j][1])
                        cls.Game_matrix[i][bomb_j][1] = 0
                        cls.Game_matrix[i][bomb_j][2] = ''
                        cls.__item_counter['score'] += 100 * cls.__Level
                        cls.spaun_power(i, bomb_j)
                        break
                else:
                    break

            for i in range(bomb_i - 1, bomb_i - bomb_range - 1, -1):
                if (i >= 0) and (cls.Game_matrix[i][bomb_j][2] != 'undestroyable'):
                    array_for_entity_killing.append((i, bomb_j))
                    if cls.Game_matrix[i][bomb_j][2] == 'destroyable':
                        cls.Game_canvas.delete(cls.Game_matrix[i][bomb_j][1])
                        cls.Game_matrix[i][bomb_j][1] = 0
                        cls.Game_matrix[i][bomb_j][2] = ''
                        cls.__item_counter['score'] += 100 * cls.__Level
                        cls.spaun_power(i, bomb_j)
                        break
                else:
                    break

            for j in range(bomb_j + 1, bomb_j + bomb_range + 1):
                if (j < 17) and (cls.Game_matrix[bomb_i][j][2] != 'undestroyable'):
                    array_for_entity_killing.append((bomb_i, j))
                    if cls.Game_matrix[bomb_i][j][2] == 'destroyable':
                        cls.Game_canvas.delete(cls.Game_matrix[bomb_i][j][1])
                        cls.Game_matrix[bomb_i][j][1] = 0
                        cls.Game_matrix[bomb_i][j][2] = ''
                        cls.__item_counter['score'] += 100 * cls.__Level
                        cls.spaun_power(bomb_i, j)
                        break
                else:
                    break

            for j in range(bomb_j - 1, bomb_j - bomb_range - 1, -1):
                if (j >= 0) and (cls.Game_matrix[bomb_i][j][2] != 'undestroyable'):
                    array_for_entity_killing.append((bomb_i, j))
                    if cls.Game_matrix[bomb_i][j][2] == 'destroyable':
                        cls.Game_canvas.delete(cls.Game_matrix[bomb_i][j][1])
                        cls.Game_matrix[bomb_i][j][1] = 0
                        cls.Game_matrix[bomb_i][j][2] = ''
                        cls.__item_counter['score'] += 100 * cls.__Level
                        cls.spaun_power(bomb_i, j)
                        break
                else:
                    break

            player_has_hit = False  # Костыль для того, чтобы если бомба затрагивает клетку 0:0 урон при респе не был 2Х
            for explocions_cords in array_for_entity_killing:
                expl_x, expl_y = cls.Game_matrix[explocions_cords[0]][explocions_cords[1]][0]
                if Main_player.collidirect(expl_x, expl_y, 70) and not player_has_hit:
                    Main_player.get_hit()
                    player_has_hit = True
                for enemy in cls.__Enemy_list:
                    if enemy.collidirect(expl_x, expl_y, 60):
                        cls.__item_counter['score'] += 300 * cls.__Level
                        enemy.get_hit()
                        cls.__Enemy_list.remove(enemy)

            if ((cls.Game_matrix[cls.__exit_item['i']][cls.__exit_item['j']][1] == 0)
                    and (cls.__exit_item['state'] == 'NotSpawn')):
                cls.__exit_item['image_item'] = cls.Game_canvas.create_image(
                    *cls.Game_matrix[cls.__exit_item['i']][cls.__exit_item['j']][0],
                    image=Window.img['exit']['not_active'])
                cls.__exit_item['state'] = 'NotActive'

            if (not cls.__Enemy_list) and (cls.__exit_item['state'] == 'NotActive'):
                cls.Game_canvas.delete(cls.__exit_item['image_item'])
                cls.__exit_item['image_item'] = cls.Game_canvas.create_image(
                    *cls.Game_matrix[cls.__exit_item['i']][cls.__exit_item['j']][0],
                    image=Window.img['exit']['active'])
                cls.__exit_item['state'] = 'active'

            if cls.__bombs_array:
                PlayingField.Game_canvas.delete(cls.__bombs_array.pop(0))

            cls.Game_canvas.delete(cls.__labels['score'])
            cls.__labels['score'] = cls.Game_canvas.create_text(1460, 150, text='Счет:' + str(cls.__item_counter['score']), font='Impact 45', fill='#B06003')

    @classmethod
    def bomb_has_been_planted(cls, player_i, player_j):
        if len(cls.__bombs_array) < Main_player.get_characters('max_bomb'):
            cls.__bombs_array.append(cls.Game_canvas.create_image(*cls.Game_matrix[player_i][player_j][0], anchor='center', image=Window.img['bomb']))
            Window.after(1200, lambda: cls.explotions(player_i, player_j))


class Entity:
    """ Класс для различных существ - игрока и врагов"""

    def __init__(self, animation_dict, matrix_pos_i=0, matrix_pos_j=0):
        self.matrix_pos = {'i': matrix_pos_i, 'j': matrix_pos_j}
        self.cords = {'x': -1, 'y': -1}

        self.animation = animation_dict
        self.image_item = None

        self.orientation = 'right'
        self.on_moving = False
        self.hit = False

    def entity_pack(self, pos_i=None, pos_j=None):
        if pos_i is not None:
            self.matrix_pos['i'] = pos_i
            self.matrix_pos['j'] = pos_j

        self.cords['x'], self.cords['y'] = PlayingField.Game_matrix[self.matrix_pos['i']][self.matrix_pos['j']][0]
        self.image_item = PlayingField.Game_canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation['right'][-1])
        self.orientation = 'right'
        self.on_moving = False
        self.hit = False

    def get_cords(self):
        return self.cords['x'], self.cords['y']

    def collidirect(self, dg_x, dg_y, ranges):
        if (dg_x - ranges < self.cords['x'] < dg_x + ranges) and (dg_y - ranges < self.cords['y'] < dg_y + ranges):
            return True
        else:
            return False


class Enemy(Entity):
    def __init__(self, animation_dict, matrix_pos_i, matrix_pos_j, speed, caldown):
        super().__init__(animation_dict, matrix_pos_i, matrix_pos_j)
        self.speed = speed
        self.caldown = caldown

    def __del__(self):
        PlayingField.Game_canvas.delete(self.image_item)

    def enemy_moving(self):
        if not self.on_moving:
            correct_moves = list()
            if (PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] + 1) and
                    not (self.matrix_pos['i'] == self.matrix_pos['j'] + 1 == 0)):
                correct_moves.append((100, 'right', 'x', 'j'))

            if (PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] - 1) and
                    not (self.matrix_pos['i'] == self.matrix_pos['j'] - 1 == 0)):
                correct_moves.append((-100, 'left', 'x', 'j'))

            if (PlayingField.move_is_correct(self.matrix_pos['i'] - 1, self.matrix_pos['j']) and
                    not (self.matrix_pos['i'] - 1 == self.matrix_pos['j'] == 0)):
                correct_moves.append((-100, self.orientation, 'y', 'i'))

            if (PlayingField.move_is_correct(self.matrix_pos['i'] + 1, self.matrix_pos['j']) and
                    not (self.matrix_pos['i'] + 1 == self.matrix_pos['j'] == 0)):
                correct_moves.append((100, self.orientation, 'y', 'i'))

            distance, vector, cord, m_pos = random.choice(correct_moves)

            self.on_moving = True
            self.matrix_pos[m_pos] += 1 if distance > 0 else -1

            dist = distance / len(self.animation[vector])
            for i in range(len(self.animation[vector])):
                if not self.hit:
                    self.cords[cord] += dist
                    deleting_image = self.image_item
                    self.image_item = PlayingField.Game_canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation[vector][i])
                    PlayingField.Game_canvas.delete(deleting_image)
                    sleep(self.speed)
                else:
                    break
            else:
                sleep(self.caldown)
                self.on_moving = False
                self.orientation = vector

    def get_hit(self):
        self.hit = True


class Player(Entity):
    """ Класс игрока """

    def __init__(self, animation_dict):
        super().__init__(animation_dict)
        self.characters = {'HP': -1, 'max_bomb': -1, 'speed': -1.0, 'bomb_range': -1}
        self.packing = True

    def player_pack(self, pos_i, pos_j):
        self.entity_pack(pos_i, pos_j)
        self.packing = False

    def set_characters(self, charc, value):
        self.characters[charc] += value

    def get_characters(self, charc):
        return self.characters[charc]

    def player_moving(self, distance, vector, cord, m_pos):
        if not self.on_moving:
            self.on_moving = True
            self.matrix_pos[m_pos] += 1 if distance > 0 else -1

            dist = distance / len(self.animation[vector])
            for i in range(len(self.animation[vector])):
                if not self.hit:
                    self.cords[cord] += dist
                    deleting_image = self.image_item
                    self.image_item = PlayingField.Game_canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation[vector][i])
                    PlayingField.Game_canvas.delete(deleting_image)
                    sleep(self.characters['speed'])
                else:
                    PlayingField.Game_canvas.delete(self.image_item)
                    if self.characters['HP'] > 0:
                        self.player_pack(0, 0)
                    else:
                        PlayingField.level_exit('lose')
                    break
            else:
                if not self.hit:
                    PlayingField.check_for_exit_level(self.matrix_pos['i'], self.matrix_pos['j'])
                    self.on_moving = False
                    self.orientation = vector
                    PlayingField.collect_powers(self.matrix_pos['i'], self.matrix_pos['j'])

                else:
                    PlayingField.Game_canvas.delete(self.image_item)
                    if self.characters['HP'] > 0:
                        self.player_pack(0, 0)
                    else:
                        PlayingField.level_exit('lose')

    def get_hit(self):
        if not self.packing:    # Костыль для того, чтобы при столкновении с противниками урон от них не был 100000xx
            self.packing = True
            PlayingField.pack_enpy_heart()

            self.characters['HP'] -= 1
            if self.on_moving:
                self.hit = True
            else:
                PlayingField.Game_canvas.delete(self.image_item)
                if self.characters['HP'] > 0:
                    self.player_pack(0, 0)
                else:
                    PlayingField.level_exit('lose')

    def player_action(self, event):
        if (event.char.lower() in ('d', 'в')) and PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] + 1):
            threading.Thread(target=self.player_moving, args=(100, 'right', 'x', 'j'), daemon=True).start()

        elif (event.char.lower() in ('a', 'ф')) and PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] - 1):
            threading.Thread(target=self.player_moving, args=(-100, 'left', 'x', 'j'), daemon=True).start()

        elif (event.char.lower() in ('w', 'ц')) and PlayingField.move_is_correct(self.matrix_pos['i'] - 1, self.matrix_pos['j']):
            threading.Thread(target=self.player_moving, args=(-100, self.orientation, 'y', 'i'), daemon=True).start()

        elif (event.char.lower() in ('s', 'ы')) and PlayingField.move_is_correct(self.matrix_pos['i'] + 1, self.matrix_pos['j']):
            threading.Thread(target=self.player_moving, args=(100, self.orientation, 'y', 'i'), daemon=True).start()

        elif event.char.lower() in ('e', 'у'):
            PlayingField.bomb_has_been_planted(self.matrix_pos['i'], self.matrix_pos['j'])

    def set_default_characters(self):
        self.characters['HP'] = 3
        self.characters['speed'] = 0.04
        self.characters['max_bomb'] = 1
        self.characters['bomb_range'] = 1


Main_player = Player(Window.img['animation']['player'])

if __name__ == '__main__':
    Window.mainloop()
