package test;

import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificadoresAcceso {
    public static void main( String[] args ) {
        Clase1 clase1 = new Clase1();
        // Clase1 clase11 = new Clase1("a"); // error - el const que permite str como atr es protected
        System.out.println("Clase1 = " + clase1.atributoPublic);
        clase1.metodoPublico();

        Clase3 claseHija = new Clase3();
        System.out.println("Clase3 = " + claseHija);
    }
}
