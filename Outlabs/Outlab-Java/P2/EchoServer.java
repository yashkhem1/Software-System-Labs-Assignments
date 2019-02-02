import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class EchoServer
{

    private static Socket socket;

    public static void main(String[] args)
    {
        try
        {

            int port = 8025;
            ServerSocket serverSocket = new ServerSocket(port);
            //System.out.println("Server Started and listening to the port 25000");

            //Server is running always. This is done using this while(true) loop
            while(true)
            {
                //Reading the message from the client
                socket = serverSocket.accept();
                InputStream is = socket.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                String request = br.readLine();
                System.out.println(request);


                for(int i = 0; i < args.length; i++){
                    request = request + args[i];
                }

                String response = request + "\n";

                //Sending the response back to the client.
                OutputStream os = socket.getOutputStream();
                OutputStreamWriter osw = new OutputStreamWriter(os);
                BufferedWriter bw = new BufferedWriter(osw);
                bw.write(response);
                //System.out.println(response);
                bw.flush();
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }

        finally
        {
            try
            {
                socket.close();
            }
            catch(Exception e){}
        }
    }
}