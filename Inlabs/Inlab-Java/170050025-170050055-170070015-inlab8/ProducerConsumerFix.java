public class ProducerConsumerFix {
    public static int totalStock = 0;

    public static void main(String args[]){
        ProducerConsumerFix PC = new ProducerConsumerFix();
        FixDemo p = new FixDemo("producer", PC);
        FixDemo c = new FixDemo("consumer", PC);

        p.start();
        c.start();

        try {
            p.t.join();
            c.t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(Integer.toString(totalStock));



    }
}


class FixDemo implements Runnable{
    public Thread t;
    private String threadName;

    private ProducerConsumerFix PC;

    FixDemo(String name, ProducerConsumerFix pc){
        threadName=name;
        PC=pc;
    }

    public void run(){

        synchronized(PC) {
            for (int i = 0; i < 100000; i++) {
                if (threadName == "producer") PC.totalStock++;
                else if (threadName == "consumer") PC.totalStock--;
            }
        }

    }

    public void start () {
        if (t == null) {
            t = new Thread (this,threadName);
            t.start ();
        }
    }

}



