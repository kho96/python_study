// Hello.java

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
        System.out.println(args.length);
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }

}