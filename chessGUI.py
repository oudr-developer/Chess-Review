########################################
# COPY RIGHTS : Oussama Draoui        #
#######################################
#   CHESS GUI : creating the visual bored and chess items

import pygame as pg
import tkinter as tk
from tkinter import filedialog as fd
# import tkFileDialog
from chessAI import *
pg.init()
root = tk.Tk().withdraw()

#################################
# CLASS TO BUILD THE DIGITAL GAME
#################################
class GUI:
  def __init__(self):
    self.window = pg.display
    self.sc=self.window.set_mode((610, 610))
    self.clock = pg.time.Clock()
    self.bg = pg.image.load('C:\\Users\\hp\Desktop\\old-project\\Tkinter\\Chess Review\\imgs\\bored.jpg')
    self.txt = None
    self.bored = None
    self.lexer = None
    self.moves = None
    self.openFile()
    self.reset()
  def openFile(self):
    filename = fd.askopenfilename(filetypes=(
        ('arthimitec chess', '*.chess'), ('all files', '*.*')))
    filename = filename if filename != '' else 'test.chess'
    self.txt = open(filename, 'r').read()
  def reset(self):
    
    self.bored = Bored()
    self.lexer = Lexer(self.txt, self.bored)
    self.moves = self.lexer.makeMoves()
    self.run()
  def built(self):
    items = self.bored.items
    for item in items:
      img = pg.image.load(
          f'C:\\Users\\hp\Desktop\\old-project\\Tkinter\\Chess Review\\imgs\\{item.img}').convert()
      color = (248,249,250) if item.team == 'black' else (3,14,94)
      img.set_colorkey(color)
      # img.set_rect((255,0,0))
      img = pg.transform.scale(img,(55,55))
      x= item.getRank()*66+74
      y = item.file*66+74
      if item.check:
        pg.draw.circle(self.sc, (255, 0, 0, 0.5),
                        (x-img.get_width()//2, y-img.get_height()//2), 30)
        item.incrementCeck()
      self.sc.blit(img,(x-img.get_width()//2,y-img.get_height()//2))
    return 
  def run(self):
    move = Move(self.moves,self.bored,self.built)
    run = True
    while run:
      self.sc.blit(self.bg, (0, 0))
      self.built()
      for event in pg.event.get():
        if event.type==pg.QUIT:
          exit()
      keys = pg.key.get_pressed()
      if keys[pg.K_SPACE]:
        print('moved ...')
        move.moving()
        pg.time.wait(500)
      elif keys[pg.K_o]:
        self.openFile()
        self.reset()
      elif keys[pg.K_r]:
        self.reset()
      move.text(self.sc)
      self.window.flip()
      self.clock.tick(60)
      self.window.update()
#############################
# CLASS TO MOVE PIECES
#############################
class Move:
  def __init__(self,moves,bored,built):
    self.moves = moves
    self.move = None
    self.built = built
    self.idx = -1
    self.bored = bored
    self.txt = None
    self.advance()

  def advance(self):
    self.idx += 1
    self.move = self.moves[self.idx] if self.idx < len(self.moves) else None

  def moving(self):
    if self.move != None:
      piece = self.move
      if type(piece) == type([]):
        for item in piece:
          self.item = self.bored.getItem(*item.item())
          self.item.moveTo(*item.getMove())
          self.bored.setItem(self.item, *item.item())
          self.built()
      elif isinstance(piece, Winner):
        print(f'{piece.winner} player win in {piece.total_moves} moves')
        self.txt = f'{piece.winner} player win in {piece.total_moves} moves'

      else:
        print('move ....', piece)
        self.item = self.bored.getItem(*piece.item())
        # print(piece.item())
        if piece.isTaked():
          piece.Taking(self.bored)
          self.item.moveTo(*piece.getMove())
          self.bored.setItem(self.item, *piece.item())
          self.built()
        
        elif piece.isChecked():
          king = self.bored.getKing(piece.team)
          if king.check and king.checkCount > 1:
            king.check = False
            king.resetCheck()
          else:
            king.check = True
          self.built()

        else:
          self.item.moveTo(*piece.getMove())
          self.bored.setItem(self.item, *piece.item())
          self.built()
          if piece.isChanging():
            self.item.setNewname(piece.new_item)
            self.bored.setItem(self.item, *piece.item())
            self.built()
      # self.text()
      self.built()
      self.advance()

  def text(self,sc):
    if self.txt:
      font = pg.font.Font('Poppins-BlackItalic.ttf', 32)
      txt = font.render(self.txt, False, (255, 255, 255), (0, 0, 0, 0.5))
      txtBox = txt.get_rect()
      txtBox.center = (305, 305)
      self.built()
      sc.blit(txt, txtBox)

GUI().run()

