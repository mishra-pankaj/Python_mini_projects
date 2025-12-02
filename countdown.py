import time
timer = int(input("enter your time in ss "))
for x in range(timer, 0, -1):
    second = x%60
    min = int(x/60) %60
    print(f"00.{min:02}.{second:02}")
    time.sleep(1)
print("Times up")