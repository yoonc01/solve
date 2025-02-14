import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        boolean isValid = true;
        
        for (int i = 0; i < n; i++) {
            int accountableCount = 0;
            String[] task = br.readLine().split(" ");
            for (String person : task) {
                if (person.equals("A")) accountableCount++;
            }
            if (accountableCount != 1) {
                isValid = false;
                break;
            }
        }
        bw.write(isValid ? "Yes" : "No");
        bw.flush();
        br.close();
        bw.close();
    }
} 