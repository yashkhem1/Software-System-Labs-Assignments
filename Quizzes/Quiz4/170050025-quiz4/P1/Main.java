import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Main <impl-option>");
            System.out.println("\tWhere <impl-option> == disk or net");
            System.exit(1);
        }
        FetchAndProcess fetchAndProcess = null;
        List<String> paths = new ArrayList<>();
        switch (args[0]) {
            case "disk":
                fetchAndProcess = new FetchAndProcessFromDisk();
                for (int i = 1; i < 50; i++) {
                    paths.add("data/gym" + String.valueOf(i));
                }
                break;
            case "net":
                fetchAndProcess = new FetchAndProcessFromNetwork();
                for (int i = 1; i < 50; i++) {
                    paths.add("https://www.cse.iitb.ac.in/~yashsriram/SSL/quiz4/gym" + String.valueOf(i) + ".php");
                }
                break;
            default:
                System.out.println("Unknown Option");
                System.exit(2);
        }
        fetchAndProcess.fetch(paths);
        String output = fetchAndProcess.process();
        System.out.println(output);
    }
}
