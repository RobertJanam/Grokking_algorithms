import java.util.Arrays;

public class BinarySearchRecursive{
    public static int binary_search_recursive(int[] arr, int item, int left, int right){

        // Base case
        if (left > right){
            return -1;
        }

        int mid = left + (right - left) / 2;

        int guess = arr[mid];

        if (guess == item){
            return mid;
        }

        else if(item > guess){
            return binary_search_recursive(arr, item, mid + 1, right);
        }

        else {
            return binary_search_recursive(arr, item, left, mid - 1);
        }

    }

    public static void main(String[] args) {
        int array [] = {6, 4, 7, 2, 8, 1, 3};
        Arrays.sort(array);
        int left = 0;
        int right = array.length - 1;
        System.out.println(binary_search_recursive(array, 3, left, right));
        System.out.println(binary_search_recursive(array, 10, left, right));
    }
}
