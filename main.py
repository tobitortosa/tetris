import pygame, sys
from game import Game
from colors import Colors
from dbfunctions import *

create_table_jugadores()

pygame.display.set_caption("Tetris")
pygame.init()


nombre = ""
active = False


title_font = pygame.font.Font(None, 40)
ranking_font_nombre_puntos = pygame.font.Font(None, 30)
ranking_font = pygame.freetype.SysFont(None, 28, True, False)


menu_text = title_font.render("Ingrese su nombre", True, Colors.white)
ranking_text = title_font.render("Mejores Puntuaciones", True, Colors.white)
ranking_text_puntos = ranking_font_nombre_puntos.render("Puntos", True, Colors.white)
ranking_text_nombre = ranking_font_nombre_puntos.render("Nombre", True, Colors.white)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
time_surface = title_font.render("Time", True, Colors.white)

text_box = pygame.Rect(122, 100, 100, 50)
score_rect = pygame.Rect(320, 55, 170, 60)
time_rect = pygame.Rect(320, 530, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)


screen = pygame.display.set_mode((500, 620))

clock = pygame.time.Clock()
game = Game()


GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)


game_time = 180


menu_state = True
game_state = False
ranking_state = False

# menu button

start_button_surface = title_font.render("Start", True, Colors.white)
start_button = pygame.Rect(150, 200, 200, 60)

ranking_button_surface = title_font.render("Ranking", True, Colors.white)
ranking_button = pygame.Rect(150, 300, 200, 60)

menu_button_surface = title_font.render("Menu", True, Colors.white)
menu_button = pygame.Rect(150, 500, 200, 60)


menu_state_flag = False


start_ticks = pygame.time.get_ticks()  # starter tick

jugadores = get_jugadores()

while True:
    while menu_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += event.unicode.upper()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if start_button.collidepoint(event.pos):
                    player_exist = False
                    if len(nombre) > 0:
                        if len(jugadores) == 0:
                            create_jugador(nombre)
                            jugadores = get_jugadores()

                        else:
                            exist = []
                            for element in jugadores:
                                if element[1] == nombre:
                                    exist.append(element)
                            if len(exist) == 0:
                                create_jugador(nombre)
                                jugadores = get_jugadores()

                        menu_state = False
                        game_state = True
                    print(jugadores)

                if ranking_button.collidepoint(event.pos):
                    game_state = False
                    menu_state = False
                    ranking_state = True

        screen.fill(Colors.dark_blue)

        if active:
            input_color = Colors.verde
        else:
            input_color = Colors.white

        pygame.draw.rect(screen, input_color, text_box, 4, 12)
        text_surface = title_font.render(nombre, True, Colors.naranja)
        screen.blit(text_surface, (text_box.x + 10, text_box.y + 12))
        text_box.w = max(250, text_surface.get_width() + 10)

        a, b = pygame.mouse.get_pos()
        if (
            start_button.x <= a <= start_button.x + 200
            and start_button.y <= b <= start_button.y + 60
        ):
            pygame.draw.rect(screen, Colors.verde, start_button, 30, 12)
        else:
            pygame.draw.rect(screen, Colors.cyan, start_button, 30, 12)

        if (
            ranking_button.x <= a <= ranking_button.x + 200
            and ranking_button.y <= b <= ranking_button.y + 60
        ):
            pygame.draw.rect(screen, Colors.verde, ranking_button, 30, 12)
        else:
            pygame.draw.rect(screen, Colors.cyan, ranking_button, 30, 12)

        screen.blit(start_button_surface, (start_button.x + 70, start_button.y + 15))
        screen.blit(
            ranking_button_surface, (ranking_button.x + 45, ranking_button.y + 15)
        )
        screen.blit(menu_text, (125, 30))

        pygame.display.flip()
        clock.tick(60)  # FPS

    def recursive_draw(surf, x, y, width, height):
        """Recursive rectangle function."""
        pygame.draw.rect(surf, (0, 0, 0), [x, y, width, height], 1)
        if y >= 620:  # Screen bottom reached.
            return
        # Is the rectangle wide enough to draw again?
        elif x < 500 - width:  # Right screen edge not reached.
            x += width
            # Recursively draw again.
            recursive_draw(surf, x, y, width, height)
        else:
            # Increment y and reset x to 0 and start drawing the next row.
            x = 0
            y += height
            recursive_draw(surf, x, y, width, height)

    recursive_draw(screen, 0, 0, 200, 50)

    while ranking_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    ranking_state = False
                    game_state = False
                    menu_state = True

        screen.fill(Colors.dark_blue)

        x = 55
        y = 110

        screen.blit(ranking_text, (100, 20))
        screen.blit(ranking_text_puntos, (41, 70))
        screen.blit(ranking_text_nombre, (312, 70))

        for row in jugadores:
            for cell in row:
                ranking_font.render_to(
                    screen, (x, y), str(cell), pygame.Color("dodgerblue")
                )
                x += 230  # should be a constant
            y += 40  # should be a constant
            x = 55  # should be a constant, too :-)

        a, b = pygame.mouse.get_pos()
        if (
            menu_button.x <= a <= menu_button.x + 200
            and menu_button.y <= b <= menu_button.y + 60
        ):
            pygame.draw.rect(screen, Colors.verde, menu_button, 30, 12)
        else:
            pygame.draw.rect(screen, Colors.cyan, menu_button, 30, 12)

        screen.blit(menu_button_surface, (menu_button.x + 65, menu_button.y + 15))

        pygame.display.flip()
        clock.tick(60)  # FPS

    while game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over = False
                    game_time = 180
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()

            if event.type == TIMER and game.game_over == False:
                if game_time > 0:
                    game_time -= 1
                    print(game_time)

            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        if game.game_over == True:
            game_time = 0
            for jugador in jugadores:
                if jugador[1] == nombre:
                    if jugador[0] < game.score:
                        update_puntaje_by_name(game.score, nombre)

        time_value = title_font.render(str(game_time), True, Colors.white)

        if game_time == 0:
            game.game_over = True

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))
        screen.blit(time_surface, (375, 500, 50, 50))

        if game.game_over == True:
            screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 12)
        screen.blit(
            score_value_surface,
            score_value_surface.get_rect(
                centerx=score_rect.centerx, centery=score_rect.centery
            ),
        )

        pygame.draw.rect(screen, Colors.light_blue, time_rect, 0, 12)
        screen.blit(
            time_value,
            time_value.get_rect(centerx=time_rect.centerx, centery=time_rect.centery),
        )

        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 12)
        game.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # FPS
