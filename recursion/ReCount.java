import java.util.Arrays;

public class ReCount {
    public static int count(int[] arr){
        if (arr.length == 0){
            return 0;
        }

        return 1 + count(Arrays.copyOfRange(arr, 1, arr.length));
    }

    public static void main(String[] args){
        int[] arr = {2, 4, 5, 7};

        System.out.print("Count: " + count(arr));
    }
}
