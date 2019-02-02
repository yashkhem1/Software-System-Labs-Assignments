import java.text.SimpleDateFormat;
import java.util.Date;

class runningClock implements Runnable{
    private Thread t;

    public void run() {
        SimpleDateFormat formatter = new SimpleDateFormat("HH:mm:ss");
        while(true) {
            Date date = new Date();
            System.out.println(formatter.format(date));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void start () {
        if (t == null) {
            t = new Thread (this);
            t.start ();
        }
    }

}

public class Clock{
    public static void main(String args[]){
        runningClock r1 = new runningClock();
        r1.start();
    }
}
