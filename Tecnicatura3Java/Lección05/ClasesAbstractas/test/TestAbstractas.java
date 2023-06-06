package test;

import domain.*;

public class TestAbstractas {
    public static void main( String[] args ) {                   // Upcasting: tipo hija (Rectangulo) a tipo padre (FG)
        FiguraGeometrica figura = new Rectangulo("Rectangulo");
        figura.dibujar();
        
    }
}
