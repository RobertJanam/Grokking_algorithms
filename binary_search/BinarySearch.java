import java.util.Arrays;
 
public class BinarySearch{
    public static int binary_search_iterative(int[] arr, int item){
        int low = 0;
        int high = arr.length - 1; // length of the array gives the last index as the highest

        while(low <= high){ // as long as low and high don't overlap
            int mid = (low + high) / 2;
            if (arr[mid] == item){
                return mid; // if guess is correct
            }

            if (item > arr[mid]){
                low = mid + 1;
            }

            else{
                high = mid - 1;
            }
        }
        return -1;

    }

    public static void main(String args[]){
        int array [] = {3, 1, 5, 2, 6, 9};
        Arrays.sort(array); // sorts in ascending order
        System.out.println(binary_search_iterative(array, 5));
        System.out.print(binary_search_iterative(array, 10));
    }

}
