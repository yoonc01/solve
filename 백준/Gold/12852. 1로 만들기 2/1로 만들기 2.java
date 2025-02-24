import java.util.*;
import java.io.*;

public class Main {
    static int n, dp[], prev[];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    
    static public void main(String []args) throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new int[n + 1];
        prev = new int[n + 1];
        for (int i = 0; i < n + 1; i++)
            dp[i] = n + 1;
        dp[1] = 0;
        for (int current = 2; current < n + 1; current++) {
            dp[current] = dp[current - 1] + 1;
            prev[current] = current - 1;
            if (current % 2 == 0 && dp[current / 2] + 1 < dp[current]) {
                dp[current] = dp[current / 2] + 1;
                prev[current] = current / 2;
            }
            if (current % 3 == 0 && dp[current / 3] + 1 < dp[current]) {
                dp[current] = dp[current / 3] + 1;
                prev[current] = current / 3;
            }
        }
        sb.append(dp[n]).append("\n");
        while(n != 0) {
            sb.append(n).append(" ");
            n = prev[n];
        }
        System.out.println(sb);
    }
}