package com.mr.u;

import java.util.Base64;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        System.out.println("Encoding JSON");
        // String base64Encoded = DatatypeConverter.printBase64Binary(jsonBytes);

        String json = "";
        File f = new File(
                getClass().getClassLoader().getResource("email-activity-party.json").getFile()
        );
        FileReader fr = new FileReader(f);
        char[] letters = new char[(int) f.length()];
        fr.read(letters);
        fr.close();
        String content = new String(letters);

        String s = encodeBase64(json);
        System.out.println("Decoded JSON");
    }

    public static String encodeBase64(String encodeMe){
        byte[] b = encodeMe.getBytes();
        // byte[] b = encodeMe.getBytes(Charset.forName("UTF-8"));
        byte[] encodedBytes = Base64.getEncoder().encode(b);
        return new String(encodedBytes) ;
    }
}
