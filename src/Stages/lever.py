class Lever:
    def __init__(self):
        self._on_position = False

    def change_position(self):
        """Change the state of the on_position attribute of the Lever instance."""
        self._on_position = not (self._on_position)