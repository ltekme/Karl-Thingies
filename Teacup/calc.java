
import java.util.Scanner;

public class calc {
    public static void main(String [] args) {
        // Get func
        if (args.length == 0) {
            System.out.println("Please Provide A Methoad As Follows \n -p Plus \n -m Minus \n -d Divide");
            
       } else {
        
            Scanner scn = new Scanner(System.in);
            System.out.print("Enter The First Number: ");
            int n1 = scn.nextInt();
            System.out.print("Enter The First Number: ");
            int n2 = scn.nextInt();
            scn.close();
            
            if (args[0].equals("-p")) {
                System.out.println("Number 1 Plus Number 2 is "+ (n1+n2));

            } else if (args[0].equals("-m")) {
                System.out.println("Number 1 Minus Number 2 is "+ (n1-n2));

            } else if (args[0].equals("-d")) {
                System.out.println("Number 1 divided by Number 2 is "+ (n1/n2));
            };
        };
    }; 
}

/*
 * https://www.w3schools.com/java/java_conditions.asp
 * 
 */