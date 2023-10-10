
import java.util.BitSet;
class Answer {
    public static void main(String[] args) {
        Gen rand = new Gen();
        int cache_size = 1073741823;
        BitSet bs=new BitSet(cache_size);
        long MAX_CNT = 50000000000L;
        for (long i = 0; i < MAX_CNT; i++) {
            long ans = rand.next();
            if ((ans & 0x000000000000003f) == 0x0000000000000000) {
                bs.set((int)(ans >> 6));
            }
        }
        int cnt = 0;
        for (int i = 0; i < cache_size; i++) {
            if (bs.get(i)) {
                cnt++;
            }
        }
        System.out.println((long)cnt * 64);
    }
}
