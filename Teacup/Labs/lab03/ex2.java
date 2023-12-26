public class ex2 {
    public static void main(String[] args) {
        double a;
        a = 20;
        System.out.println(a-8);
        //(a) 12.0

        int n=9; n+=1; 
        System.out.println(n); 
        System.out.println(n+1);
        //(b) 10
        // 11

        int num=7;
        num = 9%num;
        System.out.println(num);
        //(c) 2

        int u, v;
        u = 5;
        v = u * u;
        System.out.println(u*v);
        //(d) 125

        double x = 8;
        x+=5;
        System.out.println(x+3*x);
        //(e) 52.0

        // float p = (float) 5.1, q = (float) 2.3;
        double p=5.1, q=2.3;
        p += p; 
        System.out.println(p + q);
        System.out.println(p - q);
        //(f) 12.5
        // 7.8999999999999995
    }
}

// https://stackoverflow.com/questions/6319727/what-exactly-does-double-mean-in-java
// https://www.w3schools.com/java/ref_keyword_char.asp
// https://stackoverflow.com/questions/43975824/what-is-the-percent-operator-in-java