package paquete1;

public class TestDefault {
    public static void main(String[] args) {
        // Accedemos a la clase default Clase2 por medio
        // de la clase pública ClaseHija2
        ClaseHija2 claseH2 = new ClaseHija2();
        claseH2.atributoDefault = "Cambio desde la prueba";
        System.out.println("claseH2 atributo Default = " + claseH2.atributoDefault);
    }
}
