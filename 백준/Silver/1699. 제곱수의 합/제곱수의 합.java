import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1]; 
        for (int i = 0; i <= n; i++) {
            dp[i] = i;
        }

        List<Integer> squares = new ArrayList<>();
        for (int i = 1; i * i <= n; i++) {
            squares.add(i * i);
        }

        for (int i = 2; i <= n; i++) {
            for (int square : squares) {
                if (square > i) break;
                dp[i] = Math.min(dp[i], dp[i - square] + 1);
            }
        }

        System.out.println(dp[n]);
    }
}
