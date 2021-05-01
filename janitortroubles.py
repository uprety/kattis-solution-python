from  math import sqrt 
def getMaxArea(a,b,c,d):
    sp = (a + b + c + d)/2
    return  sqrt((sp - a) * (sp - b) * (sp - c) * (sp - d))

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    print(getMaxArea(a,b,c,d))
