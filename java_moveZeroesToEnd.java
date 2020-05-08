/**
 *   Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
   Hide Hint #1  
In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
   Hide Hint #2  
A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.
 */

 /**
  * This class works, but uses a temp array, which is not cool
  */
class java_moveZeroesToEnd {
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
    
    public void moveZeroes(int[] nums) {
        int[] temp = new int[nums.length];
        int j = 0;
        int zerocounter = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                temp[j++] = nums[i]; 
            }
            else
                zerocounter++;
        }
        while(zerocounter >0){
            temp[j++] = 0;
            zerocounter--;
        }
        print_array(temp,0,temp.length);
    }

}
/** 
 * This class works, but does not handle the case in which there are contiguous 0s e.g. 0,0,1
*/
class java_moveZeroesToEnd_single_array {
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
   
   public void moveZeroes(int[] nums) {
       int j = 0;
       for(int i = 0; i < nums.length; i++){
           if(nums[i] == 0){
               for(j = i+1 ; j < nums.length; j++){
                   nums[j - 1] = nums[j];
                   //print_array(nums, i,nums.length);
               }
               nums[nums.length-1] = 0;
           }
           print_array(nums, 0,nums.length);
       }
   }
}

/** 
 * This class works, but needs to be optimized
*/
class java_moveZeroesToEnd_single_array_bordercondition {
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
   
   public int checkZeroes(int[] nums,int i){
       int zerocounter = 0;
       while(i < nums.length && nums[i++] == 0){
           zerocounter++;
       }
       return zerocounter;
   }
   
   public void moveZeroes(int[] nums) {
       int j = 0;
       int zerocounter = 0;
        for(int i = 0; i < nums.length; i++){
           print_array(nums, 0,nums.length);
          if(nums[i] == 0){
              zerocounter = checkZeroes(nums,i);
              while(zerocounter > 0){
                  for(j = i+1 ; j < nums.length; j++){
                      nums[j - 1] = nums[j];
                  }
              nums[nums.length-1] = 0;
                  zerocounter--;
              }
              
          }
          print_array(nums, 0,nums.length);
      }


   }
}