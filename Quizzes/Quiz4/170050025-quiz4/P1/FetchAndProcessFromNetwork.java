import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;

public class FetchAndProcessFromNetwork implements FetchAndProcess {
    private List<String> data = new ArrayList<>();

    @Override
    public void fetch(List<String> paths) {
      // Implement here
        String path=null;
        for(int i = 0; i < paths.size(); i++) {

            try {
                path = paths.get(i);
                URL url = new URL(path);
                URLConnection urlcon = url.openConnection();
                InputStream stream = urlcon.getInputStream();
                int j;
                String pokemon="";
                while((j=stream.read())!=-1){
                    char a = (char)j;
                    //System.out.println(a);
                    if (a!=' ' && a!='\n') pokemon = pokemon+ a;
                    else{
                        data.add(pokemon);
                        pokemon="";
                    }
                }
            }

            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public String process() {
      // Implement here
        int arrayLength=data.size();
        String result="";
        for(int i = 0; i < arrayLength; i++){
            result = result+data.get(i);
            result=result+"\n";
        }
        return result;
    }
}
