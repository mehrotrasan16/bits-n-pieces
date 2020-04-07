/* Problem Statement: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/

import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

class java_singleNumber{

    public static int singleNumber(int[] nums) {
        int size = nums.length;
        int result = 0;
        for(int i = 0; i < size; i++){
            result = result ^ nums[i];
        }
        return result;
    }

    private static final Scanner scan = new Scanner(System.in);
    public static void main(String[] args) {
        // int x1 = scan.nextInt();
        // int x2 = scan.nextInt();
        // System.out.println(x1^x2);
        int size = 5;
        int[] array = new int[size];
        int xor = 0;
        for( int i =0; i < size; i ++){
            array[i] = scan.nextInt();
        }
        for(int i = 0; i < size; i++){
            xor = xor ^ array[i];
        }
        System.out.println("XOR result:" + xor);
        
        System.out.println("CALLing your function:");

        System.out.println("Function singleNumber result:" + singleNumber(array));

    }
}