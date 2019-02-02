import java.util.Scanner;

public class PSum extends Thread {

    private int[] array;

    private int low, high, partial;

    public PSum(int[] array, int low, int high){
        this.array = array;
        this.low = low;
        this.high = high;
    }

    private int sum(int[] array, int low, int high){
        int total = 0;
        for(int i = low; i <high; i++) total+= array[i];
        return total;
    }

    public int getPartialSum(){
        return partial;
    }

    public void run(){
        partial = sum(array, low, high);
    }

    public static void ParallelSum(int array[], int n, int p){
        for(int i = n; i > 0; i--){
//            int start = 0;
            PSum[] sums = new PSum[(int) Math.pow(p,i-1)];
            for(int j = 0; j < Math.pow(p,i-1); j++){
                sums[j] = new PSum(array, j*p, j*p+p);
                sums[j].start();
            }

            try {
                for (PSum sum : sums) {
                    sum.join();
                }
            }

            catch (InterruptedException e) {
                e.printStackTrace();
            }

            for (int j = 0; j < Math.pow(p,i-1); j++ ){
                array[j] = sums[j].getPartialSum();
            }



        }

        System.out.println(Integer.toString(array[0]));
    }

    public static void main(String args[]){

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int p = scanner.nextInt();
        int[] NumArray = new int[(int) Math.pow(p,n)];
        for (int i = 0; i < Math.pow(p,n); i++) NumArray[i] = scanner.nextInt();
        scanner.close();

        ParallelSum(NumArray,n,p);






    }





}
