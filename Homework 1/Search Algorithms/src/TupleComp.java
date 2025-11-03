import java.util.Comparator;

public class TupleComp implements Comparator<Tuple<Integer, Integer>> {
	public Tuple<Integer, Integer> goal;
	public TupleComp (Tuple<Integer, Integer> g) {
		goal=g;
	}
    @Override
    public int compare(Tuple<Integer, Integer> a, Tuple<Integer, Integer> b) {
        // Assume neither string is null. Real code should
        // probably be more robust
        // You could also just return x.length() - y.length(),
        // which would be more efficient.
        if (h(a) < h(b)) {
            return -1;
        }
        if (h(a) > h(b)) {
            return 1;
        }
        return 0;
    }
    public int h(Tuple<Integer, Integer> a) {
    	//|x1 - x2| + |y1 - y2|
    	return Math.abs(a.x-goal.x)+Math.abs(a.y-goal.y);
    }
}