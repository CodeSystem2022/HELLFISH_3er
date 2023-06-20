public class Persona {
    private int id;
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas = 0;

    // Constructor vacio
    public Persona() {
        this.id = ++Persona.numeroPersonas;
    }

    // Constructor con parámetros (sobrecarga de constructores)
    public Persona(String nombre, String tel, String email) {
        this(); // llamada al constructor vacío
        this.nombre = nombre;
        this.tel = tel;
        this.email = email;
    }

    // Getters
    public int getId() {
        return this.id;
    }

    public String getNombre() {
        return this.nombre;
    }

    public String getTel() {
        return this.tel;
    }

    public String getEmail() {
        return this.email;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Persona { id = " + this.id + ", nombre = " + this.nombre + ", tel = " + this.tel + ", email = " + this.email + " }";
    }

    // Prueba del método toString()
    public static void main(String[] args) {
        Persona persona1 = new Persona("María", "234882242", "Marimaria@gmail.com");
        System.out.println(persona1);
    }
}
