import java.util.HashMap;
import java.util.Scanner;

public class Anagrams {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        String s1= in.nextLine();
        String s2=in.nextLine();//TO take care of CASE SENSITIVENESS
        s1=s1.toLowerCase();
        s2=s2.toLowerCase();
       // System.out.println(s1+" "+s2);
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i=0;i<s1.length();++i){
            if(hash.containsKey(s1.charAt(i))) {
                int a = hash.get(s1.charAt(i));
                hash.put(s1.charAt(i),++a);
                continue;
            }
            hash.put(s1.charAt(i),0);
        }
        HashMap<Character, Integer> hash2 = new HashMap<>();
        for (int i=0;i<s2.length();++i){
            if(hash2.containsKey(s2.charAt(i))) {
                int a = hash2.get(s2.charAt(i));
                hash2.put(s2.charAt(i),++a);
                continue;
            }
            hash2.put(s2.charAt(i),0);
        }
       for (Character key : hash.keySet()){
           Integer key2 = hash2.get(key);
           if((key2 == null) || (key2 != hash.get(key))) {
               System.out.println("Not Anagrams");
               System.exit(0);
           }
       }
       System.out.println("Anagrams");
    }
}

