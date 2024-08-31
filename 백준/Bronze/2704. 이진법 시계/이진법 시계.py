def zero(line):
    while len(line) != 6:
        line = "0" + line
    return line


for _ in range(int(input())):
    h, m, s = map(int, input().split(':'))
    h_b = zero(bin(h)[2:])
    m_b = zero(bin(m)[2:])
    s_b = zero(bin(s)[2:])
    r1 = ""
    for i in range(6):
        r1 += h_b[i] + m_b[i] + s_b[i]
    r2 = h_b + m_b + s_b
    print(r1, r2)