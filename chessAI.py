# the Part who transform algebra game to visual moves
# import pygame as pg
P = 'Pown'
K = 'King'
R = 'Rock'
N = 'Knight'
Q = 'Qween'
B = 'Bishop'
BKI = 'blackKing.png'
BPI = 'blackPown.png'
BRI = 'blackRock.png'
BNI = 'blackKnight.png'
BQI = 'blackQween.png'
BBI = 'blackBishop.png'
WKI = 'whiteKing.png'
WPI = 'whitePown.png'
WRI = 'whiteRock.png'
WNI = 'whiteKnight.png'
WQI = 'whiteQween.png'
WBI = 'whiteBishop.png'

##################################
#  THE ACTUAL CHESS PIECES
####################################
class Item:
  def __init__(self,name,rank,file,team):
    self.name=name
    self.file = file
    self.rank=rank
    self.team = team
    self.img = self.getImage()
    self.check = False
    self.checkCount = 1
  def setNewname(self,name):
    self.name= name
    self.img = self.getImage()
  def incrementCeck(self):
    self.checkCount +=1
  def resetCheck(self):
    self.checkCount=1
  def getImage(self):
    if self.team == 'black':
      if   self.name == K:return BKI
      elif self.name == N:return BNI
      elif self.name == Q:return BQI
      elif self.name == P:return BPI
      elif self.name == R:return BRI
      elif self.name == B:return BBI
    elif self.team == 'white':
      if   self.name == K:return WKI
      elif self.name == N:return WNI
      elif self.name == Q:return WQI
      elif self.name == P:return WPI
      elif self.name == R:return WRI
      elif self.name == B:return WBI
    
  def moveTo(self,rank,file):
    self.rank = rank
    self.file = file
    return self
  def ckeck():
    if self.name == K: self.check = True
  def updatePown(self,name):
    if self.name == P:
      self.name == name
      self.image == self.gatImage()
  def getRank(self):
    ranks = 'abcdefgh'
    return ranks.index(self.rank)
  def __repr__(self):
    files = [7,6,5,4,3,2,1,0]
    return f'Piece : {self.name[0]}{self.rank}{files.index(self.file)+1}'
###################################
#  THE ACTUAL BORED
####################################
class Bored:
  def __init__(self):
    self.items = [
      Item(P, 'a', 6, 'white'),
      Item(P, 'b', 6, 'white'),
      Item(P, 'c', 6, 'white'),
      Item(P, 'd', 6, 'white'),
      Item(P, 'e', 6, 'white'),
      Item(P, 'f', 6, 'white'),
      Item(P, 'g', 6, 'white'),
      Item(P, 'h', 6, 'white'),
      Item(R, 'a', 7, 'white'),
      Item(R, 'h', 7, 'white'),
      Item(N, 'b', 7, 'white'),
      Item(N, 'g', 7, 'white'),
      Item(B, 'c', 7, 'white'),
      Item(B, 'f', 7, 'white'),
      Item(Q, 'd', 7, 'white'),
      Item(K, 'e', 7, 'white'),
      
      Item(P, 'a', 1, 'black'),
      Item(P, 'b', 1, 'black'),
      Item(P, 'c', 1, 'black'),
      Item(P, 'd', 1, 'black'),
      Item(P, 'e', 1, 'black'),
      Item(P, 'f', 1, 'black'),
      Item(P, 'g', 1, 'black'),
      Item(P, 'h', 1, 'black'),
      Item(R, 'a', 0, 'black'),
      Item(R, 'h', 0, 'black'),
      Item(N, 'b', 0, 'black'),
      Item(N, 'g', 0, 'black'),
      Item(B, 'c', 0, 'black'),
      Item(B, 'f', 0, 'black'),
      Item(Q, 'd', 0, 'black'),
      Item(K, 'e', 0, 'black'),
    ]
  def getItem(self,name,rank,file):
    for item in self.items:
      if item.name == name and item.rank == rank and item.file == file:
        return item
  def setItem(self,new_item,name,rank,file):
     for i in range(len(self.items)):
      item = self.items[i]
      if item.name == name and item.rank == rank and item.file == file:
        self.items[i]=new_item
  def deleteItem(self,rank,file):
      for item in self.items:
        if item.rank == rank and item.file == file:
          self.items.pop(self.items.index(item))
  def getKing(self,team):
    for item in self.items:
      if item.name  == K and item.team == team: return item
  def makeCheck(self,player):
    team = 'white' if player == 'black' else 'black'
    for item in self.items:
      if item.name == K and item.team == team: item.check()  
###################################
#  TOKEN CLASS TO DEFINE PIECES
##################################
class Token:
  def __init__(self,name,rank,file,team,check=False):
    self.name = name
    self.rank = rank
    self.file  = file
    self.team = team
    self.remove = False
    self.taked = None
    self.new_rank = rank
    self.new_file = file
    self.check = check
    self.change = False
    self.new_item = None
  def item(self):
    return [self.name,self.rank,self.file]
  def setNewMove(self,new_rank,new_file):
    self.new_rank = new_rank
    self.new_file = new_file
  def getMove(self):
    return (self.new_rank,self.new_file)
  def take(self,taked_rank,taked_file,taked_team):
    self.taked = True
    self.taked_rank = taked_rank
    self.taked_file = taked_file
    self.taked_team = 'white' if taked_team == 'black' else 'black'
    return 
  def isTaked(self):
    if self.taked is None : return False
    return True
  def isChanging(self):
    return self.change
  def Taking(self,bored):
    bored.deleteItem(self.taked_rank,self.taked_file)
    # self.setNewMove(self.taked_rank,self.taked_file)
  def __repr__(self):
    files = [7,6,5,4,3,2,1,0]
    if self.rank and self.file:return f'{self.name} {self.rank}{files.index(self.file)+1}'
    return f'{self.name} {self.team}'
  def isChecked(self):
    return self.check
class Winner:
  def __init__(self,winner,total_moves):
    self.winner = winner
    self.total_moves = total_moves
  def __repr__(self):
    return 'Check Mate'
################################## 
#  LEXER TO PARSE THE MOVES
#################################
class Lexer :
  def __init__(self,text,bored):
    self.text = text
    self.idx = -1
    self.char = None
    self.player = None
    self.player = self.changeplayer()
    self.bored=bored
    self.totalMoves = len(self.text.split('\n'))
    self.advance()
  def advance(self):
    self.idx +=1
    self.char = self.text[self.idx] if self.idx < len(self.text) else None
    print(self.char,self.idx)
    return 
  def makeMoves(self):
    moves = []
    while self.char != None:
      if self.char in ' \n':
        self.player =self.changeplayer()
        self.advance()
      elif self.char == 'P':moves.append(self.maketokens(P))
      elif self.char == 'N':moves.append(self.maketokens(N))
      elif self.char == 'R':moves.append(self.maketokens(R))
      elif self.char == 'B':moves.append(self.maketokens(B))
      elif self.char == 'Q':moves.append(self.maketokens(Q))
      elif self.char == 'K':moves.append(self.maketokens(K))
      
      elif self.char == '+': 
        self.player=self.changeplayer()
        king = Token(K,None,None,self.player,True)
        moves.append(king)
        self.advance()
      elif self.char == '=':
        token = moves[-1]
        self.advance()
        token.change = True
        token.new_item = self.getname(self.char)
        self.advance()
      elif self.char == '#':
        moves.append(Winner(self.player,self.totalMoves))
        self.advance()
        print('check mate')
        self.advance()
      elif self.char == 'o':moves.append(self.cassel())
      else: break
    print(moves)
    return moves
  def changeplayer(self):
    return 'black' if self.player == 'white' else 'white'
  def maketokens(self,name):
    files = [7,6,5,4,3,2,1,0]
    ranks = 'abcdefgh'
    self.advance()
    rank = self.char
    self.advance()
    file = files[int( self.char)-1]
    self.advance()
    item = Token(name,rank,file,self.player)
    print('moving item :',item)
    if self.char == '-':
      self.advance()
      new_rank = self.char
      self.advance()
      new_file = files[int(self.char)-1]
      item.setNewMove(new_rank,new_file)
      print('item was moved')
      self.advance()
    elif self.char == 'x':
      print('taking item ....')
      self.advance()
      new_rank = self.char
      self.advance()
      file = int(self.char)
      
      self.advance()
      if self.char == 'E':
        self.advance()
        item.take(new_rank, files[file], self.player)
        item.setNewMove(new_rank, files[file-1])
        print('taked file',file-1)
        print('file',file)
      else:
        item.take(new_rank, files[file-1], self.player)
        item.setNewMove(new_rank, files[file-1])
    return item
  def getname(self,name):
    if self.char == 'P':
      return P
    elif self.char == 'N':
      return N
    elif self.char == 'R':
      return R
    elif self.char == 'B':
      return B
    elif self.char == 'Q':
      return Q
    elif self.char == 'K':
      return K
  def cassel(self):
    casel = ''
    while self.char in 'o-':
      casel += self.char
      self.advance()
      if len(casel)>5: break
      print('casseling ',casel,self.idx)
    if self.player == 'white':
      king = Token(K,'e',7,self.player)
      if casel == 'o-o':
        rock = Token(R,'h',7,self.player)
        king.setNewMove('g',7)
        rock.setNewMove('f',7)
      elif casel == 'o-o-o':
        rock = Token(R,'a',7,self.player)
        king.setNewMove('c',7)
        rock.setNewMove('d',7)
    elif self.player == 'black':
      king = Token(K,'e',0,self.player)
      if casel == 'o-o':
        rock = Token(R,'h',0,self.player)
        king.setNewMove('g',0)
        rock.setNewMove('f',0)
      elif casel == 'o-o-o':
        rock = Token(R,'a',0,self.player)
        king.setNewMove('c',0)
        rock.setNewMove('d',0)
    return [king,rock]


