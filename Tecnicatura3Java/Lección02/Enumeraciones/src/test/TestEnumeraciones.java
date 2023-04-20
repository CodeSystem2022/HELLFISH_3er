// Clase #2 JAVA - 19/04/2023

package test;

import enumeraciones.Continentes;
import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Día 1: "+ Dias.LUNES); // Las enumeraciones se tratan como cadenas
        //indicarDiaSemana(Dias.LUNES);
        // Ahora no se deben utilizar comillas para indicar el valor de la enumeración, se accede a través del operador de punto
        System.out.println("Continente N° 4: "+ Continentes.AMERICA);
        System.out.println("N° de países en América: "+ Continentes.AMERICA.getPaises());
        System.out.println("N° de habitantes en América: "+ Continentes.AMERICA.getHabitantes());
    }

    private static void indicarDiaSemana(Dias dias){
        switch (dias) {
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
                // agregar todos los días de la semana
                // agregar default
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Séptimo día de la semana");
                break;
            default:
                System.out.println("No es un día válido");
                break;


        }
    }
}
