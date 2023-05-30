package paquete1;

class Clase2 extends Clase1 { // modificador de acceso default o package 
               // ausencia del modificador
               // solo se puede acceder desde el mismo paquete
    String atributoDefault = "Valor del atributo default";

    //Clase2() {
        //System.out.println("Constructor Default");
    //}

    public Clase2() {
        super();
        this.atributoDefault = "Modificación del atributoDefault";
        System.out.println("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }

    void metodoDefault() {
        System.out.println("Método Default");
    }

}
