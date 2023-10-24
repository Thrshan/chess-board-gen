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
    def __init__(self, piece_image, name, position) -> None:
        super(Piece, self).__init__()
        self.last_pos = position
        self.surface = pygame.image.load(piece_image)
        self.rect = self.surface.get_rect()
        self.rect.left = position[1]
        self.rect.top = position[0]
        self.name = name

    def update(self, screen):
        screen.blit(self.surface, self.rect)

    def save_mous_down_pos(self, pos):
        print("Dowm")
        print((pos[0],self.last_pos[0]))
        self.mouse_down_offset_x = pos[0] - self.last_pos[0]
        self.mouse_down_offset_y = pos[1] - self.last_pos[1]


    def move(self):
        y, x = pygame.mouse.get_pos()
        print((x, self.mouse_down_offset_x))
        self.rect.left = y + self.mouse_down_offset_y
        self.rect.top = x + self.mouse_down_offset_x

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())


def prep_squares():
    play_area_left = 5
    play_area_top = 5
    grid_length = 45
    grig_nos = 8
    squares = {}

    for i in range(8):
        for j in range(8):
            pos = "{}{}".format(chr(65+j), 8-i)
            squares[pos] = ((i*45) + play_area_top, (j*45) + play_area_left)
    
    return squares
        
class Square(pygame.sprite.Sprite):
    def __init__(self, name, position) -> None:
        super(Square, self).__init__()
        self.square_surf = pygame.Surface((44, 44), pygame.SRCALPHA, 32).convert_alpha()
        # self.square_surf.fill((100, 255, 100))
        self.name = name
        self.rect = self.square_surf.get_rect(top=position[0], left=position[1])

    def update(self, surface):
        surface.blit(self.square_surf, self.rect)  



class Game:
    def __init__(self):
        pygame.init()

        self.square_dict = prep_squares()
        self.load_pieces()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = Board()

        self.squares = pygame.sprite.Group()

        for k,v in self.square_dict.items():
            self.squares.add(Square(k, v))

    def load_pieces(self):
        self.pieces = pygame.sprite.Group()
        self.pieces_dict = {}

        p = Piece("./assets/pieces/classic/45px/Chess_bdt45.svg.png", 'BD1', self.square_dict['C8'])
        self.pieces_dict['BD1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_bdt45.svg.png", 'BD2', self.square_dict['F8'])
        self.pieces_dict['BD2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_blt45.svg.png", 'BL1', self.square_dict['C1'])
        self.pieces_dict['BL1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_blt45.svg.png", 'BL2', self.square_dict['F1'])
        self.pieces_dict['BL2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_kdt45.svg.png", 'KD0', self.square_dict['E8'])
        self.pieces_dict['KD1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_klt45.svg.png", 'KL0', self.square_dict['E1'])
        self.pieces_dict['KL'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_ndt45.svg.png", 'ND1', self.square_dict['B8'])
        self.pieces_dict['ND1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_ndt45.svg.png", 'ND2', self.square_dict['G8'])
        self.pieces_dict['ND2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_nlt45.svg.png", 'NL1', self.square_dict['B1'])
        self.pieces_dict['NL1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_nlt45.svg.png", 'NL2', self.square_dict['G1'])
        self.pieces_dict['NL2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_qdt45.svg.png", 'QD0', self.square_dict['D8'])
        self.pieces_dict['QD'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_qlt45.svg.png", 'QL0', self.square_dict['D1'])
        self.pieces_dict['QL'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rdt45.svg.png", 'RD1', self.square_dict['A8'])
        self.pieces_dict['RD1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rdt45.svg.png", 'RD2', self.square_dict['H8'])
        self.pieces_dict['RD2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rlt45.svg.png", 'RL1', self.square_dict['A1'])
        self.pieces_dict['RL1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_rlt45.svg.png", 'RL2', self.square_dict['H1'])
        self.pieces_dict['RL2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD1', self.square_dict['A7'])
        self.pieces_dict['PD1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD2', self.square_dict['B7'])
        self.pieces_dict['PD2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD3', self.square_dict['C7'])
        self.pieces_dict['PD3'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD4', self.square_dict['D7'])
        self.pieces_dict['PD4'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD5', self.square_dict['E7'])
        self.pieces_dict['PD5'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD6', self.square_dict['F7'])
        self.pieces_dict['PD6'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD7', self.square_dict['G7'])
        self.pieces_dict['PD7'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_pdt45.svg.png", 'PD8', self.square_dict['H7'])
        self.pieces_dict['PD8'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL1', self.square_dict['A2'])
        self.pieces_dict['PL1'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL2', self.square_dict['B2'])
        self.pieces_dict['PL2'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL3', self.square_dict['C2'])
        self.pieces_dict['PL3'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL4', self.square_dict['D2'])
        self.pieces_dict['PL4'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL5', self.square_dict['E2'])
        self.pieces_dict['PL5'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL6', self.square_dict['F2'])
        self.pieces_dict['PL6'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL7', self.square_dict['G2'])
        self.pieces_dict['PL7'] = p
        self.pieces.add(p)
        p = Piece("./assets/pieces/classic/45px/Chess_plt45.svg.png", 'PL8', self.square_dict['H2'])
        self.pieces_dict['PL8'] = p
        self.pieces.add(p)

    def run(self):
        running = True
        dragging = False
        drag_piece = None
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked_piece = [s for s in self.pieces if s.rect.collidepoint(pos)]
                    # clicked_square = [s for s in self.squares if s.rect.collidepoint(pos)]
                    # [print(e.name) for e in clicked_piece]
                    # [print(e.name) for e in clicked_square]
                    if clicked_piece:
                        drag_piece = clicked_piece[0]
                        drag_piece.save_mous_down_pos(pos)
                        dragging = True

                elif event.type == MOUSEMOTION:
                    if dragging:
                        drag_piece.move()
                
                elif event.type == MOUSEBUTTONUP:
                    drag_piece = None
                    dragging = False


            self.board.draw(self.screen)
            self.squares.update(self.screen)
            self.pieces.update(self.screen)

            pygame.display.flip()

        

if __name__ == "__main__":
    game = Game()
    game.run()