package test;
import accesodatos.IAccesoDatos;
import accesodatos.ImplementacionMySql;

public class TestInterfaces {
    public static void main(String[] args) {
        IAccesoDatos datos = new ImplementacionMySql();

        datos.listar();
    }
}
