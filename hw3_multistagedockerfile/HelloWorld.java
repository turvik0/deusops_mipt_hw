public class HelloWorld {
    public static void main(String[] args) {
        String myCoolEnv = System.getenv("MYCOOOLENV");
        if (myCoolEnv != null) {
            System.out.println("Hello, World! Here i am in a container horaaay!" + myCoolEnv);
        }
        else {
            System.out.println("With whom am I speaking? (Environment variable not set)");
        }
    }
}