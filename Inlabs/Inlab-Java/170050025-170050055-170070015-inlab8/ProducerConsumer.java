public class ProducerConsumer {
    public static int totalStock = 0;

    public static void main(String args[]){
        ProducerConsumer PC = new ProducerConsumer();
        runDemo p = new runDemo("producer", PC);
        runDemo c = new runDemo("consumer", PC);

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


class runDemo implements Runnable{
    public Thread t;
    private String threadName;

    private ProducerConsumer PC;

    runDemo(String name, ProducerConsumer pc){
        threadName=name;
        PC=pc;
    }

    public void run(){


        for (int i = 0; i < 100000; i++) {
            if (threadName == "producer") PC.totalStock++;
            else if (threadName == "consumer") PC.totalStock--;
        }


    }

    public void start () {
        if (t == null) {
            t = new Thread (this,threadName);
            t.start ();
        }
    }

}



