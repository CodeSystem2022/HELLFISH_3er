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
        
        // Mostramos menú
        System.out.println("""
            1. Suma
            2. Resta
            3. Multiplicación
            4. División
            5. Salir
        """);

        System.out.print("Operación a realizar? ");
        int ope = Integer.parseInt(entrada.nextLine());

        if (ope >= 1 && ope <= 4) {
            System.out.print("Ingrese primer número: ");
            var ope1 = Integer.parseInt(entrada.nextLine());

            System.out.print("Ingrese segundo número: ");
            var ope2 = Integer.parseInt(entrada.nextLine());
            
        } else if (ope == 5) {
            System.out.println("Saliendo del programa");
            
        } else {
            System.out.println("Opción invalida");
        }
    }
}
