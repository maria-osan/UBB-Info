import java.time.LocalDateTime;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        MessageTask task1 = new MessageTask("1", "description1", "message1", "abc", "xyz", LocalDateTime.now());
        MessageTask task2 = new MessageTask("2", "description2", "message2", "def", "abc", LocalDateTime.now());
        MessageTask task3 = new MessageTask("3", "description3", "message3", "xyz", "mno", LocalDateTime.now());
        MessageTask task4 = new MessageTask("4", "description4", "message4", "yyy", "bcb", LocalDateTime.now());
        MessageTask task5 = new MessageTask("5", "description5", "message5", "rty", "zyx", LocalDateTime.now());

        MessageTask[] task = new MessageTask[]{task1, task2, task3, task4, task5};

        for(MessageTask t : task) {
            System.out.println(t);
        }

        StrategyTaskRunner runner = new StrategyTaskRunner(Strategy.valueOf(args[0]));
        for (MessageTask messageTask : task) {
            runner.addTask(messageTask);
        }
        runner.executeAll();

        System.out.println("\nDelay: ");
        TaskRunner delayRunner = new DelayTaskRunner(new StrategyTaskRunner(Strategy.valueOf(args[0])));
        for (MessageTask messageTask : task) {
            delayRunner.addTask(messageTask);
        }
        delayRunner.executeAll();

        System.out.println("\nPrinter: ");
        TaskRunner printerRunner = new PrinterTaskRunner(new StrategyTaskRunner(Strategy.valueOf(args[0])));
        for (MessageTask messageTask : task) {
            printerRunner.addTask(messageTask);
        }
        printerRunner.executeAll();

        System.out.println("\n\n");

        TaskRunner delayPrinter = new DelayTaskRunner(new PrinterTaskRunner(new StrategyTaskRunner(Strategy.valueOf(args[0]))));
        for (MessageTask messageTask : task) {
            delayPrinter.addTask(messageTask);
        }
        //delayPrinter.executeAll();

        SortingTaskTest.sortTest();

        Container q = new QueueContainer();
        System.out.println(q.size());
        q.add(task1);
        q.add(task2);
        System.out.println(q.remove() == task1);
        System.out.println(q.size());
        System.out.println(q.remove() == task2);
    }

    private static class SortingTaskTest extends SortingTask {
        public SortingTaskTest(int[] numbers, boolean fastSort) {
            super(numbers, fastSort);
        }
        private static void sortTest() {
            int[] list = {7, 5, 3, 2, 6, 1, 4, 8};
            int[] sorted = {1, 2, 3, 4, 5, 6, 7, 8};

            SortingTask l1 = new SortingTask(list, true);
            SortingTask l2 = new SortingTask(list, false);

            assert (Arrays.equals(l1.numbers, sorted));
            assert (Arrays.equals(l1.numbers, l2.numbers));
        }
    }
}