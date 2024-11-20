import java.util.HashMap;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "";
        HashMap<String, Integer> dic = new HashMap<>();
        dic.put("next", 10);
        dic.put("prev", -10);

        String[] endParts = video_len.split(":");
        int endTotal = Integer.parseInt(endParts[0]) * 60 + Integer.parseInt(endParts[1]);

        String[] opStartParts = op_start.split(":");
        String[] opEndParts = op_end.split(":");
        int opStartTotal = Integer.parseInt(opStartParts[0]) * 60 + Integer.parseInt(opStartParts[1]);
        int opEndTotal = Integer.parseInt(opEndParts[0]) * 60 + Integer.parseInt(opEndParts[1]);
        
        String[] posParts = pos.split(":");
        int posTotal = Integer.parseInt(posParts[0]) * 60 + Integer.parseInt(posParts[1]);

        
        if (opStartTotal <= posTotal && posTotal < opEndTotal) {
            posTotal = opEndTotal;
        }

        for (String command : commands) {
            posTotal += dic.get(command);
            posTotal = Math.max(0, posTotal); 
            posTotal = Math.min(endTotal, posTotal);

            if (opStartTotal <= posTotal && posTotal < opEndTotal) {
                posTotal = opEndTotal;
            }
        }

        if (posTotal / 60 < 10) {
            answer += "0" + (posTotal / 60);
        } else {
            answer += (posTotal / 60);
        }

        answer += ":";

        if (posTotal % 60 < 10) {
            answer += "0" + (posTotal % 60);
        } else {
            answer += (posTotal % 60);
        }

        return answer;
    }
}