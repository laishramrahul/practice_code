import pyonmttok
tokenizer = pyonmttok.Tokenizer("conservative", joiner_annotate=True)
f_read=open("/home/laishram/workspace/mt/data/assamese/train.en.txt","r")
for eachline in f_read:
    tokens=tokenizer(eachline)
    print(*tokens)
#tokens = tokenizer("মেলি থোৱা দীঘল চুলি।")
#print(*tokens)