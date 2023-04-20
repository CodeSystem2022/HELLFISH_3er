// Clase #2 JAVA - 19/04/2023

package enumeraciones;

public enum Continentes {
    AFRICA(53, "1.2 millones"),
    EUROPA(46, "0.7 millones"),
    ASIA(44, "1.5 millones"),
    AMERICA(35, "0.9 millones"),
    OCEANIA(14, "0.4 millones");

    private final int paises;
    private String habitantes;

    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

    // Método GET
    public int getPaises(){
        return this.paises;
    }

    public String getHabitantes(){
        return this.habitantes;
    }
}

