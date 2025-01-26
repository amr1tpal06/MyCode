public class {
    public static void main(String[] args)
        int a =5;
        char b ='i'
        long c=400;
        double d=3.2;
        String name="Amrit";
}

  private Node treeFromList(List<Integer> values) {

        if(values.isEmpty()) {

            return null;

        }

        root = new Node(values.getFirst());

        for(int idx = 1; idx < values.size(); idx++) {

            addToTree(values.get(idx));

        }

        return root;

    }

 

