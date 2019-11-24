//Problem: https://www.hackerrank.com/challenges/java-date-and-time/problem
//this makes no sense.
//month is zero indexed?
//this took me 1 hour to understand.
//not in the docs, you oracle soabs

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.lang.*;
class Result {

    /*
     * Complete the 'findDay' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER month
     *  2. INTEGER day
     *  3. INTEGER year
     */

    public static String findDay(int month, int day, int year) {
        Calendar c = Calendar.getInstance();
        System.out.println(month +" "+ day + " "+ year);
        String day1 = new String();
        c.set(c.MONTH,month);
        System.out.println(c.get(c.MONTH) == c.AUGUST);
        //c.set(c.DAY_OF_MONTH,day);
        //c.set(c.YEAR,year);

        c.set(year,month-1,day);

        System.out.println(c.getTime());

        switch(c.get(c.DAY_OF_WEEK)){
            case (Calendar.SUNDAY):
                day1 = "SUNDAY";
                break;
            
            case (Calendar.MONDAY):
                day1 = "MONDAY";
                break;
            
            case (Calendar.TUESDAY):
                day1 = "TUESDAY";
                break;

            case (Calendar.WEDNESDAY):
                day1 = "WEDNESDAY";
                break;

            case (Calendar.THURSDAY):
                day1 = "THURSDAY";
                break;

            case (Calendar.FRIDAY):
                day1 = "FRIDAY";
                break;

            case (Calendar.SATURDAY):
                day1 = "SATURDAY";
                break;

            default :
                day1 = "LODA";
        }
        return day1;
    }
}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bufferedWriter = new BufferedWriter(new StreamWriter(System.out));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int month = Integer.parseInt(firstMultipleInput[0]);

        int day = Integer.parseInt(firstMultipleInput[1]);

        int year = Integer.parseInt(firstMultipleInput[2]);

        String res = Result.findDay(month, day, year);
        System.out.println(res);

        // bufferedWriter.write(res);
        // bufferedWriter.newLine();

        bufferedReader.close();
//        bufferedWriter.close();
    }
}

