import sys
    
if len(set(list(sys.stdin.readline().strip()))) % 2:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")