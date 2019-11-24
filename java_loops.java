//Problem at https://www.hackerrank.com/challenges/java-loops/problem
import java.util.*;
import java.io.*;

class Solution{


    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            //n terms
            //current term, power term, a and b stay constant
            int term = 0;
            for(int j = 0; j < n; j++){ // for n terms
                    term = 0;
                    for(int k = 0; k <= j; k++){
                        //System.out.printf("term: %d\n",term);
                        term += ((int)java.lang.Math.pow(2,k) * b);
                        //System.out.printf("2^%d ,b = %d, term = %d \n",k,b,term);
                    }
                System.out.print( String.valueOf(a + term) + " ");     
            }
            System.out.println();
            //calculate the nth term as 

            
        }
        in.close();
    }
}

