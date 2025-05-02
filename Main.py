import random
import tkinter
from tkinter import messagebox
import threading

import customtkinter as ctk
import playsound

from Background_sound_module import *
from Entity_module import *
from Json_module import *

root = tkinter.Tk()
images = {
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


class MyApplication:
    """ Класс для создания и настройки окна приложения"""

    def __init__(self, rooot, title, window_image):
        # Общие настройки окна
        self.root = rooot
        self.root.title(title)
        self.root.state('zoomed')
        self.root.iconphoto(False, window_image)
        self.H = self.root.winfo_height()
        self.W = self.root.winfo_width()
        self.root.minsize(self.W, self.H)
        self.root.maxsize(self.W, self.H)

        # Настройка формы главного меню и его виджетов
        self.Main_menu_frame = tkinter.Frame(master=self.root, width=1920, height=1080)
        self.Menu_canvas = tkinter.Canvas(master=self.Main_menu_frame, width=self.W, height=self.H)
        self.Menu_canvas.pack(anchor='nw')
        self.Menu_canvas.create_image(0, 0, anchor='nw', image=images['interface']['menu'])

        self.menu_play_button = ctk.CTkButton(
            master=self.Main_menu_frame, text='Играть', width=800, height=80, border_width=5, corner_radius=0,
            font=('Impact', 35), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.play_button_function)

        self.menu_option_button = ctk.CTkButton(
            master=self.Main_menu_frame, text='Настройки', width=800, height=80, border_width=5, corner_radius=0,
            font=('Impact', 35), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.option_button_function)

        self.menu_record_button = ctk.CTkButton(
            master=self.Main_menu_frame, text='Рекорды', width=800, height=80, border_width=5, corner_radius=0,
            font=('Impact', 35), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.records_button_function)

        self.menu_exit_button = ctk.CTkButton(
            master=self.Main_menu_frame, text='Выход', width=800, height=80, border_width=5, corner_radius=0,
            font=('Impact', 35), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=exit)

        self.Menu_canvas.create_window(self.W // 2, self.H - 430, anchor='center', window=self.menu_play_button)
        self.Menu_canvas.create_window(self.W // 2, self.H - 340, anchor='center', window=self.menu_option_button)
        self.Menu_canvas.create_window(self.W // 2, self.H - 250, anchor='center', window=self.menu_record_button)
        self.Menu_canvas.create_window(self.W // 2, self.H - 160, anchor='center', window=self.menu_exit_button)
        self.Main_menu_frame.pack()

        # Настройка формы окна игрового процесса, виджетов, необходимых полей, обесчпечивающих игровой процечч
        self.Game_frame = tkinter.Frame(master=self.root)
        self.Game_canvas = tkinter.Canvas(master=self.Game_frame, width=self.W, height=self.H, bg='black')
        self.Game_labels = dict()
        self.Game_labels['max_bomb_label'] = tkinter.Label(text=0, font=('Impact', '12'), fg='#944810', bg='#F57723')

        self.Game_labels['speed_label'] = tkinter.Label(text=0, font=('Impact', '12'), fg='#944810', bg='#F57723')

        self.Game_labels['bomb_range_label'] = tkinter.Label(text=0, font=('Impact', '12'), fg='#944810', bg='#F57723')

        self.Game_labels['score_label'] = tkinter.Label(text='Счет: 0', font=('Impact', '45'), fg='#944810', bg='#F57723')

        self.Game_exit_button = ctk.CTkButton(
            master=self.Game_frame, text='Выход в главное меню', width=600, height=86, border_width=5, corner_radius=0,
            font=('Impact', 30), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=lambda: self.level_exit('exit'))

        self.Game_canvas.create_image(0, 0, anchor='nw', image=images['interface']['game_interface'])
        self.Game_canvas.create_window(110, 913, anchor='nw', window=self.Game_exit_button)
        self.Game_canvas.create_window(555, 241, window=self.Game_labels['max_bomb_label'])
        self.Game_canvas.create_window(645, 241, window=self.Game_labels['speed_label'])
        self.Game_canvas.create_window(740, 241, window=self.Game_labels['bomb_range_label'])
        self.Game_canvas.create_window(1465, 150, window=self.Game_labels['score_label'])
        self.Game_canvas.pack()

        self.Game_matrix = self.generate_game_matrix()
        self.Game_player = None

        self.Game_active_bomb_list = list()
        self.Game_enemy_list = list()
        self.Game_loosing_heart_list = list()

        self.Game_exit_cords = {'i': 0, 'j': 0}
        self.Game_level = 0
        self.Game_level_hash = get_file_info('Wall_cords.json')

        self.Key_right = 68
        self.Key_left = 65
        self.Key_up = 87
        self.Key_down = 83
        self.Key_bomb = 69

        # Настройка окна завершения игры и его виджетов
        self.End_game_frame = tkinter.Frame(master=self.root)
        self.End_game_canvas = tkinter.Canvas(master=self.End_game_frame, width=self.W, height=self.H)

        self.End_game_head_image = 0
        self.End_game_score_text_image = 0
        self.End_game_quit_button = ctk.CTkButton(
            master=self.End_game_frame, text='Меню', width=100, height=50, border_width=5, corner_radius=0,
            font=('Impact', 25), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.end_game_exit_button_function)

        self.End_game_name_entry = ctk.CTkEntry(
            master=self.End_game_frame, width=800, height=80, border_width=5, corner_radius=0, font=('Impact', 30),
            justify='center', text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C', )

        self.End_game_saving_button = ctk.CTkButton(
            master=self.End_game_frame, text='Сохранить результат', width=800, height=80, border_width=5, corner_radius=0,
            font=('Impact', 30), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.save_records_button_function)

        self.End_game_canvas.create_image(0, 0, anchor='nw', image=images['interface']['int_bg'])
        self.End_game_canvas.create_window(self.W // 2 - 730, self.H // 2 - 300,
                                           anchor='center', window=self.End_game_quit_button)
        self.End_game_canvas.create_window(self.W // 2, self.H // 2 + 132, anchor='center',
                                           window=self.End_game_name_entry)
        self.End_game_canvas.create_window(self.W // 2, self.H // 2 + 237, anchor='center',
                                           window=self.End_game_saving_button)
        self.End_game_canvas.pack()

        # Настройка окна настроек игры и его виджетов
        self.Options_frame = tkinter.Frame(master=self.root)
        self.Options_canvas = tkinter.Canvas(master=self.Options_frame, width=self.W, height=self.H)

        self.Options_quit_button = ctk.CTkButton(
            master=self.Options_frame, text='Меню', width=100, height=50, border_width=5, corner_radius=0,
            font=('Impact', 25), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.option_quit_button_function)

        self.Options_combox_for_move = ctk.CTkComboBox(
            master=root, values=['A | D | W | S', "Left | Right | Up | Down"], state='readonly', justify='center',
            width=400, height=120, corner_radius=15, border_width=5, fg_color='#FF7E27', dropdown_fg_color='#FF7E27',
            border_color='#C7621E', button_color='#C7621E', font=('Impact', 28), dropdown_font=('Impact', 20),
            text_color='#944810', dropdown_text_color='#944810', bg_color='#C7621E',
            dropdown_hover_color='#F27523', command=self.set_moving_keys)
        self.Options_combox_for_move.set('A | D | W | S')

        self.Options_combox_for_planting_bomb = ctk.CTkComboBox(
            master=root, values=['Q', 'E', 'Tab', 'Space', 'CapsLock', 'Shift', 'Ctrl', 'Enter'],
            state='readonly', justify='center', width=400, height=120, corner_radius=15, border_width=5,
            fg_color='#FF7E27', dropdown_fg_color='#FF7E27', border_color='#C7621E', button_color='#C7621E',
            font=('Impact', 28), dropdown_font=('Impact', 20), text_color='#944810', dropdown_text_color='#944810',
            bg_color='#C7621E', dropdown_hover_color='#F27523', command=self.set_planting_bomb_keys)
        self.Options_combox_for_planting_bomb.set('E')

        self.Options_checkbox_for_sound = ctk.CTkCheckBox(
            master=root,  checkbox_width=100, text='', checkbox_height=100, border_width=10, border_color='#FF7E27',
            hover_color='#F27523', fg_color='#FF7E27', text_color='#BA5C1C', checkmark_color='#BA5C1C', corner_radius=20,
            bg_color='#C7621E')
        self.Options_checkbox_for_sound.select(1)

        self.Options_canvas.create_image(0, 0, anchor='nw', image=images['interface']['settings'])
        self.Options_canvas.create_window(self.W // 2 - 730, self.H // 2 - 300, width=100, height=50,
                                          anchor='center', window=self.Options_quit_button)

        self.Options_canvas.create_window(self.W // 2 + 331, self.H // 2 + 21, anchor='center',
                                          window=self.Options_combox_for_move)

        self.Options_canvas.create_window(self.W // 2 + 331, self.H // 2 + 171, anchor='center',
                                          window=self.Options_combox_for_planting_bomb)

        self.Options_canvas.create_window(self.W // 2 + 197, self.H // 2 + 321, anchor='center',
                                          window=self.Options_checkbox_for_sound)

        self.Options_canvas.pack()

        # Настройка окна рекордов игры и его виджетов
        self.Records_frame = tkinter.Frame(master=self.root)
        self.Records_canvas = tkinter.Canvas(master=self.Records_frame, width=self.W, height=self.H)
        self.Records_search_index = 0
        self.Record_list = list()

        self.Records_quit_button = ctk.CTkButton(
            master=self.Records_frame, text='Меню', width=100, height=50, border_width=5, corner_radius=0,
            font=('Impact', 25), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.record_quit_button_function)
        self.Record_label_list = [tkinter.Label(text='', font=('impact', 17), fg='#944810', bg='#FF7D26') for _ in range(10)]

        self.Record_last_page_button = ctk.CTkButton(
            master=self.Records_frame, text='Предыдущая страница', width=500, height=70, border_width=5, corner_radius=0,
            font=('Impact', 25), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.last_page_button_function)

        self.Record_next_page_button = ctk.CTkButton(
            master=self.Records_frame, text='Следующая страница', width=500, height=70, border_width=5, corner_radius=0,
            font=('Impact', 25), text_color='#944810', fg_color='#F57B2A', border_color='#BA5C1C',
            hover_color='#FF802C', command=self.next_page_button_function)

        self.Records_canvas.create_image(0, 0, anchor='nw', image=images['interface']['records'])
        self.Records_canvas.create_window(self.W // 2 - 730, self.H // 2 - 300, width=100, height=50,
                                          anchor='center', window=self.Records_quit_button)

        self.Records_canvas.create_window(self.W // 2 - 525, self.H - 470, anchor='nw', window=self.Record_label_list[0])
        self.Records_canvas.create_window(self.W // 2 - 525, self.H - 430, anchor='nw', window=self.Record_label_list[1])
        self.Records_canvas.create_window(self.W // 2 - 525, self.H - 390, anchor='nw', window=self.Record_label_list[2])
        self.Records_canvas.create_window(self.W // 2 - 525, self.H - 350, anchor='nw', window=self.Record_label_list[3])
        self.Records_canvas.create_window(self.W // 2 - 525, self.H - 310, anchor='nw', window=self.Record_label_list[4])
        self.Records_canvas.create_window(self.W // 2 + 10, self.H - 470, anchor='nw', window=self.Record_label_list[5])
        self.Records_canvas.create_window(self.W // 2 + 10, self.H - 430, anchor='nw', window=self.Record_label_list[6])
        self.Records_canvas.create_window(self.W // 2 + 10, self.H - 390, anchor='nw', window=self.Record_label_list[7])
        self.Records_canvas.create_window(self.W // 2 + 10, self.H - 350, anchor='nw', window=self.Record_label_list[8])
        self.Records_canvas.create_window(self.W // 2 + 10, self.H - 310, anchor='nw', window=self.Record_label_list[9])

        self.Records_canvas.create_window(self.W // 2 + 270, self.H - 150, anchor='center', window=self.Record_next_page_button)
        self.Records_canvas.create_window(self.W // 2 - 300, self.H - 150, anchor='center', window=self.Record_last_page_button)
        self.Records_canvas.pack()

    # Запуск окна приложения
    def run(self):
        self.root.mainloop()

    # Методы-команды для виджетов главного меню
    def play_button_function(self):
        self.Main_menu_frame.forget()
        self.Game_frame.pack(fill='both')
        self.play_game_level(1)

        if self.Options_checkbox_for_sound.get():
            start_bg_sound()
    def option_button_function(self):
        self.Main_menu_frame.forget()
        self.Options_frame.pack(fill='both')

    def records_button_function(self):
        self.Main_menu_frame.forget()
        self.Records_frame.pack(fill='both')
        self.Records_search_index = 0
        self.Record_list = get_file_info('Records.json')

        for i in range(10):
            if i < len(self.Record_list):
                self.Record_label_list[i]['text'] = ' '.join([f'{i + 1}.', self.Record_list[i]['record_string']])
            else:
                self.Record_label_list[i]['text'] = ''

    # Методы-команды для виджетов главного меню, для реализации игрового процесса

    # Функция возвращающая сгенерированную матрицу
    def generate_game_matrix(self):
        result = list()
        x_cord = 110
        y_cord = 300
        row = list()

        while y_cord < self.H - 200:
            row.append([(x_cord + 100 // 2, y_cord + 100 // 2), 0, ''])
            x_cord += 100
            if x_cord >= self.W - 200:
                s = row.copy()
                result.append(s)
                x_cord = 110
                y_cord += 100
                row.clear()
        return result

    # Метод для очистик полей матрицы
    def clear_game_matrix(self):
        for i in range(len(self.Game_matrix)):
            for j in range(len(self.Game_matrix[i])):
                self.Game_matrix[i][j][1], self.Game_matrix[i][j][2] = 0, ''

    # Метод для выхода из уровня
    def level_exit(self, item):
        while self.Game_active_bomb_list:
            self.root.after_cancel(self.Game_active_bomb_list.pop())

        self.root.unbind('<KeyPress>')
        self.Game_player.break_animation()
        self.Game_enemy_list.clear()
        self.Game_loosing_heart_list.clear()
        self.clear_game_matrix()
        self.Game_canvas.delete('FEL')

        if item == 'lose':
            self.Game_frame.forget()
            self.End_game_frame.pack(fill='both')
            self.load_end_screen('lose')

            if self.Options_checkbox_for_sound.get():
                stop_bg_sound()

        elif item == 'exit':
            self.Game_frame.forget()
            self.Main_menu_frame.pack(fill='both')

            if self.Options_checkbox_for_sound.get():
                stop_bg_sound()

        elif (item == 'next') and (self.Game_level < 5):
            self.play_game_level(self.Game_level + 1)
        else:
            self.Game_frame.forget()
            self.End_game_frame.pack(fill='both')
            self.load_end_screen('win')

            if self.Options_checkbox_for_sound.get():
                stop_bg_sound()

    # Метод для запуска уровня
    def play_game_level(self, level_number):
        self.Game_canvas.delete('FEL')
        self.Game_level = level_number
        self.generate_level()

        self.Game_labels['max_bomb_label']['text'] = 0
        self.Game_labels['speed_label']['text'] = 0
        self.Game_labels['bomb_range_label']['text'] = 0
        if level_number == 1:
            self.Game_labels['score_label']['text'] = 'Счет: 0'

        threading.Thread(target=self.enemy_animate, daemon=True).start()

        self.Game_player = Player(images['animation']['player'], self.Game_canvas, 0, 0, 'Sounds/Player_hit.mp3')

        self.Game_player.set_characters(hp=3, max_bomb=1, speed=0.035, bomb_range=1)
        self.Game_player.entity_pack(*self.Game_matrix[0][0][0])
        self.root.bind('<KeyPress>', self.player_action)

    # Метод для генерации объектов игрового поля
    def generate_level(self):
        self.Game_canvas.create_image(100, 298, anchor='nw', image=images['field'][self.Game_level], tag=['bg', 'FEL'])
        self.Game_canvas.tag_lower('bg')

        for undestroyable_wall_cords in self.Game_level_hash[str(self.Game_level)]['undestroyable']:
            i, j = undestroyable_wall_cords
            self.Game_matrix[i][j][1] = self.Game_canvas.create_image(
                *self.Game_matrix[i][j][0], anchor='center', image=images['und_des_wal'][self.Game_level], tag=['FEL', 'wall'])
            self.Game_matrix[i][j][2] = 'undestroyable'

        for destroyable_wall_cords in self.Game_level_hash[str(self.Game_level)]['destroyable']:
            i, j = destroyable_wall_cords
            self.Game_matrix[i][j][1] = self.Game_canvas.create_image(
                *self.Game_matrix[i][j][0], anchor='center', image=images['des_wal'][self.Game_level], tag=['FEL', 'wall'])
            self.Game_matrix[i][j][2] = 'destroyable'

        self.Game_exit_cords['i'], self.Game_exit_cords['j'] = random.choice(self.Game_level_hash[str(self.Game_level)]['destroyable'])

        match self.Game_level:
            case 1:
                self.Game_enemy_list.extend(
                    [Enemy(images['animation']['slime'], self.Game_canvas, 0, 5, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['slime'], self.Game_canvas, 0, 11, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['slime'], self.Game_canvas, 5, 11, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['slime'], self.Game_canvas, 3, 16, 'Sounds/Slime_dead.mp3', 0.06, 0.2)])
            case 2:
                self.Game_enemy_list.extend(
                    [Enemy(images['animation']['green_slime'], self.Game_canvas, 1, 4, 'Sounds/Slime_dead.mp3', 0.06, 0.17),
                     Enemy(images['animation']['green_slime'], self.Game_canvas, 1, 10, 'Sounds/Slime_dead.mp3', 0.06, 0.17),
                     Enemy(images['animation']['green_slime'], self.Game_canvas, 1, 16, 'Sounds/Slime_dead.mp3', 0.06, 0.17),
                     Enemy(images['animation']['skeleton'], self.Game_canvas, 4, 7, 'Sounds/Skeleton_dead.mp3', 0.06, 0.07),
                     Enemy(images['animation']['skeleton'], self.Game_canvas, 5, 13, 'Sounds/Skeleton_dead.mp3', 0.06, 0.07)])
            case 3:
                self.Game_enemy_list.extend(
                    [Enemy(images['animation']['zombie'], self.Game_canvas, 3, 1, 'Sounds/Zombie_dead.mp3', 0.05, 0.13),
                     Enemy(images['animation']['zombie'], self.Game_canvas, 0, 9, 'Sounds/Zombie_dead.mp3', 0.05, 0.13),
                     Enemy(images['animation']['zombie'], self.Game_canvas, 5, 6, 'Sounds/Zombie_dead.mp3', 0.05, 0.13),
                     Enemy(images['animation']['zombie'], self.Game_canvas, 3, 16, 'Sounds/Zombie_dead.mp3', 0.05, 0.13),
                     Enemy(images['animation']['green_slime'], self.Game_canvas, 0, 6, 'Sounds/Slime_dead.mp3', 0.06, 0.17),
                     Enemy(images['animation']['green_slime'], self.Game_canvas, 5, 9, 'Sounds/Slime_dead.mp3', 0.06, 0.17),
                     Enemy(images['animation']['green_slime'], self.Game_canvas, 3, 15, 'Sounds/Slime_dead.mp3', 0.06, 0.17)])
            case 4:
                self.Game_enemy_list.extend(
                    [Enemy(images['animation']['slime'], self.Game_canvas, 4, 0, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['slime'], self.Game_canvas, 3, 16, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['slime'], self.Game_canvas, 5, 9, 'Sounds/Slime_dead.mp3', 0.06, 0.2),
                     Enemy(images['animation']['zombie'], self.Game_canvas, 2, 3, 'Sounds/Zombie_dead.mp3',   0.05, 0.13),
                     Enemy(images['animation']['zombie'], self.Game_canvas, 0, 13, 'Sounds/Zombie_dead.mp3',  0.05, 0.13),
                     Enemy(images['animation']['skeleton'], self.Game_canvas, 3, 7, 'Sounds/Skeleton_dead.mp3', 0.06, 0.07),
                     Enemy(images['animation']['skeleton'], self.Game_canvas, 5, 8, 'Sounds/Skeleton_dead.mp3', 0.06, 0.07)])
            case 5:
                self.Game_enemy_list.extend(
                    [Enemy(images['animation']['lava_slime'], self.Game_canvas, 4, 0, 'Sounds/Slime_dead.mp3', 0.06, 0.1),
                     Enemy(images['animation']['lava_slime'], self.Game_canvas, 0, 4, 'Sounds/Slime_dead.mp3', 0.06, 0.1),
                     Enemy(images['animation']['lava_slime'], self.Game_canvas, 4, 16, 'Sounds/Slime_dead.mp3', 0.06, 0.1),
                     Enemy(images['animation']['lava_slime'], self.Game_canvas, 5, 12, 'Sounds/Slime_dead.mp3',  0.06, 0.1),
                     Enemy(images['animation']['wither'], self.Game_canvas, 3, 6, 'Sounds/Skeleton_dead.mp3', 0.06, 0.05),
                     Enemy(images['animation']['wither'], self.Game_canvas, 3, 8, 'Sounds/Skeleton_dead.mp3', 0.06, 0.05),
                     Enemy(images['animation']['wither'], self.Game_canvas, 3, 10, 'Sounds/Skeleton_dead.mp3', 0.06, 0.05)])

    # Метод для проверки возможности передвижения персонажа на клетку
    def move_is_correct(self, i, j):
        if (0 <= i < 6) and (0 <= j < 17) and not (self.Game_matrix[i][j][2] in ('undestroyable', 'destroyable')):
            return True
        else:
            return False

    # Метод, запускающийся в отдельном потоке для реализации автономного перемещения противников по игровому полю
    def enemy_animate(self):
        for enemy in self.Game_enemy_list:
            enemy_i, enemy_j = enemy.get_mpos()
            enemy_x, enemy_y = self.Game_matrix[enemy_i][enemy_j][0]
            enemy.entity_pack(enemy_x, enemy_y)

        while self.Game_enemy_list:
            for enemy in self.Game_enemy_list:
                if self.Game_player.collidirect(*enemy.get_cords(), ranges=40):
                    self.hit_game_player()

                enemy_i, enemy_j = enemy.get_mpos()
                correct_moves = list()
                if self.move_is_correct(enemy_i, enemy_j + 1):
                    correct_moves.append((100, 'x', 'j', 'right'))

                if self.move_is_correct(enemy_i, enemy_j - 1):
                    correct_moves.append((-100, 'x', 'j', 'left'))

                if self.move_is_correct(enemy_i - 1, enemy_j):
                    correct_moves.append((-100, 'y', 'i'))

                if self.move_is_correct(enemy_i + 1, enemy_j):
                    correct_moves.append((100, 'y', 'i'))

                threading.Thread(target=enemy.enemy_moving, args=(random.choice(correct_moves)), daemon=True).start()

    # Обработчик событий управления персонажем
    def player_action(self, event):
        player_i, player_j = self.Game_player.get_mpos()
        if (event.keycode == self.Key_right) and self.move_is_correct(player_i, player_j + 1):
            threading.Thread(target=self.Game_player.player_moving, args=(100, 'x', 'j', 'right'), daemon=True).start()
            self.check_player_position()

        elif (event.keycode == self.Key_left) and self.move_is_correct(player_i, player_j - 1):
            threading.Thread(target=self.Game_player.player_moving, args=(-100, 'x', 'j', 'left'), daemon=True).start()
            self.check_player_position()

        elif (event.keycode == self.Key_up) and self.move_is_correct(player_i - 1, player_j):
            threading.Thread(target=self.Game_player.player_moving, args=(-100, 'y', 'i'), daemon=True).start()
            self.check_player_position()

        elif (event.keycode == self.Key_down) and self.move_is_correct(player_i + 1, player_j):
            threading.Thread(target=self.Game_player.player_moving, args=(100, 'y', 'i'), daemon=True).start()
            self.check_player_position()

        elif (event.keycode == self.Key_bomb) and (len(self.Game_active_bomb_list) < self.Game_player.get_characters('max_bomb')):
            self.Game_matrix[player_i][player_j][1] = self.Game_canvas.create_image(
                *self.Game_matrix[player_i][player_j][0], anchor='center', image=images['bomb'], tag='FEL')
            self.Game_matrix[player_i][player_j][2] = 'bomb'
            bomb_thread = threading.Thread(target=self.explotions_game_bomb, args=(player_i, player_j), daemon=True)
            self.Game_active_bomb_list.append(self.root.after(1200, bomb_thread.start))

    # Метод для определения выхода или усиления в клетке, на которой находиться персонаж
    def check_player_position(self):
        player_i, player_j = self.Game_player.get_mpos()
        match self.Game_matrix[player_i][player_j][2]:
            case 'active_exit':
                self.level_exit('next')
            case 'HP':
                if self.Game_player.get_characters('HP') < 3:
                    self.Game_player.up_characters('HP', 1)
                    self.Game_canvas.delete(self.Game_loosing_heart_list.pop())
                self.play_game_sound('Sounds/Power.mp3')
                self.Game_canvas.delete(self.Game_matrix[player_i][player_j][1])
                self.Game_matrix[player_i][player_j][1], self.Game_matrix[player_i][player_j][2] = 0, ''
            case 'max_bomb':
                self.Game_player.up_characters('max_bomb', 1)
                self.Game_labels['max_bomb_label']['text'] += 1
                self.play_game_sound('Sounds/Power.mp3')
                self.Game_canvas.delete(self.Game_matrix[player_i][player_j][1])
                self.Game_matrix[player_i][player_j][1], self.Game_matrix[player_i][player_j][2] = 0, ''
            case 'speed':
                if self.Game_player.get_characters('speed') > 0.01:
                    self.Game_player.up_characters('speed', -0.002)
                    self.Game_labels['speed_label']['text'] += 1
                self.play_game_sound('Sounds/Power.mp3')
                self.Game_canvas.delete(self.Game_matrix[player_i][player_j][1])
                self.Game_matrix[player_i][player_j][1], self.Game_matrix[player_i][player_j][2] = 0, ''
            case 'bomb_range':
                self.Game_player.up_characters('bomb_range', 1)
                self.Game_labels['bomb_range_label']['text'] += 1
                self.play_game_sound('Sounds/Power.mp3')
                self.Game_canvas.delete(self.Game_matrix[player_i][player_j][1])
                self.Game_matrix[player_i][player_j][1], self.Game_matrix[player_i][player_j][2] = 0, ''

    # Метод для обработки получения урона персонажем
    def hit_game_player(self):
        self.play_game_sound(self.Game_player.dead_sound)
        self.Game_player.break_animation()
        hp, max_bomb, speed, bomb_range = self.Game_player.get_characters('all')
        if hp - 1 > 0:
            self.Game_player = Player(images['animation']['player'], self.Game_canvas, 0, 0, 'Sounds/Player_hit.mp3')
            self.Game_player.set_characters(hp=hp - 1, speed=speed, max_bomb=max_bomb, bomb_range=bomb_range)
            self.pack_enpy_heart()
            self.Game_player.entity_pack(*self.Game_matrix[0][0][0])
        else:
            self.level_exit('lose')

    # Метод для выведения пустых сердец на интерфейс
    def pack_enpy_heart(self):
        if len(self.Game_loosing_heart_list) == 0:
            self.Game_loosing_heart_list.append(self.Game_canvas.create_image(690, 95, image=images['interface']['empy_heart'], tag='FEL'))
        else:
            self.Game_loosing_heart_list.append(self.Game_canvas.create_image(600, 95, image=images['interface']['empy_heart'], tag='FEL'))

    # Метод для удаления бомбы и обработки ее взрыва
    def explotions_game_bomb(self, bomb_i, bomb_j):
        def kill_enemy_function(i, j):
            nonlocal player_has_hit, score_point
            expl_x, expl_y = self.Game_matrix[i][j][0]
            if self.Game_player.collidirect(expl_x, expl_y, ranges=60) and not player_has_hit:
                self.hit_game_player()
                player_has_hit = True

            enemy_index = 0
            while enemy_index < len(self.Game_enemy_list):
                if self.Game_enemy_list[enemy_index].collidirect(expl_x, expl_y, ranges=60):
                    self.play_game_sound(self.Game_enemy_list[enemy_index].dead_sound)
                    self.Game_enemy_list.pop(enemy_index).break_animation()
                    score_point += 300 * self.Game_level
                else:
                    enemy_index += 1

        self.Game_active_bomb_list.pop()
        self.play_game_sound('Sounds/Bomb.mp3')
        self.Game_canvas.delete(self.Game_matrix[bomb_i][bomb_j][1])
        self.Game_matrix[bomb_i][bomb_j][1], self.Game_matrix[bomb_i][bomb_j][2] = 0, ''

        bomb_range = self.Game_player.get_characters('bomb_range')
        player_has_hit = False
        score_point = 0


        for i in range(bomb_i, bomb_i + bomb_range + 1):
            if (i > 5) or (i < 0) or (self.Game_matrix[i][bomb_j][2] == 'undestroyable'):
                break
            elif self.Game_matrix[i][bomb_j][2] == 'destroyable':
                self.Game_canvas.delete(self.Game_matrix[i][bomb_j][1])
                self.Game_matrix[i][bomb_j][1], self.Game_matrix[i][bomb_j][2] = 0, ''
                self.spawn_game_power(i, bomb_j)
                score_point += 100 * self.Game_level
                break
            else:
                kill_enemy_function(i, bomb_j)

        for i in range(bomb_i, bomb_i - bomb_range - 1, -1):
            if (i > 5) or (i < 0) or (self.Game_matrix[i][bomb_j][2] == 'undestroyable'):
                break
            elif self.Game_matrix[i][bomb_j][2] == 'destroyable':
                self.Game_canvas.delete(self.Game_matrix[i][bomb_j][1])
                self.Game_matrix[i][bomb_j][1], self.Game_matrix[i][bomb_j][2] = 0, ''
                self.spawn_game_power(i, bomb_j)
                score_point += 100 * self.Game_level
                break
            else:
                kill_enemy_function(i, bomb_j)

        for j in range(bomb_j, bomb_j + bomb_range + 1):
            if (j > 16) or (j < 0) or (self.Game_matrix[bomb_i][j][2] == 'undestroyable'):
                break
            elif self.Game_matrix[bomb_i][j][2] == 'destroyable':
                self.Game_canvas.delete(self.Game_matrix[bomb_i][j][1])
                self.Game_matrix[bomb_i][j][1], self.Game_matrix[bomb_i][j][2] = 0, ''
                self.spawn_game_power(bomb_i, j)
                score_point += 100 * self.Game_level
                break
            else:
                kill_enemy_function(bomb_i, j)

        for j in range(bomb_j, bomb_j - bomb_range - 1, -1):
            if (j > 16) or (j < 0) or (self.Game_matrix[bomb_i][j][2] == 'undestroyable'):
                break
            elif self.Game_matrix[bomb_i][j][2] == 'destroyable':
                self.Game_canvas.delete(self.Game_matrix[bomb_i][j][1])
                self.Game_matrix[bomb_i][j][1], self.Game_matrix[bomb_i][j][2] = 0, ''
                self.spawn_game_power(bomb_i, j)
                score_point += 100 * self.Game_level
                break
            else:
                kill_enemy_function(bomb_i, j)

        if self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][2] == '':
            self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][1] = self.Game_canvas.create_image(
                    *self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][0],
                    image=images['exit']['not_active'], tag='FEL')
            self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][2] = 'not_active_exit'

        if (self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][2] == 'not_active_exit') and (not self.Game_enemy_list):
            self.Game_canvas.delete(self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][1])
            self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][1] = self.Game_canvas.create_image(
                    *self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][0],
                    image=images['exit']['active'], tag='FEL')
            self.Game_matrix[self.Game_exit_cords['i']][self.Game_exit_cords['j']][2] = 'active_exit'

        self.Game_labels['score_label']['text'] = 'Счет: ' + str(int(self.Game_labels['score_label']['text'][self.Game_labels['score_label']['text'].index(' ') + 1:]) + score_point)

    # Метод для спауна игровых усилений
    def spawn_game_power(self, i, j):
        if (i, j) != (self.Game_exit_cords['i'], self.Game_exit_cords['j']):
            match random.randint(1, 20):
                case 5:
                    self.Game_matrix[i][j][2] = 'HP'
                    self.Game_matrix[i][j][1] = self.Game_canvas.create_image(*self.Game_matrix[i][j][0],
                                                                                image=images['powers']['HP'], tag='FEL')
                case 10:
                    self.Game_matrix[i][j][2] = 'max_bomb'
                    self.Game_matrix[i][j][1] = self.Game_canvas.create_image(*self.Game_matrix[i][j][0],
                                                                               image=images['powers']['max_bomb'], tag='FEL')
                case 15:
                    self.Game_matrix[i][j][2] = 'bomb_range'
                    self.Game_matrix[i][j][1] = self.Game_canvas.create_image(*self.Game_matrix[i][j][0],
                                                                               image=images['powers']['bomb_range'], tag='FEL')
                case 20:
                    self.Game_matrix[i][j][2] = 'speed'
                    self.Game_matrix[i][j][1] = self.Game_canvas.create_image(*self.Game_matrix[i][j][0],
                                                                               image=images['powers']['speed'], tag='FEL')

    # Методы-команды для виджетов окна завершения игры
    # Метод для загрузки окна завершеня игры
    def load_end_screen(self, result):
        score = int(self.Game_labels['score_label']['text'][self.Game_labels['score_label']['text'].index(' ') + 1:])

        self.End_game_head_image = self.End_game_canvas.create_image(self.W // 2 + 50, self.H // 2 - 120, anchor='center',
                                                                     image=images['interface'][result])
        self.End_game_score_text_image = self.End_game_canvas.create_text(self.W // 2, self.H // 2 + 20,
                                                                          text='Ваш счет: ' + str(score),
                                                                          font='impact 45', fill='#87410E')
        self.End_game_name_entry.delete(0, tkinter.END)

    def end_game_exit_button_function(self):
        self.End_game_canvas.delete(self.End_game_head_image)
        self.End_game_canvas.delete(self.End_game_score_text_image)
        self.End_game_frame.forget()
        self.Main_menu_frame.pack(fill='both')

    def save_records_button_function(self):
        name = self.End_game_name_entry.get()
        score = int(self.Game_labels['score_label']['text'][self.Game_labels['score_label']['text'].index(' ') + 1:])

        if name == len(name) * ' ':
            messagebox.showwarning(title='Бомбермен', message='Укажите имя для сохранения рекорда!')
        elif len(name) > 15:
            messagebox.showwarning(title='Бомбермен', message='Имя не должно содержать более 15 символов!')
        else:
            record_list = get_file_info('Records.json')
            for i in range(len(record_list)):
                if score > record_list[i]['score']:
                    record_list.insert(i, {'record_string': f'{name}: {score}', 'score': score})
                    break
            else:
                record_list.append({'record_string': f'{name}: {score}', 'score': score})

            set_file_info('Records.json', record_list)
            self.End_game_frame.forget()
            self.Main_menu_frame.pack(fill='both')

    # Методы-команды для виджета выхода окна настроек
    def option_quit_button_function(self):
        self.Options_frame.forget()
        self.Main_menu_frame.pack(fill='both')

    def set_moving_keys(self, selected_option):
        if selected_option == 'A | D | W | S':
            self.Key_right = 68   # D
            self.Key_left = 65    # A
            self.Key_up = 87      # W
            self.Key_down = 83    # S
        else:
            self.Key_right = 39   # key Right ->
            self.Key_left = 37    # key Left <-
            self.Key_up = 38      # key Up ^
            self.Key_down = 40    # key Down ^

    def set_planting_bomb_keys(self, selected_option):
        match selected_option:
            case 'Q': self.Key_bomb = 81
            case 'E': self.Key_bomb = 69
            case 'Tab': self.Key_bomb = 9
            case 'Space': self.Key_bomb = 32
            case 'CapsLock': self.Key_bomb = 20
            case 'Shift': self.Key_bomb = 16
            case 'Ctrl': self.Key_bomb = 17
            case 'Enter': self.Key_bomb = 13

    def play_game_sound(self, sound):
        if self.Options_checkbox_for_sound:
            playsound.playsound(sound, block=False)

    # Методы-команды для виджетов окна рекордов
    def record_quit_button_function(self):
        self.Records_frame.forget()
        self.Main_menu_frame.pack(fill='both')

    def next_page_button_function(self):
        if self.Records_search_index + 10 < len(self.Record_list):
            self.Records_search_index += 10
            for i in range(10):
                if self.Records_search_index + i < len(self.Record_list):
                    self.Record_label_list[i]['text'] = ' '.join(
                        [f'{self.Records_search_index + i + 1}.', self.Record_list[self.Records_search_index + i]['record_string']])
                else:
                    self.Record_label_list[i]['text'] = ''

    def last_page_button_function(self):
        if self.Records_search_index > 0:
            self.Records_search_index -= 10
            for i in range(10):
                if self.Records_search_index + i < len(self.Record_list):
                    self.Record_label_list[i]['text'] = ' '.join(
                        [f'{self.Records_search_index + i + 1}.', self.Record_list[self.Records_search_index + i]['record_string']])
                else:
                    self.Record_label_list[i]['text'] = ''


Application = MyApplication(root, 'Бомбермен', images['bomb'])

if __name__ == '__main__':
    Application.run()
