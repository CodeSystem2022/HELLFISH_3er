// Clase 3 JAVA - Auto Boxing Unboxing 25/04/2023

package test;
/**
 * @author ASCUA
 */
public class TestAutoBoxingUnboxing {
    public static void main(String[] args) {
        // Clases envolventes o Wrapper
        
        /*
            Clases envolventes de tipos primitivos
            1. int = la clase envolvente es Integer (enteros)
            2. long = la clase envolvente es Long
            3. float = la clase envolvente es Float
            4. double = la clase envolvente es Double 
            5. boolean = la clase envolvente es Boolean
            6. byte = la clase envolvente es Byte
            7. char = la clase envolvente es Character
            8. short = la clase envolvente es Short
        */
        
        int enteroPrimitivo = 10; // Tipo Primitivo
        System.out.println("enteroPrimitivo = " + enteroPrimitivo);
        Integer entero = 10; // Tipo Object con la clase Integer
        System.out.println("entero = " + entero.doubleValue()); // AutoBoxing = lo paso nuevamente a un tipo Primitivo
        
        //Integer entero = 10 // Integer es una clase que nos permite acceder a diferentes métodos y funciones mediante el punto
        // entero.byteValue(); 
        // Esta variable "entero" ya no es una variable primitiva, ya es un objeto de la clase Integer       
        
        // Unboxing:
        int entero2 = entero; // Lo contrario a Boxing
        System.out.println("entero2 = " + entero2);
        
        
        
    }
}
