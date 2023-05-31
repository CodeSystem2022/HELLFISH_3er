package paquete2;

public class Clase4 {
    private String atributoPrivado = "Atributo Privado";

    private Clase4() {
        System.out.println("Constructor Privado");
    }

    // Creamos Constructor público para poder crear objetos
    public Clase4(String arg) {
        this(); // Con esto llamamos al constructor vacio y privado
        System.out.println("Constructor Público");
    }

    private void metodoPrivado() {
        System.out.println("Método Privado");
    }

    public String getAtributoPrivado() {
        return this.atributoPrivado;
    }

    public void setAtributoPrivado(String nuevoAtrib) {
        this.atributoPrivado = nuevoAtrib;
    }
}
