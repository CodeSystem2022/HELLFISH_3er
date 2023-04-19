package mundopc; // Clase 1 Programación 3, JAVA - 5/04/2023 

import ar.com.system2023.mundopc.*;

public class mundoPC {

    public static void main(String[] args) {
        
        // Creamos las ordenes, las inicializamos y luego las utilizamos
        
        Orden orden1 = new Orden(); // Inicializamos el arreglo aunque está vacío
        Orden orden2 = new Orden(); // Una nueva lista para el objeto orden2
        Orden orden3 = new Orden();
        Orden orden4 = new Orden();
        Orden orden5 = new Orden();
        Orden orden6 = new Orden();
        Orden orden7 = new Orden();
        Orden orden8 = new Orden();
        Orden orden9 = new Orden();
        Orden orden10 = new Orden(); // La última orden de computadoras
        
        // 1. Creamos los objetos, empezamos con la marca HP 
        Monitor monitorHP = new Monitor("HP", 14); // Importar la clase
        Teclado tecladoHP = new Teclado("HP", "Bluetooth");
        Raton ratonHP = new Raton("HP", "Bluetooth");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        // Agregamos PC #1 marca HP a la orden: (luego de haberla creado)
        orden1.agregarComputadora(computadoraHP);
        orden1.mostrarOrden();

        // 2. Creamos otro objeto de diferente marca, esta vez de tipo Gamer
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        // Agregamos PC #2 Gamer a la orden
        orden2.agregarComputadora(computadoraGamer);
        orden2.mostrarOrden();
        
        // Tarea: Crear más objetos de tipo computadora con todos sus elementos
        // Completar la lista en el objeto orden que llegue a 10 elementos
        // Probar de esta manera los métodos al máximo rendimiento
        
        // 3. Creamos otro objeto, esta vez de marca ASUS
        Monitor monitorAsus = new Monitor("ASUS", 15.6); // La marca y el tamaño de pantalla (15.6 pulgadas)
        Teclado tecladoAsus = new Teclado("ASUS", "Bluetooth");
        Raton ratonAsus = new Raton("ASUS", "Touchpad");
        Computadora computadoraCuatro = new Computadora("ASUS 15.6", monitorAsus, tecladoAsus, ratonAsus);
        // Agregamos la computadora #3 a la orden y la mostramos
        orden3.agregarComputadora(computadoraCuatro);
        orden3.mostrarOrden();
        
        // 4. Creamos otro objeto de marca HP ENVY
        Monitor monitorEnvy = new Monitor("HP ENVY", 13.3);
        Teclado tecladoEnvy = new Teclado("HP ENVY", "Silver mate");
        Raton ratonEnvy = new Raton("Envy", "Touchpad");
        Computadora computadoraCinco = new Computadora("Ultrabook HP ENVY 13.3", monitorEnvy, tecladoEnvy, ratonEnvy);
        // Agregamos la computadora #4 a la orden y la mostramos 
        orden4.agregarComputadora(computadoraCinco);
        orden4.mostrarOrden();
       
        // 5. Creamos otro objeto de marca Ultrabook HP
        Computadora computadorasUltrabook = new Computadora("Ultrabook HP 13", monitorHP, tecladoGamer, ratonHP);
        // Agregamos la computadora #5 a la orden y la mostramos
        orden5.agregarComputadora(computadorasUltrabook);
        orden5.mostrarOrden();

        // 6. Creamos otro objeto de marca HP Gamer RYZEN 5 4300U 8GB
        Monitor monitorUltrabookHp = new Monitor("Ultrabook HP", 14);
        Teclado tecladoUltrabookHP = new Teclado("Ultrabook HP", "color black mate");
        Raton ratonUltrabookHP = new Raton("Touchpad", "Ultrabook HP");
        Computadora computadoraSeis = new Computadora("Ultrabook HP RYZEN 5 4300U 12GB RAM", monitorUltrabookHp, tecladoUltrabookHP, ratonUltrabookHP);
        // Agregamos la computadora #6 a la orden y la mostramos
        orden6.agregarComputadora(computadoraSeis);
        orden6.mostrarOrden();
        
        // 7. Creamos otro objeto de marca LENOVO
        Monitor monitorLenovo = new Monitor("LENOVO", 14);
        Teclado tecladoLenovo = new Teclado("LENOVO", "silver");
        Raton ratonLenovo = new Raton("LENOVO", "Integrado ultraslim");
        Computadora computadoraSiete = new Computadora("LENOVO RYZEN 3 8GB RAM", monitorLenovo, tecladoLenovo, ratonLenovo);
        // Agregamos la computadora #7 a la orden y la mostramos
        orden7.agregarComputadora(computadoraSiete);
        orden7.mostrarOrden();
        
        // 8. Creamos otro objeto de marca Apple
        Monitor monitorApple = new Monitor("Apple", 13);
        Teclado tecladoApple = new Teclado("Magic Keyboard", "Bluetooth");
        Raton ratonApple = new Raton("Apple Mouse", "ultra ligero");
        Computadora computadoraOcho = new Computadora("Apple Macbook 13 8GB i5", monitorApple, tecladoApple, ratonApple);
        // Agregamos la computadora #8 a la orden y la mostramos
        orden8.agregarComputadora(computadoraOcho);
        orden8.mostrarOrden();
        
        // 9. Creamos otro objeto de marca Samsung
        Monitor monitorSAMSUNG = new Monitor("SAMSUNG", 27);
        Teclado tecladoSAMSUNG = new Teclado("SAMSUNG keyboard", "Bluetooth 6.0");
        Raton ratonSAMSUNG = new Raton("SAMSUNG mouse", "Bluetooth");
        Computadora computadoraNueve = new Computadora("SAMSUNG Galaxy Book2 Pro", monitorSAMSUNG, tecladoSAMSUNG, ratonSAMSUNG);
        // Agregamos la computadora #9 a la orden y la mostramos
        orden9.agregarComputadora(computadoraNueve);
        orden9.mostrarOrden();
       
        // 10. Creamos otro objeto de marca HP DragonFly
        Monitor monitorDragonFly = new Monitor("HP DRAGONFLY", 17);
        Teclado tecladoDragonFly = new Teclado("HP DRAGONFLY", "black matte");
        Raton ratonDragonFly = new Raton("Reciclado con plásticos marinos", "Touchpad");
        Computadora computadoraDiez = new Computadora("HP DRAGONFLY 17 16GB RAM RECYCLED", monitorDragonFly, tecladoDragonFly, ratonDragonFly);
        // Agregamos la computadora #10 a la orden y la mostramos
        orden10.agregarComputadora(computadoraDiez);
        orden10.mostrarOrden();
    }
}