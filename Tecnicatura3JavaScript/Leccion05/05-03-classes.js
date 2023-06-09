// Clase 06 - 15-05

class Persona { //Clase padre
    
    static contadorObjetosPersona = 0; //Atributo estatico
    //email = 'Valor default email'; // Atributo NO estatico
 
    static get MAX_OBJ(){ //Simula una constante
    return 5;
    }
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersona < Persona.MAX_OBJ){ 
    this.idPersona = ++Persona.contadorPersona;
} else{ 
    console.log('Se ha superado el maximo de objetos permitidos'); //aparece el mensaje al superarse el limite
    }
    }

    get nombre() {
        return this._nombre;
    }
    
    get apellido() {
        return this._apellido;
    }

    set nombre(s) {
        this._nombre = s;
    }

    set apellido(s) {
        this._apellido = s;
    }

    nombreCompleto() {
        return this._nombre + ' ' + this._apellido;
    }

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
}

class Empleado extends Persona { //Clase hija
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento() {
        return this._departamento;
    }

    set departamento(departamento) {
        this._departamento = departamento;
    }

    nombreCompleto() {
        return super.nombreCompleto() + ", " + this._departamento;
    }
}

let persona1 = new Persona("Martina", "P");
// console.log(persona1);
console.log(persona1.nombre);
persona1.nombre = "Juana Clara";
console.log(persona1.nombre);
persona1.apellido = "M"
console.log(persona1.nombre + persona1.apellido);

let persona2 = new Persona("Carla", "L");
// console.log(persona2);
console.log(persona2.nombre);
persona2.nombre = "Romina";
console.log(persona2.nombre);
persona2.apellido = "S"
console.log(persona2.nombre + persona2.apellido);

let empleado1 = new Empleado("María", "E", "Sistemas");
console.log(empleado1);
console.log(empleado1.nombreCompleto());
console.log(empleado1.toString());
console.log(persona1.toString());

// Object.prototype.toString // Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
console.log(persona1.toString());

// Clase 7 - JAVA 8.1 atributos static
//persona1.saludar(); No se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

//Atributo estatico vs No estatico
//Atributo estatico se asocia a la Clase y en cuanto al Atributo NO estatico se asocia a los objetos
console.log(persona1.email); //Valor default email //accedemos desde el objeto persona1 de la clase padre al atributo NO estatico
console.log(empleado1.email); //Valor default email //accedemos desde el objeto empleado1 de la clase hija al atributo NO estatico
//console.log(Persona.email); undefined  Se demuestra que no se puede acceder al atributo NO estatico desde la clase debido a que es un objeto estatico, sino que esta creando una nueva variable

//Creacion de constantes estaticas
//Para esto debemos crear un metodo estatico que solo nos permitira leer el valor que va a regresar este metodo
console.log(Persona.MAX_OBJ); //Nos regresa al resultado de valor 5
Persona.MAX_OBJ = 10; //Incluso si quisieramos modificar o alterar el valor de la constante no nos permite 
console.log(Persona.MAX_OBJ); 

Let persona4 = new Persona('Pedro','Rios');
console.log(persona4.toString());
Let persona5 = new Persona('Celeste','Callejas');
console.log(persona5.toString());
