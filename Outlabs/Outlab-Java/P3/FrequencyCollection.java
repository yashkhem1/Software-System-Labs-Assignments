

import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.nio.file.*;
public class FrequencyCollection {
        public static String readFileAsString(String fileName)
    {
        try{
        String data = new String(Files.readAllBytes(Paths.get(fileName)));
        return data;}
        catch(Exception e){
            return(e.toString());}
    }
    public static void insertIntoArray(String token, ArrayList<String> arr, ArrayList<Integer> freq){
        String[] stop = new String[]{ "and", "the", "is", "in", "at", "of", "his", "her", "him" };
        if(Arrays.asList(stop).contains(token)) {
            int a=1;
        }
        else {
            if (arr.indexOf(token) != -1) {
                int i = arr.indexOf(token);
                freq.set(i,freq.get(i)+1);
            } else{
                int i = 0;
                for (; i < arr.size(); i++) {
                    if (arr.get(i).compareTo(token) >= 0) {
                        break;
                    }
                }
                arr.add(i, token);
                freq.add(i, 1);
            }
        }
    }
    public static void main(String[] args){
        String data=readFileAsString(args[0]);
//
//        java.lang.String data="here I am Wondering who I am the is inside this her him hEre wondering the is at who please please please help and my AND his friend";
        data=data.toLowerCase();
        StringTokenizer arr=new StringTokenizer(data);
        ArrayList<String> s=new ArrayList<String>();
        ArrayList<Integer> freq=new ArrayList<Integer>();
        for(;arr.hasMoreTokens();){
            insertIntoArray(arr.nextToken(),s,freq);
        }
        for(int i=0;i<s.size();i++){
            String printer=s.get(i)+','+Integer.toString(freq.get(i));
            System.out.println(printer);
        }
    }

}
