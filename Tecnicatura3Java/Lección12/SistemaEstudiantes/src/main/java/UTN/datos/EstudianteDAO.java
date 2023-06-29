// 12.2 Listado de estudiantes con la Clase EstudianteDAO -> Parte 1
package UTN.datos;

import UTN.dominio.Estudiante;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    // Método Listar:
    public List<Estudiante> listar(){
        List<Estudiante> estudiantes = new ArrayList<>();
        // Creamos algunos objetos que son necesarios para comunicarnos con la base de datos:
        PreparedStatement ps; // Ayuda a preparar la sentencia SQL y la envia a la base de datos
        ResultSet rs; // Obtiene el resultado de la consulta SQL en la base de datos


    }

}
