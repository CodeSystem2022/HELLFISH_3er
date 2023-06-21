import java.util.Scanner;
public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while(true){//Ciclo infinito
        System.out.println("****** Aplicación Calculadora ******");
            mostrarMenu();
            try{
        var opecion = Integer.parseInt(entrada.nextLine());
        if (operacion >= 1 && operacion <= 4) {
            ejecutarOperacion(operacion, entrada);
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

    private static void mostrarMenu(){
        System.out.println("""
                           1. SUMA
                           2. RESTA
                           3. MULTIPLICACION
                           4. DIVISION
                           5. SALIR
                           """);
        System.out.print("Seleccione una operacion: ");
    }//Fin metodo mostrarMenu
    private static void ejecutarOperacion(int operacion, Scanner entrada){
        // 9.3 Ponemos la entrada de información
        System.out.print("Ingrese el valor para el operando 1: ");
        var operando1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Ingrese el valor para el operando 2: ");
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
        default -> System.out.println("Opcion Erronea: "+operacion);
    }//Fin switch
    }//Fin metodo ejecutarOperacion
}
