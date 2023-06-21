class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    cyan = (21, 204, 209)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    def __init__(self) -> None:
        pass

    @classmethod
    def get_ceil_colors(cls):
        return [
            cls.dark_grey,
            cls.green,
            cls.orange,
            cls.yellow,
            cls.cyan,
            cls.white,
            cls.dark_blue,
            cls.light_blue,
        ]
