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
        
// 12.5 Hacemos las pruebas del método -> Buscar un estudiante por ID()
//        var estudiante1 = new Estudiante(1);
//        System.out.println("Estudiantes antes de la búsqueda: "+estudiante1);
//        var encontrado = estudianteDao.buscarEstudiantePorID(estudiante1);
//        if(encontrado)
//            System.out.println("Estudiante encontrado: "+estudiante1);
//        else
//            System.out.println("No se encontró al estudiante: "+estudiante1.getIdEstudiante());
    }
}
