import random

win = 0
lose = 0
i = 0

for _ in range(1000): # Chạy 1000 lần thử nghiệm
    balance = 1000 # Số dư ban đầu
    o = 0
    i += 1 # Đếm số lần lặp
    print(f"Lần lặp thứ {i}")

    while balance > 1 and balance < 2000: # Chơi cho đến khi cháy tài khoản hoặc x2
        pick = random.choice([1,2,3,4]) # Chọn ngẫu nhiên 1 (thắng) hoặc 2 (thua)

        if pick == 1: # Thắng
            balance = balance + ((balance * 0.1)*3)
            o += 1 # Đếm số lần chơi trong mỗi lần lặp
            print (f"Lần chơi thứ {o} của lần lặp thứ {i}. Số dư hiện tại: {balance:.2f}")
        
        else: # Thua
            o += 1 # Đếm số lần chơi trong mỗi lần lặp
            balance = balance - (balance * 0.1)
            print (f"Lần chơi thứ {o} của lần lặp thứ {i}: thua, số dư hiện tại: {balance:.2f}")

    if balance <= 1: # Cháy tài khoản
        lose += 1

    else: # X2 tài khoản
        win += 1

print("")
print(f"Sau 1000 lần chơi, bạn x2 tài khoản được {win} lần và bị cháy tài khoản {lose} lần.")