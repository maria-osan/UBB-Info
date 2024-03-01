import java.util.ArrayList;
import java.util.List;

public class StackContainer extends AbstractContainer{
    @Override
    protected int getRemoveIndex() {
        return tasks.size() - 1;
    }

    /*List<Task> tasks = new ArrayList<>();

    @Override
    public Task remove() {
        if(!tasks.isEmpty()) {
            return tasks.remove(tasks.size() - 1);
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
