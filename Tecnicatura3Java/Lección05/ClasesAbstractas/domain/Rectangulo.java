package domain;

public class Rectangulo extends FiguraGeometrica {
    // Constructor
    public Rectangulo (String tipoFigura) {
        super(tipoFigura);
    }

    @Override // implementando del método
  
    public void dibujar() {
        System.out.println("Se imprime un: " + this.getClass().getSimpleName());
    }
}
