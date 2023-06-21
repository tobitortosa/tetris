class Colors:
    gris_oscuro = (26, 31, 40)
    verde = (47, 230, 23)
    naranja = (226, 116, 17)
    amarillo = (237, 234, 4)
    cyan = (21, 204, 209)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    def __init__(self) -> None:
        pass

    @classmethod
    def get_ceil_colors(cls):
        return [
            cls.gris_oscuro,
            cls.verde,
            cls.naranja,
            cls.amarillo,
            cls.cyan,
        ]
