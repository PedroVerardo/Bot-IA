#caso dano recebido
class Zigzag:
    def __init__(self) -> None:
        self.cont = 0

    def update_state(self):
        self.cont += 1
        if self.cont == 8:
            self.cont = 0
            return "virar_esquerda"
        if self.cont == 6:
            return "virar_esquerda"
        if self.cont == 4:
            return "virar_direita"
        elif self.cont == 2:
            return "virar_direita"
        return "andar"

#maneiramais efetiva de pegar informações no mapa
class Explore:
    def __init__(self,x,y,direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction
    def update_state(self):
        print(self.x,self.y)
        if(self.x == 1 and self.direction == "west"):
            return "virar_esquerda"
        elif(self.x == 58 and self.direction == "east"):
            return "virar_direita"
        elif(self.y == 1 and self.direction == "north"):
            return "virar_esquerda"
        elif(self.y == 33 and self.direction == "east"):
            return "virar_direita"
        return "andar"

#dano nos inimigos
class Atirar:
    def __init__(self,gameIA) -> None:
        self.gameIA = gameIA
    def update_state(self):
        self.gameIA.reset_state()
        return "atacar"

#cria o caminho para o power up
class CriaPath:
    def __init__(self,marcados) -> None:
        self.marcos = marcados

    def update_state(self):
        pass

class Blocked:
    def __init__(self,gameIA) -> None:
        self.cont = 1
        self.gameIA = gameIA
        self.dir = self.gameIA.dir
        self.rigt = "virar_direita"
        self.left = "virar_esquerda"
        self.last_position = [(self.gameIA.player.x,self.gameIA.player.y)]
    def update_state(self):
        if self.gameIA.player.x == 0 or self.gameIA.player.x == 59 or self.gameIA.player.y == 0 or self.gameIA.player.y == 34:
            self.gameIA.bords_state()
        if self.cont == 0:
            self.gameIA.reset_state()
        if (self.gameIA.player.x,self.gameIA.player.y) in self.last_position:
            return "virar_esquerda"
        self.cont += 1
        if self.cont == 9:
            self.cont = 0
            return "virar_direita"
        if self.cont == 7:
            return "virar_esquerda"
        if self.cont == 4:
            return "virar_esquerda"
        elif self.cont == 2:
            return "virar_direita"
        return "andar"

class PegarT:
    def __init__(self,gameIA) -> None:
        self.gameIA = gameIA
    def update_state(self):
        self.gameIA.reset_state()
        return "pegar_ouro"

class PegarP:
    def __init__(self,gameIA) -> None:
        self.gameIA = gameIA
    def update_state(self):
        self.gameIA.reset_state()
        return "pegar_powerup"

class Breeze:
    def __init__(self,gameIA) -> None:
        self.gameIA = gameIA
        #self.lista_temp = gameIA.GetObservableAdjacentPositions()
        self.cont = 0
        self.tentativa = 2

    def update_state(self):
        if self.tentativa%2 == 0:
            self.tentativa += 1
            if self.cont == 0:
                self.cont += 1
                return "andar_re"
            if self.cont == 1:
                self.cont = 0
                self.gameIA.reset_state()
                return "virar_esquerda"
        else:
            self.gameIA.reset_state()
            return "virar_esquerda"


class Boards:
    def __init__(self,gameIA) -> None:
        self.gameIA = gameIA
    
    def update_state(self):
        if(self.gameIA.dir == "north" and self.gameIA.player.y == 0):
            return "virar_direita"
        elif(self.gameIA.dir == "south" and self.gameIA.player.y == 34):
            return "virar_esquerda"
        elif(self.gameIA.dir == "west" and self.gameIA.player.x == 0):
            return "virar_direita"
        elif(self.gameIA.dir == "east" and self.gameIA.player.x == 59):
            return "virar_direita"
        return "andar"