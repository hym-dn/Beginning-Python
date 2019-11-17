def process(string): 
    print('Processing:', string)

with open("/Users/nanyao/Learn/Beginning-Python/Chapter11/11-6/text.txt") as f:
    while True:
        char=f.read(1)
        if not char:
            break
        process(char)