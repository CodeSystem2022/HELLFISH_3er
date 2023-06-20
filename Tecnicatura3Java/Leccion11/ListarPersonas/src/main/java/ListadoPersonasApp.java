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
}
