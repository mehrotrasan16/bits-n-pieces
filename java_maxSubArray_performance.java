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

    public int maxSubArray(int[] nums) {
        if(nums.length == 1){
            return nums[0];
        }
        else{
            return maxSubArray(Arrays.copyOfRange(nums, 0, nums.length/2)) + maxSubArray(Arrays.copyOfRange(nums, nums.length/2+1,nums.length));
        }
        
    }

    private static Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
       
    }
}