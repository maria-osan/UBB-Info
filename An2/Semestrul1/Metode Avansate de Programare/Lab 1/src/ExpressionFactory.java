public class ExpressionFactory {
    private static ExpressionFactory instance;

    private ExpressionFactory() {
        //Constructor privat pentru Singleton
    }

    public static ExpressionFactory getInstance() {
        if(instance == null)
            instance = new ExpressionFactory();

        return instance;
    }

    public ComplexExpression createExpression(Operation operation, NumarComplex[] args) {
        return switch (operation) {
            case ADDITION -> new AdditionExpression(args);
            case SUBSTRACTION -> new SubstractionExpression(args);
            case MULTIPLICATION -> new MultiplicationExpression(args);
            case DIVISION -> new DivisionExpression(args);
            default -> throw new IllegalArgumentException("Operatie nerecunoscuta: " + operation);
        };
    }
}
