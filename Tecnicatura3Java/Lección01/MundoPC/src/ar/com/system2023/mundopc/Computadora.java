
package ar.com.system2023.mundopc;

public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;
    
    // Constructor vacío
    private Computadora(){
        this.idComputadora = ++Computadora.contadorComputadoras;
    }
    
    // Constructor 2
    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton){
        this(); // Llamado al constructor vacío
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }

    public int getIdComputadora(){
        return idComputadora;
    }
    
    public String getNombre() {
        return nombre;
    }

    public Monitor getMonitor() {
        return this.monitor;
    }

    public Teclado getTeclado() {
        return this.teclado;
    }

    public Raton getRaton() {
        return raton;
    }

    @Override
    public String toString() {
        return "Computadora{" + "idComputadora=" + idComputadora + ", nombre=" + nombre + ", monitor=" + monitor + ", teclado=" + teclado + ", raton=" + raton + '}';
    }
}

