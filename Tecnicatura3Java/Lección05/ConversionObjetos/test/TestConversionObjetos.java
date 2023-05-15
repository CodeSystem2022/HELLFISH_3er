package test;

import domain.*;

public class TestConversionObjetos {
    public static void main( String[] args ) {
        Empleado empleado;

        empleado = new Escritor("Juana", 5000, TipoEscritura.CLASICO);
        // System.out.println("empleado = " + empleado);

        // System.out.println(empleado.obtenerDetalles());  // tiene en cuenta override
        // de la clase Escritor

        // empleado.getTipoEscritura(); // método no definido en clase empleado, por lo que
        // no se puede usar

        // Para esto se utiliza el downcasting
        // convierte a un tipo padre en tipo hijo para así acceder a métodos
        // que solo se definieron en la clase hija

        // Downcasting forma 1
        // ((Escritor)empleado).getTipoEscritura();

        // Downcasting forma 2
        Escritor escritor = (Escritor)empleado;
        escritor.getTipoEscritura();

        // Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
