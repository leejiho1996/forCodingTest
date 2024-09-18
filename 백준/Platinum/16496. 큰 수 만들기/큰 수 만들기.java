import java.io.*;
import java.util.*;


public class Main {

	static StringBuilder sb=new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n=Integer.parseInt(br.readLine());
		String arr[]=new String[n];
		st=new StringTokenizer(br.readLine());

		for(int i=0;i<arr.length;i++) 
			arr[i]=st.nextToken();

		Arrays.sort(arr,new Comparator<>() {
			@Override
			public int compare(String n1,String n2) {
				return (n2+n1).compareTo(n1+n2);
			}
		});
		
		for(int i=0;i<arr.length;i++)
			sb.append(arr[i]);

		boolean find=false;
		for(int i=0;i<sb.toString().length();i++) 
			if(sb.toString().charAt(i)!='0')  find=true;
		
		
		if(find)
			System.out.println(sb);
		else
			System.out.println("0");



	}
}