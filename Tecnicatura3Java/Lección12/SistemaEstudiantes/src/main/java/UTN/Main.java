package UTN;

import UTN.conexion.Conexion;

public class Main {
    public static void main(String[] args) {
        var conexion = Conexion.getConnection();
        if(conexion != null)
            System.out.println("Conexión exitosa" +conexion);
        else
            System.out.println("Conexión fallida");
        } // Fin main
} // Fin clase Main