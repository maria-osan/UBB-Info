public class TaskContainerFactory implements Factory{
    private static final TaskContainerFactory instance = new TaskContainerFactory();
    private TaskContainerFactory() {}
    public static TaskContainerFactory getInstance() {
        return instance;
    }

    @Override
    public Container createContainer(Strategy startegy) {
        return switch (startegy) {
            case LIFO -> new StackContainer();
            case FIFO -> new QueueContainer();
        };
    }
}
