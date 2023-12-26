import java.util.Scanner;
public class LDLC {
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);

        System.out.print("Enter TC: ");
        float tc = ent.nextFloat();
        System.out.print("Enter HDLC: ");
        float hdlc = ent.nextFloat();
        System.out.print("Enter TG: ");
        float tg = ent.nextFloat();
        ent.close();

        float ldlc = tc - hdlc - (tg / 5);

        System.out.println("LDLC = " + ldlc);

    }
}
