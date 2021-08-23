import os
#d=1
#with open("data"+str(d)+".txt", "r") as u:
#    k = u.readlines()
#    print(k)
#    with open("data"+str(d-1)+".txt", "r") as o:
#        kk = o.readlines()
#        print(kk)
#        for kkk in kk:
#            k.remove(kkk)
#        print(k)
#        fileee=open("data"+str(d)+".txt","w")
#        fileee.writelines(k)
#        u.close()
#        o.close()
#        fileee.close()


for i in range(1,75501):
    #with open("data.txt", "r") as u:
    #    k = u.readlines()
    try:
        with open("y\\data"+str(i)+".txt", "r") as o:
            k=o.readlines()
            for kk in k:
                with open("veri.txt", "a") as p:
                    p.writelines(kk)
    except:
        i+=1

#os.remve("data"+str(d-1)+".txt")






