package com.company;

import java.util.Scanner;
//Find the sum of the digits
//in the number 100! (i.e. 100 factorial)
public class Main {
    public static void main(String[] args) {
	// write your code here

        Scanner input = new Scanner(System.in);
        Fuctorial ex_3 = new Fuctorial();
        System.out.print("Input your number: ");
        int fuck = input.nextInt();
        ex_3.Fuctorial(fuck);
    }
}
