import java.util.Arrays;
import java.util.Random;


public class Main {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
		String[] strings = new String[50000000];
    	int a=0x4e00;
    	int b=0x9fa5;
    	Random r=new Random(10);
    	for(int i=0;i<50000000;i++) {
			if (i % 500000 == 0) {
				System.out.printf("gen %d%% %d\n", i / 500000, System.currentTimeMillis() - startTime);
			}
    		int j=(int)(r.nextInt(4))+2;
			StringBuilder sb = new StringBuilder();
            for (int jj = 0; jj < j; jj++) {
                sb.append((char) (a + (int) (r.nextInt(b - a))));
            }
            strings[i] = sb.toString();
    	}
        System.out.printf("### sort start %d\n", System.currentTimeMillis() - startTime);
        Arrays.sort(strings);
        System.out.printf("### sort done %d\n", System.currentTimeMillis() - startTime);
        int num = strings[0].length() + 1;
        for (int i = 1; i < strings.length; i++) {
            if (i % 500000 == 0) {
                System.out.printf("diff %d%% %d\n", i / 500000, System.currentTimeMillis() - startTime);
            }
            int n = diff(strings[i - 1], strings[i]);
            num += n;
        }
        System.out.printf("done %d\n", System.currentTimeMillis() - startTime);
        System.out.println(num);
    }

    private static int diff(String a, String b) {
        char[] aa = a.toCharArray();
        char[] bb = b.toCharArray();
        int len = Math.min(aa.length, bb.length);
        int i = 0;
        for (; i < len; i++) {
            if (aa[i] != bb[i]) {
                break;
            }
        }
        return bb.length - i;
    }
}
