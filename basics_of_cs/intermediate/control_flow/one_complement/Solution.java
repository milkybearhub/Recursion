class Solution{
    public static String oneComplement(String bits){
        String answer = "";
        for(int i = 0; i < bits.length(); i++) {
            answer += bits.charAt(i) == '0' ? "1" : "0";
        }
        return answer;
    }
}
