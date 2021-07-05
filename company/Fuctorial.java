package com.company;

import java.math.BigInteger;

public class Fuctorial {
    public void Fuctorial(int n) {
        //Since int does not contain a large number of digits was used class BigInteger
        BigInteger result = new BigInteger(String.valueOf(1));
        BigInteger result_Sum = new BigInteger(String.valueOf(0));
        for (int i = 1; i <= n; i++) {
            //Found fucktorial
            result = result.multiply(BigInteger.valueOf(i));
        }
        System.out.println("Result: " + result);
        //Using a loop, we recalculate the sum of all elements of the calculated factorial
        while (result.compareTo(BigInteger.ZERO) > 0) {
            result_Sum = result_Sum.add(result.remainder(BigInteger.valueOf(10)));
            result = result.divide(BigInteger.valueOf(10));
        }
        System.out.println("Result Sum " + result_Sum);
    }
}
