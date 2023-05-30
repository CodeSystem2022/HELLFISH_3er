// Clase 06 - 15-05
class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre() {
        return this._nombre;
    }
}

let persona1 = new Persona("Martina", "P");
// console.log(persona1);
console.log(persona1.nombre);

let persona2 = new Persona("Carla", "L");
// console.log(persona2);
console.log(persona2.nombre);
