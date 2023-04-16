from Abstract.drawable import Drawable

class Door(Drawable):
    def __init__(self, is_open="False"):
        self._is_open = is_open

    def open(self):
        """Change the state of is_open to True"""
        self._is_open = True

    def close(self):
        """Change the state of is_open to False"""
        self._is_open = False
