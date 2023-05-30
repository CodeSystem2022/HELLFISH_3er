// Clase 06 - 15-05

// let persona3 = new Persona("Carla", "P"); // Error - no se puede acceder
                                             // a una clase antes de su definición

class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre() {
        return this._nombre;
    }

    // video 6 - solo completa esto
    get apellido() {
        return this._apellido;
    }

    set nombre(s) {
        this._nombre = s;
    }

    set apellido(s) {
        this._apellido = s;
    }
}

class Empleado extends Persona {
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
console.log(empleado1.nombre);
