import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        /*
         * Write your code here.
         * 07:05:45PM
         * 07 - h
         * 45PM - ap_pm

         */
        Integer h = new Integer(s.split(":")[0]);
        String am_pm = s.split(":")[2].substring(1,3);

        if(am_pm == "AM"){
            return s.substring(0,s.indexOf("A"));
        }
        else{
            h += 12;
            String min = new String(s.split(":")[1]);
            String sec = new String(s.split(":")[2].substring(0,2));
            return new String(h+":"+min+":"+sec);
        }
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
