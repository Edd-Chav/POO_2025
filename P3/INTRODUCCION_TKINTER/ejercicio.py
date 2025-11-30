class Figuras:
    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible
        
    def estaVisible(self):
        return self.visible
    
    def mostrar(self):
        return self.x,self.y,self.visible
    
    def ocultar(self):
        self.visible=False
    
    def mover(self,x,y):
        coordenada=int(input("Coordenada x: "))
        coordenada2=int(input("Coordenada y: "))
        return coordenada,coordenada2
    
    def calcularArea(self):
        area=self.x*self.y
        return area
    
    
class Rectangulos(Figuras):
    def __init__(self, x, y, visible,alto, ancho):
        super().__init__(x, y, visible)
        self.__alto=alto
        self.__ancho=ancho
     
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto):
        self.__alto=alto
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho=ancho 
        
    def ocultar(self):
        self.visible=False
    
    def mover(self):
        coordenada=int(input("Coordenada x: "))
        coordenada2=int(input("Coordenada y: "))
        return coordenada,coordenada2
    
    def calcularArea(self):
        area= self.__alto *self.__ancho
        return area
    
    
class Circulos(Figuras):
    def __init__(self, x, y, visible,radio):
        super().__init__(x, y, visible)
        self.__radio=radio
        
    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self,radio):
        self.__radio=radio
    
    
    def ocultar(self):
        self.visible=False
    
    def mover(self):
        coordenada=int(input("Coordenada x: "))
        coordenada2=int(input("Coordenada y: "))
        return coordenada,coordenada2
    
    def calcularArea(self):
        area=3.14*self.__radio*self.__radio
        return f"{area}"
    

rectangulo1=Rectangulos(3,4,True,10,20)

circulo1=Circulos(3,3,True,6)

print(rectangulo1.calcularArea())
