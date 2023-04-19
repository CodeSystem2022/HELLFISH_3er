
package ar.com.system2023.mundopc;

public class dispositivoEntrada {
    private String tipoEntrada;
    private String marca;
    
    public dispositivoEntrada(String tipoEntrada, String marca){
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }
    
    // Getters y Setters
    
    public String getTipoEntrada() {
        return this.tipoEntrada;
    }

    public void setTipoEntrada(String tipoEntrada) {
        this.tipoEntrada = tipoEntrada;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "dispositivoEntrada{" + "tipoEntrada=" + tipoEntrada + ", marca=" + marca + '}';
    }
}