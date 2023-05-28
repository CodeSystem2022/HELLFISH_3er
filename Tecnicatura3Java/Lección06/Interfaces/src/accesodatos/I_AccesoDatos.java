/* JAVA Clase 7 - 24/05/2023 */
package accesodatos;
/**
 *
 * @author ASCUA
 */
public interface I_AccesoDatos {
    int MAX_REGISTRO = 10; // si o si debemos asignar para evitar problemas
    
    // Método insertar es abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar();
    
    void eliminar();
}
