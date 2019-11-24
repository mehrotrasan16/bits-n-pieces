Problem: https://www.hackerrank.com/challenges/java-static-initializer-block/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static Scanner input = new Scanner(System.in);
    public static int B = input.nextInt(); 
    public static int H = input.nextInt();
    public static boolean flag = true;

    static{
        if((B < 0) || (H < 0)){
            System.out.print("java.lang.Exception: Breadth and height must be positive");
            System.exit(0);
        }
    }

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class

