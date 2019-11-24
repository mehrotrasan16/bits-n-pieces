// Problem: https://www.hackerrank.com/challenges/java-datatypes/problem

import java.util.*;
import java.io.*;
import java.lang.Math.*;


class Solution{
    public static void main(String []argh)
    {



        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127)System.out.println("* byte");
                if(x >= (-1 * java.lang.Math.pow(2,16)) && x <= (java.lang.Math.pow(2,16)))System.out.println("* short");
                if(x >= (-1 * java.lang.Math.pow(2,32)) && x <= (java.lang.Math.pow(2,32)))System.out.println("* int");
                if(x >= (-1 * java.lang.Math.pow(2,64)) && x <= (java.lang.Math.pow(2,64)))System.out.println("* long");
                
                //Complete the code
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}



