import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FetchAndProcessFromDisk implements FetchAndProcess {
    private List<String> data = new ArrayList<>();

    @Override
    public void fetch(List<String> paths){
      // Implement here
        int length = paths.size();
        String path = null;
        for(int i = 0; i < length; i++){
            path=paths.get(i);
            try {
                File file = new File(path);
                FileReader fileReader = new FileReader(file);
                BufferedReader bufferedReader = new BufferedReader(fileReader);
//            StringBuffer stringBuffer = new StringBuffer();
                String line;
                while ((line = bufferedReader.readLine()) != null) {
                    data.add(line);
                }
                fileReader.close();
            }

            catch(Exception e){e.printStackTrace();}
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
