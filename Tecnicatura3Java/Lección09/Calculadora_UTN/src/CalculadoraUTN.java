import java.util.Scanner;

public class CalculadoraUTN {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while(true){//Ciclo infinito
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
            try{
        var ope = Integer.parseInt(entrada.nextLine());

        if (operacion >= 1 && ope <= 4) {
            System.out.print("Ingrese primer número: ");
            var operando1 = Integer.parseInt(entrada.nextLine());
            System.out.print("Ingrese segundo número: ");
            var operando2 = Integer.parseInt(entrada.nextLine());

            int resultado;
        
    switch(operacion){
        case 1 -> { //Suma
            resultado = operando1 + operando2;
            System.out.println("Resultado de la suma: "+resultado);
        }
        case 2 -> { //Resta
            resultado = operando1 - operando2;
            System.out.println("Resultado de la resta: "+resultado);
        }
        case 3 -> { //Multiplicacion
            resultado = operando1 * operando2;
            System.out.println("Resultado de la multiplicacion: "+resultado);
        }
        case 4 -> { //Division
            resultado = operando1 / operando2;
            System.out.println("Resultado de la division: "+resultado);
        }
        default -> System.out.println("Opcion Erronea: "+ operacion);
    }//Fin switch
        } //Fin del if
        else if (operacion == 5) {
            System.out.println("Saliendo del programa");
            break;//Rompe el ciclo infinito
        } else {
            System.out.println("Opción invalida"+operacion);
        }
            //IMPRIMIMOS UN SALTO DE LINEA
            System.out.println("");
                }catch(Exception e){//Termina el try y comienza el catch
            System.out.println("Ocurrio un error: "+e.getMessage());
            System.out.println("");
        }//fin del catch
        }//Fin while
    }//Fin de la main
}
