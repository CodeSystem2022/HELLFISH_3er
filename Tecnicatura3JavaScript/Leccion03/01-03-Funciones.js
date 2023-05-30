miFuncion(8,2); //Esto se le conoce como hosting

function miFuncion(a, b){
    // console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamando la Funcion
miFuncion(5,4);

let resultado = miFuncion(6, 7);
console.log(resultado);

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


console.log(typeof miFuncion); // tipo function, que es un objeto y tiene métodos

function miFuncionDos(a, b) {
    //console.log(arguments); // método arguments devuelve {0:5, 1:7} los valores con que fue llamada

    console.log(arguments.length); // cantidad de arg que recive la función, no tiene en cuenta 
    // los args declarados en la definición sino los arg con que fue llamada
    // no se puede usar arguments.length fuera de la función
}

miFuncionDos(5, 7);

// toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); // transcribe la función a txt, no el retorno sino la declaración de
// la función en sí, utilizando cosas raras

// Funciones Flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7);
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


