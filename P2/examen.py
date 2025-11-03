class Fabrica:
    def __init__(self,llantas,color,precio):
        self._llantas=llantas
        self._color=color
        self._precio=precio

    @property
    def llantas(self):
        return self._llantas

    
    @llantas.setter
    def llantas(self,llantas):
        self._llantas=llantas
    

    @property
    def color(self):
        return self._color


    @color.setter
    def llantas(self,color):
        self._color=color


    
    @property
    def precio(self):
        return self._precio


    @precio.setter
    def llantas(self,precio):
        self._precio=precio


class Moto(Fabrica):
    def __init__(self, llantas, color, precio,tipoMoto):
        super().__init__(llantas, color, precio)
        self.tipoMoto=tipoMoto

    @property
    def tipoMoto(self):
        return self.tipoMoto


    @tipoMoto.setter
    def tipoMoto(self,tipoMoto):
        self.tipoMoto=tipoMoto

class Coche(Fabrica):
    def __init__(self, llantas, color, precio,tipoCoche):
        super().__init__(llantas, color, precio)
        self.tipoCoche=tipoCoche

    @property
    def tipoCoche(self):
        return self.tipoCoche


    @tipoCoche.setter
    def tipoCoche(self,tipoCoche):
        self.tipoCoche=tipoCoche


moto1=Moto(2,"Rojo",1200,"Sport")
coche1=Coche(4,"Azul",10000,"Sedan")


print(moto1.color,moto1.llantas,moto1.tipoMoto)
print(coche1.color,coche1.precio,coche1.tipoCoche)