package test;

import paquete1.Clase1;
import paquete2.Clase3;
import paquete2.Clase4;

public class TestModificadoresAcceso {
    public static void main( String[] args ) {
        Clase1 clase1 = new Clase1();
        // Clase1 clase11 = new Clase1("a"); // error - el const que permite str como atr es protected
        System.out.println("Clase1 = " + clase1.atributoPublic);
        clase1.metodoPublico();

        Clase3 claseHija = new Clase3();
        System.out.println("Clase3 = " + claseHija);

        Clase4 clase4 = new Clase4("Público");
        System.out.println("clase4 = " + clase4.getAtributoPrivado());
        clase4.setAtributoPrivado("Cambio desde el test");
        System.out.println("clase4 = " + clase4.getAtributoPrivado());
    }
}
