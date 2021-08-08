class Solution{
    public static int sumOfAllPrimes(int n){
        // 1と2は個別に処理
        if (n == 1) {
            return 0;
        } else if (n == 2) {
            return 2;
        }

        int sum = 2;
        while (n > 2) {
            // 2で割り切れるなら素数ではない
            if (n % 2 == 0) {
                n -= 1;
                continue;
            }

            for(int i = 3; n / 2 >= i; i++) {
                if (n % i == 0) {
                    n -= 1;
                    i = 3;
                    continue;
                }
            }
            sum += n;
            n -= 1;
        }
        return sum;
    }
}