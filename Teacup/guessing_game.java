import java.util.Scanner;

public class guessing_game {
    public static void main(String [] args) {
        Scanner a = new Scanner(System.in);
        int i = 0;
        int t = 100;
        while (i < t) {
            int r = (int) (Math.random() * t) + 1;
            System.out.print("Guess the Number(1-100): ");
            int g = a.nextInt();
            if (r==g){
                System.out.println("You WIN");
                break;
            } else {
                System.out.println("Nope");
            }
            i++;
        }
        a.close();
    }
}

