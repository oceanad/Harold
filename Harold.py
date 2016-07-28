import turtle
import math
import Tkinter

def main():       
    turtle.setup(500,500)
    turtle.title('Hex')
    Herman = turtle.Turtle()
    Herman_text = turtle.Turtle()
    position = [100, 100]
    Herman_text.goto(Herman.position()[0], Herman.position()[1])
    Herman_text.write("Player 1 is a purple turtle. Player 2 is a green turtle.", align="center")
    Herman_text.ht()
    screen = turtle.Screen()
    polygon = turtle.Turtle()
    polygon.hideturtle()
    Harold = turtle.Turtle()    
    Harold.hideturtle()
    polygon.speed(0)   
    size = (2)
    start = [-100, 100]
    board = Board(polygon, Harold, size, start)
    board.draw_board()
    
    screen.onclick(board.play)
    Harold.penup()
    
class Hexagon():
    num_sides = 6
    side_length = 20
    angle = 360.0 / num_sides
    radius = 10 * math.sqrt(3)
        
    def __init__(self, polygon, position):
        self.polygon = polygon
        self.x = position[0]
        self.y = position[1]
        self.centre = [self.x, self.y - self.radius]
        self.pt = [(self.x - 1.6), (self.y - self.radius - 1.6)]
        self.clicked = False
        self.draw_hex()
        
    def draw_hex(self):
        self.polygon.penup()
        self.polygon.setpos(self.x, self.y)
        self.polygon.setheading(0)
        self.polygon.right(self.angle / 2)
        self.polygon.pendown()
        for i in range(self.num_sides):
            self.polygon.forward(self.side_length)
            self.polygon.right(self.angle)
    
    def is_played(self, mouse_pos):
        sq1 = (self.centre[0] - mouse_pos[0])**2
        sq2 = (self.centre[1] - mouse_pos[1])**2
        distance = math.sqrt(sq1 + sq2)   
        if distance < Hexagon.radius:
            return True
        else:
            return False
            
    def fill(self, num_moves):
        self.Harold.stamp()
        self.clicked = True

class Board():
    diameter = (10 * math.sqrt(3)) * 2
    
    def __init__(self, polygon, Harold, board_size, start_pos):
        self.polygon = polygon
        self.Harold = Harold
        self.board_size = board_size
        self.start_pos = start_pos
        self.num_moves = 0
        self.list = []
        
    def draw_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(Hexagon(self.polygon, self.start_pos))  
                self.start_pos[0] += Board.diameter
            self.start_pos[0] = self.start_pos[0] - ((self.board_size) * Board.diameter) + (Board.diameter/2)
            self.start_pos[1] -= Hexagon.side_length * 1.5
            self.list.append(row)
            
    def play(self, x, y):
        for row in self.list:
            for hexagon in row:
                if hexagon.is_played((x, y)) and not hexagon.clicked:
                    if self.num_moves %2 == 0:
                        self.Harold.color("Purple") 
                    else:
                        self.Harold.color("Green")
                    self.Harold.shape("turtle")
                    self.Harold.goto(hexagon.pt) 
                    self.Harold.stamp()
                    self.num_moves += 1
                    hexagon.clicked = True
    
#game = True
#Define something as game
#while game:
    #Grid code? Outside?
    #User (mouse) input code
    #Win condition code
    #A win is when there is a string of hexagons of the same color that travels from one side of its designated board to the other
    #if win:
        #game = false
#def start(self):
#def main():
#def isInside():0, 0

#def check_win(Hexboard):
    #win_cond = #Edges connected?
#Define the mainloop?
#def main()

#def check_win(self):

#hex = Hexagon()

main()
turtle.done()