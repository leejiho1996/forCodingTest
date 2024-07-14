import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException { //예외처리 꼭 해줘야 함
	    HashMap<String,String> hashMap = new HashMap<>(); //key,value에 String말고 다른 데이터타입 넣을 수있음
		
		String[] colors= {"black","brown","red","orange","yellow","green","blue","violet","grey","white"};
		
		for (int i=0; i<10;i++) {
			//HashMap은 put으로 값 추가 가능
			hashMap.put(colors[i], Integer.toString(i)); //☆int to String
		}
		
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //BufferedReader 사용 
	
		
		String[] inputs = new String[3];
		
		for (int i=0; i<3;i++) { 
			StringTokenizer st = new StringTokenizer(br.readLine());
			inputs[i]=st.nextToken();
			//System.out.println(inputs[i]);
		}
		
		StringBuilder sb = new StringBuilder();
		
		sb.append(hashMap.get(inputs[0]));
		sb.append(hashMap.get(inputs[1]));
		for (int i=0; i<Integer.parseInt(hashMap.get(inputs[2])); i++) { //☆String to int
			sb.append('0');
		}
		
		 
		BigInteger BigI = new BigInteger(sb.toString());
		
		
		System.out.println(BigI);
		
		
	}
		
}

