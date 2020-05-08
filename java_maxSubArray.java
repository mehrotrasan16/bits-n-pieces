/* Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

- Print all possible contiguous sub arrays in an array.
- sum their elements
- compare with max size 
Example:

Input: [-2,6,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 */
import java.util.Scanner;

class java_maxSubArray{
    private static final int ERROR = -999;

    public static int sum(int[] array, int startIndex, int endIndex){
        if(startIndex < 0 || endIndex > array.length){
            return ERROR;
        }
        int sum = 0;
        for(int i = startIndex;i < endIndex;i++){
            sum += array[i];
        }
        return sum;
    }

    public static void print_array(int[] array,int startIndex, int endIndex){
        if(startIndex < 0 || endIndex > array.length){
            startIndex = 0;
            endIndex = array.length;
        }
        System.out.print("[");
        for (int i = startIndex; i < endIndex; i++) {
            System.out.print(array[i] + ",");
        }
        System.out.print("]\n");
    }

    private static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        // int size = 7;
        //int[] array = new int[size];
        // for(int i =0; i < size; i++){
        //     array[i] = scan.nextInt();
        // }
        int[] array = new int[]{1};  
        print_array(array, 0, array.length);
        int windowSize = 1;
        int maxSum = array[0];
        int[] maxSumArray = new int[2];
        int currSum = 0;

        while(windowSize <= array.length){
            System.out.println("WindowSize: " + windowSize);
            for (int i = 0; i < array.length; i++) {
                print_array(array, i, i+windowSize);
                currSum = sum(array,i,i+windowSize);
                if(maxSum <= currSum){
                    maxSum =  currSum;
                    maxSumArray[0] = i;
                    maxSumArray[1] = i+windowSize;
                }
            }
            windowSize++;
        }

        System.out.println("MAX Sum:" + maxSum);
        System.out.println("MAX sum array:");
        print_array(array, maxSumArray[0], maxSumArray[1]);
    }
}