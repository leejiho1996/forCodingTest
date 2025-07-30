words = []

while True:
    try:
        line = input()
    except EOFError:
        break

    for i in line.rstrip().split():
        words.append(i)
        
stdout = ""
line_count = 0

for token in words:
    if token == "<br>":
        stdout += "\n"
        line_count = 0
    elif token == "<hr>":
        if line_count:
            stdout += "\n"
        stdout += "-"*80 + "\n"
        line_count = 0
    elif line_count + len(token) + 1 <= 80:
        stdout += " "*(bool(line_count)) + token
        line_count += len(token) + 1
    else:
        stdout += "\n" + token
        line_count = len(token)

print(stdout)
