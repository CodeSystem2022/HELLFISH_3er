// Clase 7 - JAVA 8.1: Atributos Estáticos parte 1 y 2
// palabra static con métodos
// 29/05/2023

// Sobreescribiendo el método de la clase padre (Object)
    toString(){ // Regresa un String
    // Se aplica el polimorfismo que significa = múltiples formas en tiempo de ejecución
    // El método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
}

static saludar(){
    console.log('Saludos desde este método static');
}

static saludar2(persona){
    console.log(persona.nombre+' '+persona.apellido);
}

class Empleado extends Persona{ // clase hija
	constructor(nombre, apellido, departamento){
		super(nombre, apellido);
		this._departamento = departamento;
	}
...

// Object.prototype.toString // Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString);
console.log(persona1.toString());

..
//persona1.saludar(); no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

