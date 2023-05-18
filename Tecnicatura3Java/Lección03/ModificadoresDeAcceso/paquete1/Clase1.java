// Clase 3 JAVA - 25/04/2023
package paquete1;
/**
 *
 * @author ASCUA
 */
public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";
    
    // Constructor public
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    // Constructor protected
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
    
    // Método public
    public void metodoPublico(){
        System.out.println("Método public en ejecución");
    }
    
    // Método protected
    protected void metodoProtected(){
        System.out.println("Método protected");
    }
}
