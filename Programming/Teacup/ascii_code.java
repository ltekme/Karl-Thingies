public class ascii_code {
    public static void main(String[] args) {
        String a = "AaBbCcDd";
        char[] b = a.toCharArray();
        for (char i:b) {
            int c = (int)i;
            System.out.println(c);
        }
    }
}
