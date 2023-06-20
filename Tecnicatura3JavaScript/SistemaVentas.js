class Orden {
    static contOrdenes = 0
    static MAX_PRODUCTOS = 5;

    constructor() {
        this.idOrden = ++Orden.contOrdenes;
        this.productos = []
        this.contProdAgregados = 0;
    }

    agregarProducto(producto) {
        this.contProdAgregados++
        if (this.contProdAgregados <= Orden.MAX_PRODUCTOS) {
            this.productos.push(producto);
        } else {
            this.contProdAgregados = Orden.MAX_PRODUCTOS;  // ya no aumentamos el contador de productos agregados
        }
    }

    calcularTotal() {
        let total = 0;
        for (let i = 0; i < this.productos.length; i++){
            total += this.productos[i].precio;
        }
        return total;
    }

    mostrarOrden() {
        return `
    \n- Orden: ${this.idOrden}
    productos: ${this.productos}
    \ncontador productos agregados: ${this.contProdAgregados}
    \nTotal de la orden: ${this.calcularTotal()}\n`
    }
}
