i = 0  
total_skor = 0  
while True:
    d1, d2, d3 = input().split()
    i += 1  
    b1 = 10 if d1 == 'A' else 7 if d1 == 'B' else 4 if d1 == 'C' else 1 if d1 == 'D' else 0
    b2 = 10 if d2 == 'A' else 7 if d2 == 'B' else 4 if d2 == 'C' else 1 if d2 == 'D' else 0
    b3 = 10 if d3 == 'A' else 7 if d3 == 'B' else 4 if d3 == 'C' else 1 if d3 == 'D' else 0
    total_skor += b1 + b2 + b3
    hitungan_A = (d1 == 'A') + (d2 == 'A') + (d3 == 'A')
    if total_skor >= 70 or hitungan_A == 3:
        break
print(i, total_skor)