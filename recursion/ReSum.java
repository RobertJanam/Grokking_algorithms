package recursion;

import java.util.Arrays;

public class ReSum {
    public static int sum(int[] arr){
        if (arr.length == 0){
            return 0;
        }

        return arr[0] + sum(Arrays.copyOfRange(arr, 1, arr.length));
    }

    public static void main(String[] args){
        int[] arr = {2, 4, 5, 7};

        System.out.print("Sum: " + sum(arr));
    }
}
