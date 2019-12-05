import java.math.BigDecimal;
import java.util.*;
class Solution{

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
      	sc.close();
         //declare array of bigdecimals
         BigDecimal[] bd = new BigDecimal[n];
         String[] arr = new String[n];
         Integer[] iarr = new Integer[n];
         Float[] farr = new Float[n];

        //read string array into big decimal array
        for(int i = 0; i < n; i ++){
            bd[i] = new BigDecimal(s[i]);
        }
        
        //sort bigecimal array ascending
        for(int i = 0; i < n; i ++){
            
            int min_index = i;
            
            for(int j = i+1; j < n; j++){
                if(bd[j].compareTo(bd[min_index]) < 0){
                    min_index= j;
                }
            }

            BigDecimal temp = bd[min_index]; 
            bd[min_index] = bd[i]; 
            bd[i] = temp; 
        }

        //sort bigecimal array descending
        for(int i = 0; i < n; i ++){
            
            int max_index = i;
            
            for(int j = i+1; j < n; j++){
                if(bd[j].compareTo(bd[max_index]) > 0){
                    max_index= j;
                }
            }

            BigDecimal temp = bd[max_index]; 
            bd[max_index] = bd[i]; 
            bd[i] = temp; 
        }


        // //print sorted array
        // for(int i = 0; i < n; i ++){
        //     System.out.println(bd[i]);
        // }

        //convert into string
        for(int i = 0; i < n;  i++){
                s[i] = bd[i].toString();
        }

        
        


       
        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }

}
