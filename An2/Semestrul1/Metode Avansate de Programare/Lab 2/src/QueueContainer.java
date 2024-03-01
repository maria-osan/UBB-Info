import java.util.ArrayList;
import java.util.List;

public class QueueContainer extends AbstractContainer{
    @Override
    protected int getRemoveIndex() {
        return 0;
    }

    /*List<Task> tasks = new ArrayList<>();

    @Override
    public Task remove() {
        if(!isEmpty()) {
            return  tasks.remove(0);
        } else {
            return null;
        }
    }

    @Override
    public void add(Task task) {
        tasks.add(task);
    }

    @Override
    public int size() {
        return tasks.size();
    }

    @Override
    public boolean isEmpty() {
        return tasks.isEmpty();
    }*/
}
