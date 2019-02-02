public class ArgSum {
    public static void main(String args[]){
        int sum = 0;
        for(int i = 0; i < args.length; i++){
            int a = Integer.parseInt(args[i]);
            sum+=a;
        }

        System.out.println(Integer.toString(args.length)+","+Integer.toString(sum));
    }
}
