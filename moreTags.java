//Name: sloan woodberry
// Name: moreTags.java
// Purpose:to format randomly picked hashtags for a post caption in myPost.py
// Date: 5/9/19
// Collaborators: None
import java.io.*;
import java.util.*;
import java.util.ArrayList;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.util.ArrayList;
public class moreTags{
    public static void main(String[] args)  throws FileNotFoundException, IOException {
        Scanner s = new Scanner(System.in);
        File myTags = new File("tags.txt");
        File clean = new File("cleanPostTags.txt");
        Scanner fileScan = new Scanner(myTags);
        Random r = new Random();
//this reads in tags.txt into tagList
        ArrayList<String> tagList = new ArrayList<String>();
        while (fileScan.hasNextLine()) {
            String q=fileScan.nextLine();
            tagList.add(q);
        }
        String cleanTags = "";
        //this picks 20 random tags from tags.txt to put in my caption
        for (int i = 0; i < 20; i++) {
            cleanTags+="#"+tagList.get(r.nextInt(tagList.size()))+" ";
        }
        System.out.println(cleanTags);
//this puts the tags into cleanPostTags.txt for them to be read in for my Post

        FileWriter writer = new FileWriter(clean);
        writer.write(cleanTags);
        writer.close();
    }

}