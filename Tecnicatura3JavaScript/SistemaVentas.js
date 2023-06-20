class Producto{
    static ContadorProductos = 0;
    constructor(nombre, precio){
        this._idProducto = ++Producto.ContadorProductos;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){ //Template Literals: Nos permite insertar código dinamicamente
        return 'idProducto : ${this._idProducto}, nombre: ${this._nombre}, precio: ${this._precio}';
    }
}
//Fin de la clase producto

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

// Pruebas con la relación de agregación
const producto1 = new Producto("Pizza Napolitana", 2200);
const producto2 = new Producto("Quilmes", 450);
const producto3 = new Producto("Imperial IPA", 500);

const orden1 = new Orden()
const orden2 = new Orden()
const orden3 = new Orden()

orden1.agregarProducto(producto1)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto2)

orden2.agregarProducto(producto1)
orden2.agregarProducto(producto1)
orden2.agregarProducto(producto3)
orden2.agregarProducto(producto3)
orden2.agregarProducto(producto3)

orden3.agregarProducto(producto3)
orden3.agregarProducto(producto3)
orden3.agregarProducto(producto2)
orden3.agregarProducto(producto2)
orden3.agregarProducto(producto3)
orden3.agregarProducto(producto1)  // Sexto elemento - no se tiene en cuenta
