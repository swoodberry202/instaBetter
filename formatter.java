import java.io.*;
//import java.io.File;
//import java.io.FileNotFoundException;
import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
public class formatter {
    public static void main(String[] args) throws FileNotFoundException, IOException {
        File myFile = new File("capLibrary.txt");
        File clean = new File("cleanCaption.txt");
        Scanner s = new Scanner(myFile);
        String q = "";
        while (s.hasNextLine()) {
            q += s.nextLine();

        }

        FileWriter writer = new FileWriter(clean);
        FileWriter old = new FileWriter(myFile);
        String captions = "";
        String test = "";
//
//        for (int i = 0; i < 78; i++) {
//            test = q.substring(q.indexOf("text") + 7);
//            int myEnd = test.indexOf("}}]}");
//            captions += q.substring(q.indexOf("text") + 7, (myEnd + q.indexOf("text") + 7));
//            captions += "\n";
//            q = q.substring((q.indexOf("}}]}") + 4));
//
//        }
        int capStart=0;
        int capEnd=0;
        while (q.indexOf("node\":{\"text\":\"")!=-1){
            capStart=q.indexOf("node\":{\"text\":\"")+15;//I add 15 to eliminate the quotes in captions
            capEnd=q.indexOf("\"}}]},\"shortcode\":\"");

        captions += (q.substring(capStart, capEnd)) + "\n";
            q = q.substring(capEnd + 20);

        }

        String testyBoi = captions;

//        String rest="";
//        for (int x=0;x<captions.length();x++){
//            tag= captions.indexOf("#");
//            if (tag>=0){
//                rest=testyBoi.substring(tag,testyBoi.length()-1);
//                if (rest.indexOf(" ")!=-1)
//            }
//        }
        //System.out.println(captions);

        int end=0;
        boolean b=true;
        String start="";

        while (b){
            if (testyBoi.indexOf("#")!=-1){
                start=testyBoi.substring(0,testyBoi.indexOf("#"));
                end=(testyBoi.substring(testyBoi.indexOf("#"))).indexOf(" ");
                if (end!=-1) {
                    testyBoi = start + ((testyBoi.substring(testyBoi.indexOf("#"))).substring(end));
                }
                else {
                    testyBoi = start;
                    b=false;
                }
            }
            else {b=false;}
                }

        while (b){
            if (testyBoi.indexOf("#")!=-1){
                start=testyBoi.substring(0,testyBoi.indexOf("#"));
                end=(testyBoi.substring(testyBoi.indexOf("#"))).indexOf("\n");
                if (end!=-1) {
                    testyBoi = start + ((testyBoi.substring(testyBoi.indexOf("#"))).substring(end));
                }
                else {
                    testyBoi = start;
                    b=false;
                }
            }
            else {b=false;}
        }
        while (b){
            if (testyBoi.indexOf("#")!=-1){
                start=testyBoi.substring(0,testyBoi.indexOf("#"));
                end=(testyBoi.substring(testyBoi.indexOf("#"))).indexOf("\n");
                if (end!=-1) {
                    testyBoi = start + ((testyBoi.substring(testyBoi.indexOf("#"))).substring(end));
                }
                else {
                    testyBoi = start;
                    b=false;
                }
            }
            else {b=false;}
        }
        while (b){
            if (testyBoi.indexOf("#")!=-1){
                start=testyBoi.substring(0,testyBoi.indexOf("#"));
                end=(testyBoi.substring(testyBoi.indexOf("#"))).indexOf("\"");
                if (end!=-1) {
                    testyBoi = start + ((testyBoi.substring(testyBoi.indexOf("#"))).substring(end));
                }
                else {
                    testyBoi = start;
                    b=false;
                }
            }
            else {b=false;}
        }
        testyBoi = testyBoi.replaceAll("[^\\x00-\\x7F]", "");
////
////        // erases all the ASCII control characters
        testyBoi = testyBoi.replaceAll("[\\p{Cntrl}&&[^\r\n\t]]", "");
////
////        // removes non-printable characters from Unicode
//        testyBoi = testyBoi.replaceAll("\\p{C}", "");

//
        //cleanTextContent(testyBoi);


        //System.out.println(testyBoi);
        writer.write(testyBoi);
        //writer.flush();
        writer.close();
//        for (int i=0;i<testyBoi.length()-1;i++){
//            if (testyBoi.substring(i,i+1).equals("\\u")){
//                String startOfSting=testyBoi.substring(0,i);
//                String restOfString=testyBoi.substring(i+2);
//                testyBoi=startOfSting+"\\u"+restOfString;
//                i++;s
//            }
//        }
//        System.out.println("\n \n NOW WITH WEIRDNESS \n \n");
//        System.out.println(testyBoi);
//
//        System.out.println("\u0442 \u0434");

        }



}