package selection_sort;

import java.util.Arrays;

public class SelectionSort {
    public static int[] selection_sort_pro(int[] arr){
    int n = arr.length;
    int min_idx;
    // loop through arr[i]
    for (int i = 0; i < n; i++){
        // initialize minimum index
        min_idx = i;
        //loop through arr[j]
        for (int j = i + 1; j < n; j++){
            // if current arr element arr[j] < the current arr element arr[i]:
            if(arr[j] < arr[min_idx]){
                // minimum index = j
                min_idx = j;
            }
        }
        // swap
        arr[i] = (arr[i] + arr[min_idx]) - (arr[min_idx] = arr[i]);
        //int temp = arr[i];
        //arr[i] = arr[min_idx];
        //arr[min_idx] = temp;

    }
    return arr;

}
    public static void main(String[] args) {
        int[] array = {7, 4, 8, 2, 1, 5};

        selection_sort_pro(array);
        System.out.println(Arrays.toString(array));

        /*
        selection_sort_pro(array);

        for(int i = 0; i < array.length; i++){
            System.out.print(array[i] + " ");
        } */

    }
}
