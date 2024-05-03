package main;

import java.io.FileInputStream;
import java.util.Properties;

public class ConfigLoader {
    public static String getApiKey() throws Exception {
        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream("config.properties")) {
            props.load(fis);
        }
        return props.getProperty("api_key");
    }
}
