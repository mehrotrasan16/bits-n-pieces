import java.util.Scanner;

/* Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1 */

class java_happyNumber{
    public static int square_sum_of_digits(int[] digits){
        int sum = 0;
        for (int i : digits) {
            sum += i*i;
        }
        return sum;
    }

    public static int[] get_digits(int input){
        int temp = input;
        int[] digits = new int[5];
        int i = 0;

        while(temp > 0){
            //System.out.println(temp%10);
            digits[i++] = temp%10;
           // System.out.println("Beofre" + temp);
            temp /= 10;
           // System.out.println("After" + temp);
        }

        /* for (int num : digits) {
            System.out.println(num);    
        } */
        
        return digits;
    }

    public static boolean happyNumber(int input){
        int[] digits = get_digits(input);
        int sum = square_sum_of_digits(digits);
        int loop_counter = 0;

        while(sum != 1){
            if(loop_counter == 100){
                return false;
            }
            digits = get_digits(sum);
            sum = square_sum_of_digits(digits);
            loop_counter++;
        }
        
        return true;

    }
    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Input: ");

        int input = scan.nextInt();
        if(input > 99999){
            System.out.println("Please enter number less than 100000");
            System.exit(0);
        }

        if(happyNumber(input)){
            //System.out.println(input + " is a happy number");
            System.out.println("true");
        }
        else{
            //System.out.println(input + " is a not a happy number");
            System.out.println("false");
        }

               
    }
}