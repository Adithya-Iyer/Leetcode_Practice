class Solution {
    public int rev(int num) {
        String s = String.valueOf(num);
        int l = s.length();
        char[] ch = s.toCharArray();
        for (int i=0; i<(l/2); i++) {
            char c = ch[i];
            ch[i] = ch[l-1-i];
            ch[l-1-i] = c;
        }
        return Integer.valueOf(new String(ch));
    }
    public boolean isSameAfterReversals(int num) {
        int reversed1 = rev(num);
        int reversed2 = rev(reversed1);
        return (reversed2==num);
    }
}