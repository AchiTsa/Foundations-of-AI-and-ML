import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class TupleCompWeighted implements Comparator<Tuple<Integer, Integer>> {
	public Tuple<Integer, Integer> goal;
	public Map<Tuple<Integer, Integer>, Integer> cost_so_far;
	public TupleCompWeighted (Tuple<Integer, Integer> g, Map<Tuple<Integer, Integer>, Integer> c) {
		goal=g;
		cost_so_far = c;
	}
	
	public void setCost_so_far(Map<Tuple<Integer, Integer>, Integer> c) {
		cost_so_far=c;
	}
	
	public Map<Tuple<Integer, Integer>, Integer> getCost_so_far() {
		return cost_so_far;
	}
    @Override
    public int compare(Tuple<Integer, Integer> a, Tuple<Integer, Integer> b) {
        // Assume neither string is null. Real code should
        // probably be more robust
        // You could also just return x.length() - y.length(),
        // which would be more efficient.
        if (hh(a) < hh(b)) {
            return -1;
        }
        if (hh(a) > hh(b)) {
            return 1;
        }
        return 0;
    }
    public int hh(Tuple<Integer, Integer> a) {
    	//|x1 - x2| + |y1 - y2|
    	return Math.abs(a.x-goal.x) + Math.abs(a.y-goal.y) + cost_so_far.get(a);
    }
}