import glob,os


li=[]
def get(path):
    lo=[]
    lu=glob.glob(path)
    for i in lu:
        if os.path.isdir(i):
            lo.append([i]+get(i+"\\*"))
        else:
            lo.append(i)
    return lo

def print_all(dist,lev=1,src=""):
    if src!="":
        print("-",src)
    print("     |"*lev)
    #print("- "+os.path.split(dist[0])[0])
    for i in dist:
        if dist[-1]==i:
            if type(i)==list:
                print("     |"*(lev-1)+"     +--",i[0])
                print_all(i[1:],lev+1)
            else:
                print("     |"*(lev-1)+"     +-* "+i)
        else:
            if type(i)==list:
                print("     |"*lev+"--",i[0])
                print_all(i[1:],lev+1)
            else:
                print("     |"*lev+"-* "+i)

            
    print("     |"*(lev-1))
    
def get_all(dist,lev=1):
    #print("- "+os.path.split(dist[0])[0])
    for i in dist:
            if type(i)==list:
                #print("     |"*(lev-1)+"     +--",i[0])
                get_all(i[1:],lev+1)
            else:
                #print("     |"*(lev-1)+"     +-* "+i)
                try:
                    with open(i,"r",encoding="utf-8") as fg:
                        pt=fg.read()
                        if pt.find("githubLink")!=-1:
                            print(i)
                    
                except:
                    pass
li=get("C:\\Users\\gino\\Desktop\\hexo-theme-commerce\\themes\\commerce\\*")
print_all(li,src="C:\\Users\\gino\\Desktop\\hexo-theme-commerce\\themes\\commerce")
get_all(li)
print(li)
    