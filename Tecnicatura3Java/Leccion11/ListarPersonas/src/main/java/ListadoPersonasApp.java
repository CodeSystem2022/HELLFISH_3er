import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        List<Persona> personas = new ArrayList<>();

        // Menu
        var salir = false;
        while (!salir) {
            mostrarMenu();
            try {
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e) {
                System.out.println("Ocurrió un error: " + e.getMessage());
            }
            System.out.println();
        }
    }

    private static void mostrarMenu() {
        System.out.print("""
                ******* Listado de Personas *******
                1. Agregar
                2. Listar
                3. Salir
                """);
        System.out.print("Ingrese opción: ");
    }

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        // Revisamos opción ingresada a traves de un switch
        switch (opcion) {
            case 1 -> { // Agregar persona
                System.out.print("Ingrese un nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Ingrese un teléfono: ");
                var tel = entrada.nextLine();
                System.out.print("Ingrese un email: ");
                var email = entrada.nextLine();
                // Creamos obj persona
                var persona = new Persona(nombre, tel, email);
                // Agregamos a la lista
                personas.add(persona);
                System.out.println("La lista tiene: " + personas.size() + " elementos");
            } case 2 -> { // Listar personas
                System.out.println("Listado de personas:");
                // lambda
                // personas.forEach((persona) -> System.out.println(persona));

                // método de referencia
                personas.forEach(System.out::println);;
            }
        }
    }
}
