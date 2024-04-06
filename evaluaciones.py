from pizza import Pizza

# Imprimir los atributos dentro de la clase Pizza
print('Atributos de la clase Pizza: ', 'Precio', Pizza.precio)


# Consultar si en la lista de ingredientes tengo salsa de tomate
print('¿Esta incluida la salsa de tomate en la lista de ingredientes?')
print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


# Solicitar ingredientes y tipo de masa
armar_pedido = Pizza()
armar_pedido.pedido()


# Verificar si el pedido es valido segun lo ofrecido
print(f'Su pizza como proteina tiene {armar_pedido.proteina}, los vegetales seleccionados son {armar_pedido.vegetal_1} y {armar_pedido.vegetal_2}, el tipo de masa es {armar_pedido.masa}.')
print(f'Ingredientes dentro de lo ofrecido? {armar_pedido.es_valido}')


# Verificar si la clase Pizza es una pizza valida o no, debe lanzar un error
print('La clase Pizza es una pizza valida?', Pizza.es_valido)