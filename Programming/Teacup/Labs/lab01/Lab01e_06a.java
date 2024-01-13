public class Lab01e_06a {
    public static void main(String[] args) {
        /* nice */
        int l = 50;
        int b = l*2;
        for (int i=1; i<=b; i+=2){
            int e = (b-i)/2;
            System.out.print(" ".repeat(e)); //add space
            System.out.print("*".repeat(i)); //add tree
            System.out.println(); // add line
        }
    }
}
