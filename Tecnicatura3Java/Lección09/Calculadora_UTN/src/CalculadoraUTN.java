import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("****** Aplicación Calculadora ******");
        // 9.2 Definiendo las variables:
        //var operando1 = 10;
        //var operando2 = 20;
        //var resultado = operando1 + operando2;
        //System.out.println("resultado = " + resultado);

        // 9.3 Ponemos la entrada de información
        System.out.println("Ingrese el valor para el operando 1: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el valor para el operando 2: ");
        var operando2 = Integer.parseInt(entrada.nextLine());
        // Realizamos la operación de suma en la variable "resultado" y lo mostramos por pantalla
        var resultado = operando1 + operando2;
        System.out.println("resultado = " + resultado);
    }
}