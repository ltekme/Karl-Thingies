import java.util.Scanner;

public class ValidateHKID {
    public static void main(String[] args) {

/*
   Filename:    ValidateHKID.java
   Programmer:	Karl
   Description:	Determine the check digit of HKID numbers.
*/

        Scanner kb = new Scanner(System.in);
        System.out.print("? ");
        String hkid = kb.next();
        kb.close();
        char[] letter;
        int sum;
        int code;

        letter = hkid.toCharArray();
        letter[0] = Character.toUpperCase(letter[0]);

        sum = ( (int)letter[0] -64 )*8;
        sum = sum + ( (int)letter[1] - 48 )*7;
        sum = sum + ( (int)letter[2] - 48 )*6;
        sum = sum + ( (int)letter[3] - 48 )*5;
        sum = sum + ( (int)letter[4] - 48 )*4;
        sum = sum + ( (int)letter[5] - 48 )*3;
        sum = sum + ( (int)letter[6] - 48 )*2;
        code = 11 - (sum % 11);

        System.out.print("The HKID is: " + letter[0] + hkid.substring(1,7));
        if (code == 11) {
            System.out.println("(0)");
        } else if(code == 10) {
            System.out.println("(A)");
        } else { 
            System.out.println("(" + code + ")"); 
        }
    }
}
