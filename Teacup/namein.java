import java.util.Scanner;

public class namein {

    public static void main(String [] args){
            // Get user input
            Scanner name = new Scanner(System.in);
            System.out.print("Enter Your Name: ");

            //print user input
            System.out.println("Hello " + name.nextLine());

            //close
            name.close();
        }
}
/*
 * https://www.w3schools.com/java/java_user_input.asp
 */