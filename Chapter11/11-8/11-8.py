def process(string): 
    print('Processing:', string)

with open("/Users/nanyao/Learn/Beginning-Python/Chapter11/11-6/text.txt") as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)