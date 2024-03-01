public class NumarComplex {
    private double re; //partea reala
    private double im; //partea imaginara

    public NumarComplex(double re, double im) {
        this.re = re;
        this.im = im;
    }

    //Metoda pentru adunare
    public NumarComplex adunare(NumarComplex other) {
        return new NumarComplex(this.re + other.re, this.im + other.im);
    }

    //Metoda pentru scadere
    public NumarComplex scadere(NumarComplex other) {
        return new NumarComplex(this.re - other.re, this.im - other.im);
    }

    //Metoda pentru inmultire
    public NumarComplex inmultire(NumarComplex other) {
        double newRe = this.re * other.re - this.im * other.im;
        double newIm = this.re * other.im + this.im * other.re;
        return new NumarComplex(newRe, newIm);
    }

    //Metoda pentru impartire
    public NumarComplex impartire(NumarComplex other) {
        double k = other.re * other.re + other.im * other.im;
        double newRe = (this.re * other.re + this.im * other.im) / k;
        double newIm = (this.re * other.im - this.im * other.re) / k;
        return new NumarComplex(newRe, newIm);
    }

    //Metoda pentru conjugat
    public NumarComplex conjugat(NumarComplex other) {
        return new NumarComplex(other.re, -other.im);
    }

    public double getRe() {
        return re;
    }

    public void setRe(double re) {
        this.re = re;
    }

    public double getIm() {
        return im;
    }

    public void setIm(double im) {
        this.im = im;
    }

    @Override
    public String toString() {
        return  re + " + " + im + "i";
    }
}
