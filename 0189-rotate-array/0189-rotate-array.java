class Solution {
    public void rotate(int[] nums, int k) {
        if (k>0){
            List<Integer> li=new ArrayList<>();
            for(int i:nums){
                li.add(i);
            }
            Collections.rotate(li,k);
            for (int i=0;i<li.size();i++){
                nums[i]=li.get(i);
            }
        }
    }
}