def process(string): 
    print('Processing:', string)

with open("/Users/nanyao/Learn/Beginning-Python/Chapter11/11-6/text.txt") as f:
    char=f.read(1)
    while char:
        process(char)
        char=f.read()