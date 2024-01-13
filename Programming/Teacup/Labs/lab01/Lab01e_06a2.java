import java.util.Scanner;
public class Lab01e_06a2 {
    public static void main(String[] args) {
        // get base
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the base of the triangle: ");
        int l = s.nextInt();
        s.close();
        //draw
        int b = l*2;
        for (int i=1; i<=b*2; i+=2){
            int e = (b*2-i)/2;
            System.out.print(" ".repeat(e)); //add space
            System.out.print("*".repeat(i)); //add tree
            System.out.println(); // add line
        }
    }
}
