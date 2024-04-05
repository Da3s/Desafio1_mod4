from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipo_masa

#ingredientes_proteicos = ['pollo', 'vacuno', 'carne vegetal']
#ingredientes_vegetales = ['tomate', 'aceitunas', 'champiñones']
#tipo_masa = ['tradicional', 'delgada']

class Pizza():
    precio = 10000
    
    
    def __init__(self):
        self.proteina = ()
        self.vegetal_1 = ()
        self.vegetal_2 = ()
        self.masa = ()
        self.es_valido = ()
        
        
    # Validar elemento en la lista
    @staticmethod
    def validar(elemento, valor):
        return elemento in valor
    
    # Realizar el pedido
    def pedido(self):
        print('Ingrese la proteina que desea en la pizza: ')
        print('Pollo, Vacuno o Carne Vegetal')
        self.proteina = input('Proteina: ').lower()
        print('Ingrese el vegetal que desea en la pizza: ')
        print('Tomate, Aceitunas o Champiñones')
        self.vegetal_1 = input('Primer vegetal: ').lower()
        self.vegetal_2 = input('Segundo vegetal: ').lower()
        print('Ingrese el tipo de masa que desea en la pizza: ')
        print('Tradicional o Delgada')
        self.masa = input('Masa: ').lower()
        
        # Verificar si los ingredientes ingresados son los que se ofrecen
        self.es_valido = (
            self.validar(self.proteina, ingredientes_proteicos) and
            self.validar(self.vegetal_1, ingredientes_vegetales) and
            self.validar(self.vegetal_2, ingredientes_vegetales) and
            self.validar(self.masa, tipo_masa)
            
        )