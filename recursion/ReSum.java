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

// or if you don't use static for the method you created, do this instead. Otherwise you'll end up with this error:
// Cannot make a static reference to the non-static method sum(int[]) from the type ReSum

/*
import java.util.Arrays;

public class ReSum {
    public int sum(int[] arr){
        if (arr.length == 0){
            return 0;
        }

        return arr[0] + sum(Arrays.copyOfRange(arr, 1, arr.length));
    }

    public static void main(String[] args){
        int[] arr = {2, 4, 5, 7};

        ReSum newArr = new ReSum();
        System.out.print("Sum: " + newArr.sum(arr));
    }
}
*/
