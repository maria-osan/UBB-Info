public class StrategyTaskRunner implements TaskRunner{
    private final Container container;

    public StrategyTaskRunner(Strategy strategy) {
        TaskContainerFactory taskContainerFactory = TaskContainerFactory.getInstance();
        container = taskContainerFactory.createContainer(strategy);
    }

    @Override
    public void executeOneTask() {
        Task task = container.remove();
        task.execute();
    }

    @Override
    public void executeAll() {
        while (hasTask())
            executeOneTask();
    }

    @Override
    public void addTask(Task t) {
        container.add(t);
    }

    @Override
    public boolean hasTask() {
        return !container.isEmpty();
    }
}
