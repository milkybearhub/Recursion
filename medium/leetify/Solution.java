class Solution{
    public static String leetify(String stringInput){
        return stringInput.replaceAll("[aA]", "4")
                          .replaceAll("[bB]", "8")
                          .replaceAll("[eE]", "3")
                          .replaceAll("[lL]", "1")
                          .replaceAll("[oO]", "0")
                          .replaceAll("[sS]", "5")
                          .replaceAll("[tT]", "7")
                          .replaceAll("[zZ]", "2");
    }
}
