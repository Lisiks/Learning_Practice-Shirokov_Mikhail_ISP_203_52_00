from time import sleep


class Entity:
    """ Класс для различных существ - игрока и врагов"""
    def __del__(self):
        self._canvas.delete(self._image_item)

    def __init__(self, animation_dict, canvas, matrix_pos_i, matrix_pos_j, dead_sound):
        self._matrix_pos = {'i': matrix_pos_i, 'j': matrix_pos_j}
        self._cords = {'x': -1, 'y': -1}
        self._canvas = canvas

        self._animation = animation_dict
        self._image_item = 0

        self._orientation = 'right'
        self._on_moving = False
        self._hit = False
        self.dead_sound = dead_sound

    def entity_pack(self, x, y):
        self._cords['x'], self._cords['y'] = x, y
        self._image_item = self._canvas.create_image(x, y, anchor='center', image=self._animation['right'][-1])
        self._orientation = 'right'
        self._on_moving = False

    def get_cords(self):
        return self._cords['x'], self._cords['y']

    def get_mpos(self):
        return self._matrix_pos['i'], self._matrix_pos['j']

    def collidirect(self, dg_x, dg_y, ranges):
        if (dg_x - ranges < self._cords['x'] < dg_x + ranges) and (dg_y - ranges < self._cords['y'] < dg_y + ranges):
            return True
        else:
            return False

    def break_animation(self):
        self._hit = True


class Enemy(Entity):
    def __init__(self, animation_dict, canvas, matrix_pos_i, matrix_pos_j, dead_sound, speed, caldown):
        super().__init__(animation_dict, canvas, matrix_pos_i, matrix_pos_j, dead_sound)
        self._speed = speed
        self._caldown = caldown

    def enemy_moving(self, distance, cord, m_pos, orientation=''):
        if not self._on_moving:
            self._on_moving = True
            self._matrix_pos[m_pos] += 1 if distance > 0 else -1

            if not orientation:
                orientation = self._orientation

            dist = distance / len(self._animation[orientation])
            for i in range(len(self._animation[orientation])):
                if not self._hit:
                    self._cords[cord] += dist
                    deleting_image = self._image_item
                    self._image_item = self._canvas.create_image(self._cords['x'], self._cords['y'], anchor='center',
                                                                 image=self._animation[orientation][i])
                    self._canvas.delete(deleting_image)
                    sleep(self._speed)
                else:
                    break
            else:
                sleep(self._caldown)
                self._on_moving = False
                self._orientation = orientation


class Player(Entity):
    """ Класс игрока """

    def __init__(self, animation_dict, canvas, matrix_pos_i, matrix_pos_j, dead_sound):
        super().__init__(animation_dict, canvas, matrix_pos_i, matrix_pos_j, dead_sound)
        self.characters = {'HP': -1, 'max_bomb': -1, 'speed': -1.0, 'bomb_range': -1}
        self.moving_index = 0

    def set_characters(self, hp=None, max_bomb=None, speed=None, bomb_range=None):
        if hp is not None:
            self.characters['HP'] = hp
        if max_bomb is not None:
            self.characters['max_bomb'] = max_bomb
        if speed is not None:
            self.characters['speed'] = speed
        if bomb_range is not None:
            self.characters['bomb_range'] = bomb_range

    def up_characters(self, charc, value):
        self.characters[charc] += value

    def get_characters(self, item):
        if item == 'all':
            return self.characters['HP'], self.characters['max_bomb'], self.characters['speed'], self.characters['bomb_range']
        else:
            return self.characters[item]

    def player_moving(self, distance, cord, m_pos, orientation=''):
        if not self._on_moving:
            self._on_moving = True
            self._matrix_pos[m_pos] += 1 if distance > 0 else -1

            if not orientation:
                orientation = self._orientation

            dist = distance / len(self._animation[orientation])
            for i in range(len(self._animation[orientation])):
                if not self._hit:
                    self._cords[cord] += dist
                    deleting_image = self._image_item
                    self._image_item = self._canvas.create_image(self._cords['x'], self._cords['y'], anchor='center',
                                                                 image=self._animation[orientation][i])
                    self._canvas.delete(deleting_image)
                    sleep(self.characters['speed'])
                else:
                    break
            else:
                self._on_moving = False
                self._orientation = orientation

