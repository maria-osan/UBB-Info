import java.util.Arrays;

public class SortingTask extends Task{
    public int[] numbers;
    BubbleSort bubbleSort;
    QuickSort quickSort;

    private static abstract class AbstractSorter {
        public abstract int[] sort(int[] arr);
    }

    private static class BubbleSort extends AbstractSorter {

        public int[] sort(int[] arr) {
            int n = arr.length;
            boolean swapped;

            do {
                swapped = false;
                for (int i = 1; i < n; i++) {
                    if(arr[i - 1] > arr[i]) {
                        int aux = arr[i - 1];
                        arr[i - 1] = arr[i];
                        arr[i] = aux;
                        swapped = true;
                    }
                }

            } while (swapped);
            return arr;
        }
    }

    private static class QuickSort extends AbstractSorter {
        public int[] sort(int[] arr) {
            quickSort(arr, 0 , arr.length - 1);
            return arr;
        }

        private void quickSort(int[] arr, int low, int high) {
            if(low < high) {
                int pivotIndex = partition(arr, low, high);
                quickSort(arr, low, pivotIndex - 1);
                quickSort(arr, pivotIndex + 1, high);
            }
        }

        private int partition(int[] arr, int low, int high) {
            int pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++) {
                if(arr[j] < pivot) {
                    i++;
                    int aux = arr[i];
                    arr[i] = arr[j];
                    arr[j] = aux;
                }
            }
            int aux = arr[i + 1];
            arr[i + 1 ] = arr[high];
            arr[high] = aux;
            return i + 1;
        }
    }

    public SortingTask(int[] numbers, boolean fastSort) {
        this.bubbleSort = new BubbleSort();
        this.quickSort = new QuickSort();
        if(!fastSort) {
            this.numbers = this.bubbleSort.sort(numbers.clone());
        } else {
            this.numbers = this.quickSort.sort(numbers.clone());
        }
    }

    @Override
    public void execute() {
        for(int i: this.numbers)
            System.out.println(i + " ");
    }
}
