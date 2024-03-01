import java.util.Arrays;

public class ExpressionParser {
    public ExpressionFactory expressionFactory;

    public ExpressionParser() {
        this.expressionFactory = ExpressionFactory.getInstance();
    }

    public ComplexExpression parser(String[] args) {
        if (args.length % 2 == 0 || args.length < 3)
            throw new IllegalArgumentException("Expresie invalida!");

        NumarComplex[] complexNumbers = new NumarComplex[args.length / 2 + 1];
        Operation currentOperation = null;

        int nrIndex = 0;

        for (int i = 0; i < args.length; i++) {
            if(i % 2 == 0) {
                //este numar complex
                complexNumbers[nrIndex++] = parseNumarComplex(args[i]);
            } else {
                //este  operator
                currentOperation = parseOperation(args[i]);
            }
        }

        return buildExpression(complexNumbers, currentOperation);
    }

    private ComplexExpression buildExpression(NumarComplex[] complexNumbers, Operation operation) {
        ComplexExpression expression = expressionFactory.createExpression(operation, new NumarComplex[]{complexNumbers[0], complexNumbers[1]});

        for (int i = 1; i < complexNumbers.length - 1; i++) {
            expression = expressionFactory.createExpression(operation, new NumarComplex[]{expression.execute(), complexNumbers[i + 1]});
        }
        return expression;
    }

    private static NumarComplex parseNumarComplex(String input) {
        if(!isComplexNumber(input))
            throw new IllegalArgumentException("Numarul complex: " + input + " nu este valid.");

        String[] parts = input.split("[+\\-]");

        //Daca numarul incepe cu * sau - eliminam spatiul obtinut la splitting
        if(parts[0].isEmpty()) {
            parts = Arrays.copyOfRange(parts, 1, parts.length);
        }

        double re, im;
        //Partea reala
        if (input.charAt(0) == '-') {
            re = -Double.parseDouble(parts[0]);
        } else {
            re = Double.parseDouble(parts[0]);
        }

        //Partea imaginara
        if(input.charAt(input.length() - parts[1].length() - 1) == '-') {
            im = -Double.parseDouble(parts[1].replace("i", ""));
        } else {
            im  = Double.parseDouble(parts[1].replace("i", ""));
        }

        return new NumarComplex(re, im);
    }

    private static Operation parseOperation(String input) {
        return switch (input) {
            case "+" -> Operation.ADDITION;
            case "-" -> Operation.SUBSTRACTION;
            case "*" -> Operation.MULTIPLICATION;
            case "/" -> Operation.DIVISION;
            default -> throw new IllegalStateException("Operatie nerecunoscuta: " + input);
        };
    }

    private static boolean isComplexNumber(String str) {
        return str.matches("(-?\\d+(\\.\\d+)?)\\s*([+-])\\s*(-?\\d+(\\.\\d+)?)i");
    }
}
