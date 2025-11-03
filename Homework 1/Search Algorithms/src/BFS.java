import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class BFS {
	int iterations=0;

	public BFS() {
	}

	public static String replaceCharUsingCharArray(String str, char ch, int index) {
		char[] chars = str.toCharArray();
//	    if(chars[index]== '#') {
//	    	chars[index] = '+';
//	    }
		if (chars[index] != 'D' && chars[index] != 's')
			chars[index] = ch;
		return String.valueOf(chars);
	}

	public LinkedList<Tuple<Integer, Integer>> getPossibleNeighbors(Tuple<Integer, Integer> location) { // return up,
																										// down, left
																										// and right
		LinkedList<Tuple<Integer, Integer>> neighbors = new LinkedList<>();
		neighbors.add(new Tuple<Integer, Integer>(location.x - 1, location.y));
		neighbors.add(new Tuple<Integer, Integer>(location.x + 1, location.y));
		neighbors.add(new Tuple<Integer, Integer>(location.x, location.y - 1));
		neighbors.add(new Tuple<Integer, Integer>(location.x, location.y + 1));
		return neighbors;
	}

	public void my_search(String[] map_data, Tuple<Integer, Integer> start) {
		// start can be a tuple (x, y)

		Queue<Tuple<Integer, Integer>> frontier = new LinkedList<>();
		frontier.add(start);
		Map<Tuple<Integer, Integer>, Tuple<Integer, Integer>> came_from = new HashMap<>();
		came_from.put(start, null); // null equals to nothing before

		Tuple<Integer, Integer> beforeCurrent = start;
		Tuple<Integer, Integer> Diamond = start;
		while (!(frontier.isEmpty())) {
			iterations++;
			Tuple<Integer, Integer> current = frontier.remove();
			if (map_data[current.x].charAt(current.y) == 'D') {
				// came_from.put(current, beforeCurrent);
				Diamond = current;
				System.out.println("Found the Diamond at position " + current.x + "/" + current.y);
				break;
			}
//	    	came_from.put(current, beforeCurrent);
//	    	
			@SuppressWarnings("unchecked")
			LinkedList<Tuple<Integer, Integer>> neighbors = getPossibleNeighbors(current);
			for (int i = 0; i < neighbors.size(); i++) {
				iterations++;
				if (neighbors.get(i).x >= 0 && neighbors.get(i).x < map_data.length) { // check that the x cordinate of
																						// the neighbor is in the field
					if (neighbors.get(i).y >= 0 && neighbors.get(i).y < map_data[neighbors.get(i).x].length()) { // check
																													// that
																													// the
																													// y
																													// cordinate
																													// of
																													// the
																													// neighbor
																													// is
																													// in
																													// the
																													// field
						if (came_from.containsKey(neighbors.get(i)) == false
								&& map_data[neighbors.get(i).x].charAt(neighbors.get(i).y) != '*') {
							frontier.add(neighbors.get(i));
							came_from.put(neighbors.get(i), current);
						}
					}
				} else {
					continue;
				}

			}
			beforeCurrent = current;
		}
		if (Diamond.x == start.x && Diamond.y == start.y) {
			System.out.println("Either Diamond is at starting point or there is no diamond.");
		}
		int steps = 2;
		while (came_from.get(Diamond) != null) {
			iterations++;
			steps ++;

//			if(Diamond.x == start.x && Diamond.y == start.y) {
//				return;
//			}
			Tuple<Integer, Integer> before = came_from.get(Diamond);
			map_data[before.x] = replaceCharUsingCharArray(map_data[before.x], '#', before.y);
			Diamond = before;

		}
		for (int i = 0; i < map_data.length; i++) {
			System.out.println(map_data[i]);
		}
		System.out.println("number of steps: " + steps);

	}

	public static String[] TXT2Array(String Path) throws IOException {
		List<String> listOfStrings = new ArrayList<String>();

		// load data from file
		BufferedReader bf = new BufferedReader(new FileReader(Path));

		// read entire line as string
		String line = bf.readLine();

		// checking for end of file
		while (line != null) {
			listOfStrings.add(line);
			line = bf.readLine();
		}

		// closing bufferreader object
		bf.close();

		// storing the data in arraylist to array
		String[] array = listOfStrings.toArray(new String[0]);

		return array;

	}

	public static void main(String[] args) throws IOException {
		String[] lava_map1 = new String[] { "      **               **      ", "     ***     D        ***      ",
				"     ***                       ", "                      *****    ", "           ****      ********  ",
				"           ***          *******", " **                      ******", "*****             ****     *** ",
				"*****              **          ", "***                            ", "              **         ******",
				"**            ***       *******", "***                      ***** ", "                               ",
				"                s              ", };
		String[] lava_map2 = new String[] { "     **********************    ", "   *******   D    **********   ",
				"   *******                     ", " ****************    **********", "***********          ********  ",
				"            *******************", " ********    ******************", "********                   ****",
				"*****       ************       ", "***               *********    ", "*      ******      ************",
				"*****************       *******", "***      ****            ***** ", "                               ",
				"                s              ", };
		String[] lava_map3 = new String[] { "     **********************    ", "   ******   D    **********    ",
				"**********  ****************** ", "***               *********    ", "***               *********    ",
				"***               *********    ", "***               *********    ", "***               *********    ",
				"**************    *********    ", "s              *************** ", };

		BFS abc = new BFS();
		String[] lava_map300=TXT2Array("C:\\Users\\achil\\Downloads\\ITI0210_caves\\cave600x600.txt");
		Tuple<Integer, Integer> start = new Tuple<Integer, Integer>(2, 2);
	    long start1 = System.nanoTime();
		abc.my_search(lava_map300, start);
		long end1 = System.nanoTime();      
	    System.out.println("Elapsed Time in milli-seconds: "+ ((end1-start1)/1000000));
	    System.out.println("number of iterations: "+ abc.iterations);  

	}
	

}
