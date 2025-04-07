import json
import tkinter
from tkinter import ttk
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
            'interface': {
                    'menu': tkinter.PhotoImage(file='Images/interface/menu_bg.png'),
                    'records': tkinter.PhotoImage(file='Images/interface/Records_bg.png'),
                    'settings': tkinter.PhotoImage(file='Images/interface/Settings_bg.png'),
                    'game_interface': tkinter.PhotoImage(file='Images/interface/interface.png'),
                    'empy_heart': tkinter.PhotoImage(file='Images/interface/empy_heart.png'),
                    'int_bg': tkinter.PhotoImage(file='Images/interface/interface_bg.png'),
                    'win': tkinter.PhotoImage(file='Images/interface/win.png'),
                    'lose': tkinter.PhotoImage(file='Images/interface/lose.png'),
            },
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
            },
            'bomb': tkinter.PhotoImage(file='Images/PlayingField/bomb.png'),
        }
        self.iconphoto(False, self.img['bomb'])
        self.H = self.winfo_height()
        self.W = self.winfo_width()
        self.minsize(self.W, self.H)




        self.Game_frame = tkinter.Frame(master=self, background='black')
        self.Main_menu_frame = tkinter.Frame(master=self, width=1920, height=1080)
        self.__Menu_canvas = tkinter.Canvas(master=self.Main_menu_frame, width=self.W, height=self.H)
        self.__Menu_canvas.pack(anchor='nw')
        self.__Menu_canvas.create_image(0, 0, anchor='nw', image=self.img['interface']['menu'])

        self.__Menu_canvas.create_window(self.W // 2, self.H - 160, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Выход', width=80, height=2, bg='#B35514', command=exit,
            font=('impact', 17), activeforeground='#FFDF60', activebackground='#A34D12', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 240, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Рекорды', width=80, height=2, bg='#B85715',
            command=self.open_records_button_function,
            font=('impact', 17), activeforeground='#FFDF60', activebackground='#A85013', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 320, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Настройки', width=80, height=2, bg='#BD5A15',
            command=lambda: self.change_frame(self.Main_menu_frame, self.Options_frame), font=('impact', 17),
            activeforeground='#FFDF60', activebackground='#AD5213', borderwidth=1, fg='#FFD88E'))

        self.__Menu_canvas.create_window(self.W // 2, self.H - 400, anchor='center', window=tkinter.Button(
            master=self.Main_menu_frame, text='Играть', width=80, height=2, bg='#C75E16',
            command=self.play_button, font=('impact', 17),
            activeforeground='#FFDF60', activebackground='#B35514', borderwidth=1, fg='#FFD88E'))

        self.Main_menu_frame.pack()



        self.Game_over_frame = tkinter.Frame(master=self)
        self.Game_over_vidgets = dict()
        self.Game_over_vidgets['canvas'] = tkinter.Canvas(master=self.Game_over_frame, width=self.W, height=self.H)
        self.Game_over_vidgets['quit'] = tkinter.Button(master=self.Game_over_frame, text='Меню', font=('impact', 17),
                                                        bg='#E66C19', activeforeground='#FFDF60',
                                                        activebackground='#B35514', borderwidth=1, fg='#FFD88E',
                                                        command=lambda: self.change_frame(self.Game_over_frame,
                                                                                          self.Main_menu_frame))
        self.Game_over_vidgets['result_image'] = 0
        self.Game_over_vidgets['score_image'] = 0
        self.Game_over_vidgets['player_score'] = 0
        self.Game_over_vidgets['entry'] = tkinter.Entry(master=self.Game_over_frame, font=('impact', 17), bg='#C75E16',
                                                        justify='center', fg='#FFD88E')
        self.Game_over_vidgets['save'] = tkinter.Button(master=self.Game_over_frame, text='Сохранить результат',
                                                        font=('impact', 17), width=80, height=2,
                                                        activeforeground='#FFDF60', activebackground='#A34D12',
                                                        borderwidth=1, fg='#FFD88E', bg='#E66C19',
                                                        command=self.save_records_button_function)

        self.Game_over_vidgets['canvas'].create_image(0, 0, anchor='nw', image=self.img['interface']['int_bg'])
        self.Game_over_vidgets['canvas'].create_window(self.W // 2 - 730, self.H // 2 - 300, width=100, height=50,
                                                       anchor='center', window=self.Game_over_vidgets['quit'])

        self.Game_over_vidgets['canvas'].create_window(self.W // 2, self.H // 2 + 132, width=890, height=70,
                                                       anchor='center', window=self.Game_over_vidgets['entry'])
        self.Game_over_vidgets['canvas'].create_window(self.W // 2, self.H // 2 + 237, anchor='center',
                                                       window=self.Game_over_vidgets['save'])
        self.Game_over_vidgets['canvas'].pack()


        self.Options_frame = tkinter.Frame(master=self)
        self.Options_frame_Vidgets = dict()
        self.Options_frame_Vidgets['canvas'] = tkinter.Canvas(master=self.Options_frame, width=self.W, height=self.H)

        self.Options_frame_Vidgets['quit'] = tkinter.Button(master=self.Options_frame, text='Меню', font=('impact', 17),
                                                      bg='#E66C19', activeforeground='#FFDF60',
                                                      activebackground='#B35514', borderwidth=1, fg='#FFD88E',
                                                      command=lambda: self.change_frame(self.Options_frame,
                                                                                        self.Main_menu_frame))

        self.Options_frame_Vidgets['moving_box'] = ttk.Combobox(master=self.Options_frame)
        self.Options_frame_Vidgets['bomb_box'] = ttk.Combobox(master=self.Options_frame)
        self.Options_frame_Vidgets['sound_checkbox'] = tkinter.Checkbutton(master=self.Options_frame)


        self.Options_frame_Vidgets['canvas'].create_image(0, 0, anchor='nw', image=self.img['interface']['settings'])
        self.Options_frame_Vidgets['canvas'].create_window(self.W // 2 - 730, self.H // 2 - 300, width=100, height=50,
                                                     anchor='center', window=self.Options_frame_Vidgets['quit'])

        self.Options_frame_Vidgets['canvas'].create_window(self.W // 2 + 340, self.H // 2 - 2, width=100, height=50,
                                                           anchor='center', window=self.Options_frame_Vidgets['moving_box'])

        self.Options_frame_Vidgets['canvas'].create_window(self.W // 2 + 340, self.H // 2 + 148, width=100, height=50,
                                                           anchor='center', window=self.Options_frame_Vidgets['bomb_box'])

        self.Options_frame_Vidgets['canvas'].create_window(self.W // 2 + 340, self.H // 2 + 290,
                                                           anchor='center', window=self.Options_frame_Vidgets['sound_checkbox'])

        self.Options_frame_Vidgets['canvas'].pack()


        self.Records_frame = tkinter.Frame(master=self)
        self.Records_vidgets = dict()
        self.Records_vidgets['record_search_index'] = 0
        self.Records_vidgets['record_array'] = list()

        self.Records_vidgets['canvas'] = tkinter.Canvas(master=self.Records_frame, width=self.W, height=self.H)
        self.Records_vidgets['quit'] = tkinter.Button(master=self.Records_frame, text='Меню', font=('impact', 17),
                                                        bg='#E66C19', activeforeground='#FFDF60',
                                                        activebackground='#B35514', borderwidth=1, fg='#FFD88E',
                                                        command=lambda: self.change_frame(self.Records_frame,
                                                                                          self.Main_menu_frame))
        self.Records_vidgets['record_label_array'] = [
            tkinter.Label(text='', font=('impact', 17), fg='#C7621E', bg='#FF7D26') for i in range(10)]

        self.Records_vidgets['last_record'] = tkinter.Button(text='Предыдущая страница', bg='#C75E16',
                                                             command=self.last_record_list_button_function,
                                                             font=('impact', 17), activeforeground='#FFDF60',
                                                             activebackground='#B35514', borderwidth=1, fg='#FFD88E')

        self.Records_vidgets['next_record'] = tkinter.Button(text='Следующая страница', bg='#C75E16',
                                                             command=self.next_record_list_button_function,
                                                             font=('impact', 17), activeforeground='#FFDF60',
                                                             activebackground='#B35514', borderwidth=1, fg='#FFD88E')

        self.Records_vidgets['canvas'].create_image(0, 0, anchor='nw', image=self.img['interface']['records'])
        self.Records_vidgets['canvas'].create_window(self.W // 2 - 730, self.H // 2 - 300, width=100, height=50,
                                                       anchor='center', window=self.Records_vidgets['quit'])

        self.Records_vidgets['canvas'].create_window(self.W//2 - 375, self.H - 470, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][0])
        self.Records_vidgets['canvas'].create_window(self.W//2 - 375, self.H - 430, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][1])
        self.Records_vidgets['canvas'].create_window(self.W//2 - 375, self.H - 390, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][2])
        self.Records_vidgets['canvas'].create_window(self.W//2 - 375, self.H - 350, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][3])
        self.Records_vidgets['canvas'].create_window(self.W//2 - 375, self.H - 310, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][4])
        self.Records_vidgets['canvas'].create_window(self.W//2 + 10, self.H - 470, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][5])
        self.Records_vidgets['canvas'].create_window(self.W//2 + 10, self.H - 430, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][6])
        self.Records_vidgets['canvas'].create_window(self.W//2 + 10, self.H - 390, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][7])
        self.Records_vidgets['canvas'].create_window(self.W//2 + 10, self.H - 350, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][8])
        self.Records_vidgets['canvas'].create_window(self.W//2 + 10, self.H - 310, anchor='nw',
                                                     window=self.Records_vidgets['record_label_array'][9])


        self.Records_vidgets['canvas'].create_window(self.W//2 + 225, self.H - 150, anchor='center', width=400,
                                                     height=70, window=self.Records_vidgets['next_record'])
        self.Records_vidgets['canvas'].create_window(self.W//2 - 225, self.H - 150, anchor='center', width=400,
                                                     height=70, window=self.Records_vidgets['last_record'])

        self.Records_vidgets['canvas'].pack()

    def change_frame(self, frame1, frame2):
        frame1.forget()
        frame2.pack(fill='both')

    def play_button(self):
        self.Main_menu_frame.forget()
        self.Game_frame.pack(fill='both')
        PlayingField.play_level(1)

    def load_end_screen(self, result, score):
        self.change_frame(Window.Game_frame, Window.Game_over_frame)
        self.Game_over_vidgets['canvas'].delete(self.Game_over_vidgets['result_image'])
        self.Game_over_vidgets['canvas'].delete(self.Game_over_vidgets['score_image'])
        self.Game_over_vidgets['entry'].delete(0, tkinter.END)
        self.Game_over_vidgets['result_image'] = self.Game_over_vidgets['canvas'].create_image(self.W // 2, self.H // 2 - 130, anchor='center',
                                                      image=self.img['interface'][result])
        self.Game_over_vidgets['score_image'] = self.Game_over_vidgets['canvas'].create_text(self.W // 2, self.H // 2 + 27,
                                                     text='Ваш счет: ' + str(score), font='impact 45', fill='#87410E')
        self.Game_over_vidgets['player_score'] = score

    def save_records_button_function(self):
        name = self.Game_over_vidgets['entry'].get()
        name = name[:16] + '...' if len(name) > 15 else name
        score = self.Game_over_vidgets['player_score']

        with open('Records.json', 'r') as record_file:
            record_list = json.load(record_file)
            for i in range(len(record_list)):
                if score > record_list[i]['score']:
                    record_list.insert(i, {'record_string': f'{name}: {score}', 'score': score})
                    break
            else:
                record_list.append({'record_string': f'{name}: {score}', 'score': score})
        with open('Records.json', 'w') as record_file:
            json.dump(record_list, record_file, indent=2)
        self.change_frame(self.Game_over_frame, self.Main_menu_frame)

    def open_records_button_function(self):
        self.change_frame(self.Main_menu_frame, self.Records_frame)
        self.Records_vidgets['record_search_index'] = 0
        with open('Records.json', 'r') as record_file:
            self.Records_vidgets['record_array'] = json.load(record_file)

        rindex = 0
        for i in range(10):
            if rindex < len(self.Records_vidgets['record_array']):
                self.Records_vidgets['record_label_array'][i]['text'] = ' '.join(
                    [f'{rindex+1}.', self.Records_vidgets['record_array'][rindex]['record_string']])
            else:
                self.Records_vidgets['record_label_array'][i]['text'] = ''
            rindex += 1

    def next_record_list_button_function(self):
        if self.Records_vidgets['record_search_index'] + 10 < len(self.Records_vidgets['record_array']):
            self.Records_vidgets['record_search_index'] += 10
            rindex = self.Records_vidgets['record_search_index']
            for i in range(10):
                if rindex < len(self.Records_vidgets['record_array']):
                    self.Records_vidgets['record_label_array'][i]['text'] = ' '.join(
                        [f'{rindex + 1}.', self.Records_vidgets['record_array'][rindex]['record_string']])
                else:
                    self.Records_vidgets['record_label_array'][i]['text'] = ''
                rindex += 1

    def last_record_list_button_function(self):
        if self.Records_vidgets['record_search_index'] > 0:
            self.Records_vidgets['record_search_index'] -= 10
            rindex = self.Records_vidgets['record_search_index']
            for i in range(10):
                if rindex < len(self.Records_vidgets['record_array']):
                    self.Records_vidgets['record_label_array'][i]['text'] = ' '.join(
                        [f'{rindex + 1}.', self.Records_vidgets['record_array'][rindex]['record_string']])
                else:
                    self.Records_vidgets['record_label_array'][i]['text'] = ''
                rindex += 1


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

    __labels = {
                'max_bomb': tkinter.Label(text=0, font=('Impact', '12'), fg='#B06003', bg='#F78804'),
                'speed': tkinter.Label(text=0, font=('Impact', '12'), fg='#B06003', bg='#F78804'),
                'bomb_range': tkinter.Label(text=0, font=('Impact', '12'), fg='#B06003', bg='#F78804'),
                'score': tkinter.Label(text='Счет: 0', font=('Impact', '45'), fg='#B06003', bg='#F78804')
                }

    __exit_item = {'i': 0, 'j': 0, 'image_item': 0, 'state': 'NotSpawn'}
    __Level = 0
    __Level_mane = {
        1: 'Скользкая тропа',
        2: 'Колючая долина',
        3: 'Ледяной острог',
        4: 'Жуткие поля',
        5: 'Пылающая крепость'
    }
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
        Main_player.entity_pack(0, 0)
        Window.bind('<KeyPress>', Main_player.player_action)

    @classmethod
    def set_interface(cls):
        cls.Game_canvas.create_window(110, 913, anchor='nw', width=622, height=87,
                                      window=tkinter.Button(text='Выход в главное меню', bg='#E07A04', fg='#FFD88E',
                                                            font=('impact', 17),
                                                            activeforeground='#FFDF60', activebackground='#BF6A04',
                                                            command=lambda: cls.level_exit('exit')
                                                            )
                                      )
        cls.Game_canvas.create_image(0, 0, anchor='nw', image=Window.img['interface']['game_interface'])
        cls.__Empy_heart_list.clear()

        cls.__labels['max_bomb']['text'] = 0
        cls.__labels['speed']['text'] = 0
        cls.__labels['bomb_range']['text'] = 0
        if cls.__Level == 1:
            cls.__labels['score']['text'] = 'Счет: 0'

        cls.Game_canvas.create_window(555, 241, window=cls.__labels['max_bomb'])
        cls.Game_canvas.create_window(645, 241, window=cls.__labels['speed'])
        cls.Game_canvas.create_window(740, 241, window=cls.__labels['bomb_range'])
        cls.Game_canvas.create_window(1465, 150, window=cls.__labels['score'])

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
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['slime'], cls.Game_canvas, 0, 5, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], cls.Game_canvas, 0, 11, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], cls.Game_canvas, 5, 11, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], cls.Game_canvas, 3, 16, 0.06, 0.2)])
            case 2:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 1, 4, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 1, 10, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 1, 16, 0.06, 0.17),
                                         Enemy(Window.img['animation']['skeleton'], cls.Game_canvas, 4, 7, 0.06, 0.07),
                                         Enemy(Window.img['animation']['skeleton'], cls.Game_canvas, 5, 13, 0.06, 0.07)])
            case 3:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 3, 1, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 0, 9, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 5, 6, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 3, 16, 0.05, 0.13),
                                         Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 0, 6, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 5, 9, 0.06, 0.17),
                                         Enemy(Window.img['animation']['green_slime'], cls.Game_canvas, 3, 15, 0.06, 0.17)])
            case 4:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['slime'], cls.Game_canvas, 4, 0, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], cls.Game_canvas, 3, 16, 0.06, 0.2),
                                         Enemy(Window.img['animation']['slime'], cls.Game_canvas, 5, 9, 0.06, 0.2),
                                         Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 2, 3, 0.05, 0.13),
                                         Enemy(Window.img['animation']['zombie'], cls.Game_canvas, 0, 13, 0.05, 0.13),
                                         Enemy(Window.img['animation']['skeleton'], cls.Game_canvas, 3, 7, 0.06, 0.07),
                                         Enemy(Window.img['animation']['skeleton'], cls.Game_canvas, 5, 8, 0.06, 0.07)])
            case 5:
                cls.__Enemy_list.extend([Enemy(Window.img['animation']['lava_slime'], cls.Game_canvas, 4, 0, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], cls.Game_canvas, 0, 4, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], cls.Game_canvas, 4, 16, 0.06, 0.1),
                                         Enemy(Window.img['animation']['lava_slime'], cls.Game_canvas, 5, 12, 0.06, 0.1),
                                         Enemy(Window.img['animation']['wither'], cls.Game_canvas, 3, 6, 0.06, 0.05),
                                         Enemy(Window.img['animation']['wither'], cls.Game_canvas, 3, 8, 0.06, 0.05),
                                         Enemy(Window.img['animation']['wither'], cls.Game_canvas, 3, 10, 0.06, 0.05)])

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
            cls.__Empy_heart_list.append(cls.Game_canvas.create_image(690, 95, image=Window.img['interface']['empy_heart']))
        else:
            cls.__Empy_heart_list.append(cls.Game_canvas.create_image(600, 95, image=Window.img['interface']['empy_heart']))

    @classmethod
    def level_exit(cls, item):
        Window.unbind('<KeyPress>')
        cls.__bombs_array.clear()
        cls.__Enemy_list.clear()
        cls.Game_canvas.delete('all')
        cls.clear_matrix()

        if item == 'lose':
            Window.load_end_screen('lose', int(cls.__labels['score']['text'][cls.__labels['score']['text'].index(' ') + 1:]))
        elif item == 'exit':
            Window.change_frame(Window.Game_frame, Window.Main_menu_frame)
        elif (item == 'next') and (cls.__Level < 5):
            cls.play_level(cls.__Level + 1)
        else:
            Window.load_end_screen('win', int(cls.__labels['score']['text'][cls.__labels['score']['text'].index(' ') + 1:]))

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
                    cls.__labels['max_bomb']['text'] += 1

                case 'speed':
                    if Main_player.get_characters('speed') > 0.01:
                        Main_player.set_characters('speed', -0.005)
                        
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''
                    cls.__labels['speed']['text'] += 1

                case 'bomb_range':
                    Main_player.set_characters('bomb_range', 1)
                    cls.Game_canvas.delete(cls.Game_matrix[player_i][player_j][1])
                    cls.Game_matrix[player_i][player_j][1], cls.Game_matrix[player_i][player_j][2] = 0, ''
                    cls.__labels['bomb_range']['text'] += 1

    @classmethod
    def explotions(cls, bomb_i, bomb_j):
        if len(cls.__bombs_array) != 0:
            bomb_range = Main_player.get_characters('bomb_range')
            array_for_entity_killing = list()
            score_point = 0
            for i in range(bomb_i, bomb_i + bomb_range + 1):
                if (i < 6) and (cls.Game_matrix[i][bomb_j][2] != 'undestroyable'):
                    array_for_entity_killing.append((i, bomb_j))
                    if cls.Game_matrix[i][bomb_j][2] == 'destroyable':
                        cls.Game_canvas.delete(cls.Game_matrix[i][bomb_j][1])
                        cls.Game_matrix[i][bomb_j][1] = 0
                        cls.Game_matrix[i][bomb_j][2] = ''
                        cls.spaun_power(i, bomb_j)
                        score_point += 100 * cls.__Level
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
                        cls.spaun_power(i, bomb_j)
                        score_point += 100 * cls.__Level
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
                        cls.spaun_power(bomb_i, j)
                        score_point += 100 * cls.__Level
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
                        cls.spaun_power(bomb_i, j)
                        score_point += 100 * cls.__Level
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
                        enemy.get_hit()
                        cls.__Enemy_list.remove(enemy)
                        score_point += 300 * cls.__Level

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

            cls.__labels['score']['text'] = 'Счет: ' + str(int(cls.__labels['score']['text'][cls.__labels['score']['text'].index(' ') + 1:]) + score_point)

    @classmethod
    def bomb_has_been_planted(cls, player_i, player_j):
        if len(cls.__bombs_array) < Main_player.get_characters('max_bomb'):
            cls.__bombs_array.append(cls.Game_canvas.create_image(*cls.Game_matrix[player_i][player_j][0], anchor='center', image=Window.img['bomb']))
            Window.after(1200, lambda: cls.explotions(player_i, player_j))


class Entity:
    """ Класс для различных существ - игрока и врагов"""

    def __init__(self, animation_dict, canvas, matrix_pos_i=0, matrix_pos_j=0):
        self.matrix_pos = {'i': matrix_pos_i, 'j': matrix_pos_j}
        self.cords = {'x': -1, 'y': -1}
        self.canvas = canvas

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
        self.image_item = self.canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation['right'][-1])
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
    def __init__(self, animation_dict, canvas, matrix_pos_i, matrix_pos_j, speed, caldown):
        super().__init__(animation_dict, canvas, matrix_pos_i, matrix_pos_j)
        self.speed = speed
        self.caldown = caldown

    def __del__(self):
        self.canvas.delete(self.image_item)

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
                    self.image_item = self.canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation[vector][i])
                    self.canvas.delete(deleting_image)
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

    def __init__(self, animation_dict, canvas):
        super().__init__(animation_dict, canvas)
        self.characters = {'HP': -1, 'max_bomb': -1, 'speed': -1.0, 'bomb_range': -1}

    def set_characters(self, charc, value):
        self.characters[charc] += value

    def get_characters(self, charc):
        return self.characters[charc]

    def player_moving(self, distance, vector, cord, m_pos):

        self.on_moving = True
        self.matrix_pos[m_pos] += 1 if distance > 0 else -1

        dist = distance / len(self.animation[vector])
        for i in range(len(self.animation[vector])):
            if not self.hit:
                self.cords[cord] += dist
                deleting_image = self.image_item
                self.image_item = self.canvas.create_image(self.cords['x'], self.cords['y'], anchor='center', image=self.animation[vector][i])
                self.canvas.delete(deleting_image)
                sleep(self.characters['speed'])
            else:
                #self.canvas.delete(self.image_item)
                #if self.characters['HP'] > 0:
                #    self.entity_pack(0, 0)
                #else:
                #    PlayingField.level_exit('lose')
                break
        else:
            if not self.hit:
                PlayingField.check_for_exit_level(self.matrix_pos['i'], self.matrix_pos['j'])
                self.on_moving = False
                self.orientation = vector
                PlayingField.collect_powers(self.matrix_pos['i'], self.matrix_pos['j'])

            #else:
            #    self.canvas.delete(self.image_item)
            #    if self.characters['HP'] > 0:
            #        self.entity_pack(0, 0)
            #    else:
             #       PlayingField.level_exit('lose')

    def get_hit(self):
        if not self.hit:
            self.hit = True
            PlayingField.pack_enpy_heart()
            self.characters['HP'] -= 1
            #if not self.on_moving:
            self.canvas.delete(self.image_item)
            if self.characters['HP'] > 0:
                self.entity_pack(0, 0)
            else:
                PlayingField.level_exit('lose')

    def player_action(self, event):
        if (event.char.lower() in ('d', 'в')) and PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] + 1) and not self.on_moving:
            threading.Thread(target=self.player_moving, args=(100, 'right', 'x', 'j'), daemon=True).start()

        elif (event.char.lower() in ('a', 'ф')) and PlayingField.move_is_correct(self.matrix_pos['i'], self.matrix_pos['j'] - 1) and not self.on_moving:
            threading.Thread(target=self.player_moving, args=(-100, 'left', 'x', 'j'), daemon=True).start()

        elif (event.char.lower() in ('w', 'ц')) and PlayingField.move_is_correct(self.matrix_pos['i'] - 1, self.matrix_pos['j']) and not self.on_moving:
            threading.Thread(target=self.player_moving, args=(-100, self.orientation, 'y', 'i'), daemon=True).start()

        elif (event.char.lower() in ('s', 'ы')) and PlayingField.move_is_correct(self.matrix_pos['i'] + 1, self.matrix_pos['j']) and not self.on_moving:
            threading.Thread(target=self.player_moving, args=(100, self.orientation, 'y', 'i'), daemon=True).start()

        elif event.char.lower() in ('e', 'у'):
            PlayingField.bomb_has_been_planted(self.matrix_pos['i'], self.matrix_pos['j'])

    def set_default_characters(self):
        self.characters['HP'] = 3
        self.characters['speed'] = 0.04
        self.characters['max_bomb'] = 1
        self.characters['bomb_range'] = 1


Main_player = Player(Window.img['animation']['player'], PlayingField.Game_canvas)

if __name__ == '__main__':
    Window.mainloop()
