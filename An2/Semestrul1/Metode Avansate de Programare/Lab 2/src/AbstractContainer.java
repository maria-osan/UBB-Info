import java.util.ArrayList;
import java.util.List;

public abstract class AbstractContainer implements Container{
    protected List<Task> tasks = new ArrayList<>();

    protected abstract int getRemoveIndex();

    @Override
    public Task remove() {
        if(!isEmpty()) {
            return tasks.remove(getRemoveIndex());
        } else {
            return null;
        }
    }

    @Override
    public void add(Task t) {
        tasks.add(t);
    }

    @Override
    public int size() {
        return tasks.size();
    }

    @Override
    public boolean isEmpty() {
        return tasks.isEmpty();
    }
}
