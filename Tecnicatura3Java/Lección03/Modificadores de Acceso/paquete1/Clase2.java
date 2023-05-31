package paquete1;

class Clase2 { // modificador de acceso default o package 
               // ausencia del modificador
               // solo se puede acceder desde el mismo paquete
    String atributoDefault = "Valor del atributo default";

    Clase2() {
        System.out.println("Constructor Default");
    }

    void metodoDefault() {
        System.out.println("Método Default");
    }

}
