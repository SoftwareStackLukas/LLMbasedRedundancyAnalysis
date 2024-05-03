import wordfinders.DatamuseConnector;
import wordfinders.WordnikConnector;

public class Main {
    public static void main(String[] args) {
        String[] words = new DatamuseConnector().getSimilarWords("webpage");
        String wordToCompare = "website";
        String contained = "no";
        for (String word : words) {
            if (word.equals(wordToCompare)) {
                contained = "yes";
                break;
            }
        }

        System.out.println("Word is contained: " + contained);

        // Wirdnik Connector

        words = new WordnikConnector().getSimilarWords("webpage");
        wordToCompare = "website";
        contained = "no";
        for (String word : words) {
            if (word.equals(wordToCompare)) {
                contained = "yes";
                break;
            }
        }

        System.out.println("Word is contained: " + contained);
    }
}