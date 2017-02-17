class CodeReview {
    private static int twist(int seed) {
        return (((seed & 0x80000000) | ((2*seed) & 0x7fffffff)) >> 1) ^ (((2*seed) & 1) == 1 ? 0x9908b0df : 0);
    }
    public static void main(String[] args) {
//        for (int seed = Integer.MIN_VALUE; seed < Integer.MAX_VALUE ; ++seed) {
//            if (((398 * seed) ^ twist(seed) ^ 2074608327) == 0x80000000) {
//                System.out.println(seed);
//            }
//        }
//        System.out.println("none");
        int seed = 32132121;
        System.out.printf("(398 * seed) %x\n", (398 * seed));
        System.out.printf("twist(seed) %x\n", twist(seed));
        System.out.printf("2074608327 %x\n", 2074608327);
        System.out.printf("(398 * seed) ^ twist(seed) %x\n", (398 * seed) ^ twist(seed));
        System.out.printf("((398 * seed) ^ twist(seed) ^ 2074608327) %x\n", ((398 * seed) ^ twist(seed) ^ 2074608327));
    }
}
