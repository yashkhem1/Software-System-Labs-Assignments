import java.io.IOException;
import java.util.List;

public interface FetchAndProcess {
    void fetch(List<String> paths);

    String process();
}
