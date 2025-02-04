word_list = []

def dfs(word):
    global word_list
    
    if len(word) <= 5:
        word_list.append(word)
    
    if len(word) == 5:
        return
    
    for i in ["A", "E", "I", "O", "U"]:
        dfs(word + i)
    
def solution(word):
    answer = 0
    dfs("")
    return word_list.index(word)