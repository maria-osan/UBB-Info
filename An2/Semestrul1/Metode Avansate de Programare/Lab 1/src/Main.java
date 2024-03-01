public class Main {
    public static void main(String[] args) {
        if(args.length < 2){
            System.out.println("Utilizare: numar1 operator numar2...");
        }

        try{
            ExpressionParser expressionParser = new ExpressionParser();
            ComplexExpression expression = expressionParser.parser(args);
            NumarComplex rez = expression.execute();

            System.out.println("Rezultat: " + rez.toString());
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}