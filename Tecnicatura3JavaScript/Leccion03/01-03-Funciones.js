miFuncion(8,2); //Esto se le conoce como hosting

function miFuncion(a, b){
    console.log("Sumamos: "+ (a + b));
}

//Llamando la Funcion
miFuncion(5,4);

// Paso por valor
// Tipos primitivos
let k = 10;
function cambiarValor(a) {
    a = 20; // variable de uso dentro de la función
}

cambiarValor(k); // le pasamos solo el valor de k, no la referencia a k, no se va a modificar el valor de k
