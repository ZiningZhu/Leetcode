public class LogSystem {

    private HashMap<String, Integer> hm;
    private HashMap<Integer, String> d;

    public LogSystem() {
        hm = new HashMap();
        hm.put("Year", 4);
        hm.put("Month", 7);
        hm.put("Day", 10);
        hm.put("Hour", 13);
        hm.put("Minute", 16);
        hm.put("Second", 19);
        d = new HashMap<Integer, String>();

    }

    public void put(int id, String timestamp) {
        d.put(id, timestamp);
    }

    public List<Integer> retrieve(String s, String e, String gra) {
        List<Integer> res = new ArrayList<Integer>();
        for (int id : d.keySet()) {
            String str = d.get(id);
            int loc = hm.get(gra);
            str = str.substring(0, loc);
            s = s.substring(0, loc);
            e = e.substring(0, loc);

            //System.out.println("id=" + id + "; str=" + str + "; s=" + s + "; e=" + e);
            if (str.compareTo(s) >= 0 && str.compareTo(e) <= 0) {
                res.add(id);
                //System.out.println("Added!");
            }
        }
        return res;
    }
}

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * List<Integer> param_2 = obj.retrieve(s,e,gra);
 */
