public class MultiplicationExpression extends ComplexExpression{
    public MultiplicationExpression(NumarComplex[] args) {
        super(Operation.MULTIPLICATION, args);
    }

    @Override
    public NumarComplex execute() {
        NumarComplex rez = args[0];

        for (int i = 1; i < args.length; i++) {
            rez = executeOneOperation(rez, args[i]);
        }
        return  rez;
    }

    @Override
    public NumarComplex executeOneOperation(NumarComplex a, NumarComplex b) {
        return a.inmultire(b);
    }
}
