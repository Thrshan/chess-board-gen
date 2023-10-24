import pygame

from PIL import Image


from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEMOTION,
    MOUSEBUTTONUP
)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

class Board:
    def __init__(self) -> None:
        board_image = Image.open("./assets/board/board.png")
        resized_board_image = board_image.resize((368, 368))
        board_image_data = resized_board_image.tobytes()
        board_image_dimensions = resized_board_image.size
        mode = resized_board_image.mode
        self.board_surface = pygame.image.fromstring(board_image_data, board_image_dimensions, mode)
        
    def draw(self, screen):
        screen.blit(self.board_surface, (0,0))

class Piece(pygame.sprite.Sprite):
    def __init__(self, piece_image) -> None:
        super(Piece, self).__init__()
        self.surface = pygame.image.load(piece_image)
        self.rect = self.surface.get_rect(left=0, top=0)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
    
    def move(self):
        pass

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, surface) -> None:
        super(Square, self).__init__()
        self.surface = surface
        self.square_surf = pygame.Surface((44, 44), pygame.SRCALPHA, 32).convert_alpha()
        # self.square_surf.fill((100, 255, 100))
        self.rect = self.square_surf.get_rect(top=x, left=y)

    def update(self):
        self.surface.blit(self.square_surf, self.rect)   

class Game:
    def __init__(self):
        pygame.init()
        self.squares = pygame.sprite.Group()
        self.pieces = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = Board()

        self.pieces_list = []

        p = Piece("./assets/pieces/classic/45px/Chess_bdt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_blt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_kdt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_klt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_ndt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_nlt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_qdt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_qlt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rdt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rlt45.svg.png")
        self.pieces_list.append(p);
        self.pieces.add(p)

        self.play_area = pygame.Surface((360, 360), pygame.SRCALPHA, 32).convert_alpha()
        self.play_area_rect = self.play_area.get_rect(top=5, left=5)

        self.squares_list = []
        for i in range(8):
            for j in range(8):
                sqr = Square(i*45, j*45, self.play_area)
                self.squares_list.append(sqr)
                self.squares.add(sqr)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    # clicked_sprites = [s for s in self.pieces if s.rect.collidepoint(pos)]
                    for piece in self.pieces:
                        print(piece.rect)
                    # print(clicked_sprites)


            self.board.draw(self.screen)
            self.squares.update()
            self.screen.blit(self.play_area, self.play_area_rect)
            self.squares_list[3].square_surf.blit(self.pieces_list[0].surface, (0,0))
            self.squares_list[4].square_surf.blit(self.pieces_list[1].surface, (0,0))


            pygame.display.flip()

        

if __name__ == "__main__":
    game = Game()
    game.run()