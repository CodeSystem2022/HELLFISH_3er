miFuncion(8,2); //Esto se le conoce como hosting

function miFuncion(a, b){
    // console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamando la Funcion
miFuncion(5,4);

let resultado = miFuncion(6, 7);
console.log(resultado);

// Paso por valor
// Tipos primitivos
let k = 10;
function cambiarValor(a) {
    a = 20; // variable de uso dentro de la función
}

cambiarValor(k); // le pasamos solo el valor de k, no la referencia a k, no se va a modificar el valor de k

// Paso por referencia
const persona = {
    nombre: "Juan",
    apellid: "Leper"
}

function cambiarValorObjeto(p1) {
    p1.nombre = "Juana";
    p1.apellido = "Lepez";
}

cambiarValorObjeto(persona); // se envia la dirección de memoria del obj persona y modifica todo
console.log(persona);

//Maricel Luna
// Declaramos una función de tipo expresión
let x = function(a, b) { return a + b };
resultado = x (5, 6);
console.log(resultado);


//Maricel Luna
// Funciones de tipo self e invoking
(function(a, b) {
    console.log("Ejecutando la función: " + (a + b));
} (9, 6));
