public class AdditionExpression extends ComplexExpression{
    public AdditionExpression(NumarComplex[] args) {
        super(Operation.ADDITION, args);
    }

    @Override
    public NumarComplex execute() {
        NumarComplex rez = args[0];

        for (int i = 1; i < args.length; i++) {
            rez = executeOneOperation(rez, args[i]);
        }
        return rez;
    }

    @Override
    public NumarComplex executeOneOperation(NumarComplex a, NumarComplex b) {
        return a.adunare(b);
    }
}
