// 12.2 Listado de estudiantes con la Clase EstudianteDAO -> Parte 1
package UTN.datos;

import UTN.dominio.Estudiante;
import java.sql.Connection;

import static UTN.conexion.Conexion.getConnetion;
import java.sql.DriverManager;
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
        //Creamos un objeto de tipo Conexion
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2022 ORDER BY estudiantes2022";
        try{
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante;
                estudiante.setIdEstudiante(rs.getInt("idestudiante2022"));
                estudiante.setNombre(rs.getString("Nombre"));
                estudiante.setApellido(rs.getString("Apellido"));
                estudiante.setTelefono(rs.getString("Telefono"));
                estudiante.setEmail(rs.getString("Email"));
                //Falta agregarlo a la lista
                estudiantes.add(estudiante);
            }
        } catch (Exception e){
            System.out.println("Ocurrio un error al seleccionar datos: "+e.getMessage());
        }
        finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println ("Ocurrio un error al cerrar la conexion:   "+e.getMessage()); 
            }

            } //Fin Finally
            return estudiantes;

        } //Fin del metodo listar

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



//Metodo para modificar estudiante
public boolean modificarEstudiante (Estudiante estudiante){
    PreparedStatement ps;
    Connection con getConnection
    String sql = "UPDATE estudiantes2022 SET Nombre=?, Apellido=?, Telefono= ?, Email= ? WHERE idestudiantes2022= ?"
    
    try{
       ps= con.prepareStatement(SQL);
       ps.setString(1, estudiante.getNombre());
       ps.setString(2, estudiante.getApellido());
       ps.setString(3, estudiante.getTelefono());
       ps.setString(4, estudiante.getEmail());
       ps.setIn(5, estudiante.getIdEstudiante());
       ps.execute();
       return true;

    } catch (Exception e) {
        System.out.println("Error al modificar estudiante:  "+e getMessage());
    }
//Fin catch

finally{
    
    try{

        con.close();

    } catch(Exception e){
        System.out.println ("Error al cerrar la conexion" +e.getMessage());

    } //Fin catch

}//Fin finally

  return false;

} //Fin metodo ModificarEstudiante
