public class helloarg {

    public static void main(String [] args) {
        String name;
        if (args.length == 0) {
            name = "None";
        } else {
            name = args[0];
        };
        System.out.println("Hello " + name);
    }
}

/*
 * https://www.w3schools.com/java/java_strings.asp
 */