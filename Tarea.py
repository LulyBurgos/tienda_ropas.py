class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"


class Categoria:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        return ', '.join([str(p) for p in self.__productos])

    def __str__(self):
        return f"{self.nombre}: {self.mostrar_productos()}"


class Tienda:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__categorias = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_categoria(self, categoria):
        self.__categorias.append(categoria)

    def mostrar_productos(self):
        for categoria in self.__categorias:
            print(categoria)

    def __str__(self):
        return f"Tienda: {self.nombre}"


class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    @property
    def talla(self):
        return self.__talla

    def __str__(self):
        return f"{super().__str__()} - Talla: {self.talla}"


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    @property
    def talla(self):
        return self.__talla

    def __str__(self):
        return f"{super().__str__()} - Talla: {self.talla}"


class Zapato(Producto):
    def __init__(self, nombre, precio, numero):
        super().__init__(nombre, precio)
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def __str__(self):
        return f"{super().__str__()} - Número: {self.numero}"


# Uso del programa
if __name__ == "__main__":
    # Crear productos
    camisa = Camisa("Camisa blanca", 20, "M")
    pantalon = Pantalon("Pantalon negro", 30, "L")
    zapato = Zapato("Zapato rojo", 40, 42)

    # Crear categorías
    categoria_camisas = Categoria("Camisas")
    categoria_pantalones = Categoria("Pantalones")
    categoria_zapatos = Categoria("Zapatos")

    # Agregar productos a las categorías
    categoria_camisas.agregar_producto(camisa)
    categoria_pantalones.agregar_producto(pantalon)
    categoria_zapatos.agregar_producto(zapato)

    # Crear tienda y agregar categorías
    tienda = Tienda("Tienda de Ropa")
    tienda.agregar_categoria(categoria_camisas)
    tienda.agregar_categoria(categoria_pantalones)
    tienda.agregar_categoria(categoria_zapatos)

    # Mostrar productos en la tienda
    print(tienda)
    tienda.mostrar_productos()