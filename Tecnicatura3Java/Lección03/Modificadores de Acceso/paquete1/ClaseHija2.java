package paquete1;

public class ClaseHija2 extends Clase2 {
    // Una clase default (Clase2) puede ser padre también
    public ClaseHija2() {
        super();
        this.atributoDefault = "Modificación atributo default";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }
}
