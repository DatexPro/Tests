package com.company;

public class Ex_1 {
    private int n;
    private int[] Array_Brackets = new int[n + 1];
    //Ex 1
    //To solve this task, the Catalan method was used,
    //which was implemented in Catalan method.
    //Catalan accepts one integer value parameter
    public void Catalan(int n) {
        //First - create an empty array
        Array_Brackets = new int[n + 1];
        //Second - set the zero element to 1
        Array_Brackets[0] = 1;
        //Third - create loop for calculating an Array_Bracket[m] for m=1...n
        for (int m = 1; m <= n; m++) {
            //Fourth - set each element of the array 0
            Array_Brackets[m] = 0;
            for (int k = 0; k < m; k++) {
                Array_Brackets[m] += Array_Brackets[k] * Array_Brackets[m - 1 - k];
            }
        }
        //Print result method
        System.out.println("Number of correct parentheses: " + Array_Brackets[n]);
    }
}
