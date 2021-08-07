import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

class Solution{
    public static double distanceToOrigin(int x,int y){
        return Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
    }
}
