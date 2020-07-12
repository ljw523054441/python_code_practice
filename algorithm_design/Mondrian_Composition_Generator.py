add_library('peasycam')

#基本单位
l=200
#刻度
scale_p=4
#生成体块的量的多少（0~1之间）
keep = 1
#规则输入
rule="ABCDEF"
rule_list=[]


def setup():
    global cam
    cam = PeasyCam(this, 400)
    cam.setMinimumDistance(50)
    size(scale_p*l,scale_p*l,P3D)
    
    generate()
    patch()
    colour()
    
def draw():
    background(251,252,244)
    length_all = scale_p*l
    
    #绘制块块
    for h in range(len(xs1)):
        noStroke()
        g=int(rec_col[h])
        if g<4:
            fill(255,247,0)
        elif g<7:
            fill(247,0,4)
        elif g<10:
            fill(4,4,160)
        else:
            fill(26,20,20)
            
        x = (xs1[h]*l+xs2[h]*l)/2
        y = (ys1[h]*l+ys2[h]*l)/2
        z = (zs1[h]*l+zs2[h]*l)/2
        
        a = abs(xs2[h]-xs1[h])*l
        b = abs(ys2[h]-ys1[h])*l
        c = abs(zs2[h]-zs1[h])*l
            
        pushMatrix()
        translate(x,y,z)
        box(a,b,c)
        popMatrix()
    
    #绘制面
    fill(255)
    stroke(0)
    strokeWeight(7)
    strokeCap(SQUARE)
    for k in range(len(A_add)):
        shape1=createShape()
        shape1.beginShape()
        shape1.vertex(A_add[k]*l,0,0)
        shape1.vertex(A_add[k]*l,length_all,0)
        shape1.vertex(A_add[k]*l,length_all,length_all)
        shape1.vertex(A_add[k]*l,0,length_all)
        shape1.endShape(CLOSE)
        shape(shape1,0,0)
        
    for k in range(len(B_add)):
        shape2=createShape()
        shape2.beginShape()
        shape2.vertex(0,B_add[k]*l,0)
        shape2.vertex(length_all,B_add[k]*l,0)
        shape2.vertex(length_all,B_add[k]*l,length_all)
        shape2.vertex(0,B_add[k]*l,length_all)
        shape2.endShape(CLOSE)
        shape(shape2,0,0)
        
    for k in range(len(C_add)):
        shape3=createShape()
        shape3.beginShape()
        shape3.vertex(0,0,C_add[k]*l)
        shape3.vertex(length_all,0,C_add[k]*l)
        shape3.vertex(length_all,length_all,C_add[k]*l)
        shape3.vertex(0,length_all,C_add[k]*l)
        shape3.endShape(CLOSE)
        shape(shape3,0,0)
        
    for k in range(len(D_add)):
        shape4=createShape()
        shape4.beginShape()
        shape4.vertex(D_add[k]*l,D_st1[k]*l,D_st2[k]*l)
        shape4.vertex(D_add[k]*l,D_ed1[k]*l,D_st2[k]*l)
        shape4.vertex(D_add[k]*l,D_ed1[k]*l,D_ed2[k]*l)
        shape4.vertex(D_add[k]*l,D_st1[k]*l,D_ed2[k]*l)
        shape4.endShape(CLOSE)
        shape(shape4,0,0)
        
    for k in range(len(E_add)):
        shape5=createShape()
        shape5.beginShape()
        shape5.vertex(E_st1[k]*l,E_add[k]*l,E_st2[k]*l)
        shape5.vertex(E_ed1[k]*l,E_add[k]*l,E_st2[k]*l)
        shape5.vertex(E_ed1[k]*l,E_add[k]*l,E_ed2[k]*l)
        shape5.vertex(E_st1[k]*l,E_add[k]*l,E_ed2[k]*l)
        shape5.endShape(CLOSE)
        shape(shape5,0,0)
        
    for k in range(len(F_add)):
        shape6=createShape()
        shape6.beginShape()
        shape6.vertex(F_st1[k]*l,F_st2[k]*l,F_add[k]*l)
        shape6.vertex(F_ed1[k]*l,F_st2[k]*l,F_add[k]*l)
        shape6.vertex(F_ed1[k]*l,F_ed2[k]*l,F_add[k]*l)
        shape6.vertex(F_st1[k]*l,F_ed2[k]*l,F_add[k]*l)
        shape6.endShape(CLOSE)
        shape(shape6,0,0)
        
    
    
def generate():
    
    #全局变量，点坐标
    global x1
    global y1
    global z1
    global x2
    global y2
    global z2
    
    #立方体每条边切分
    x1=[0]
    y1=[0]
    z1=[0]
    x2=[scale_p]
    y2=[scale_p]
    z2=[scale_p]
    
    #切分形成的网格点
    global A_gr
    global B_gr
    global C_gr
    A_gr=[]
    B_gr=[]
    C_gr=[]
    
    #存储每种切分语法的运行结果
    global A_add
    global B_add
    global C_add
    A_add=[]
    B_add=[]
    C_add=[]
    
    global D_add
    global D_st1
    global D_ed1
    global D_st2
    global D_ed2
    
    global E_add
    global E_st1
    global E_ed1
    global E_st2
    global E_ed2
    
    global F_add
    global F_st1
    global F_ed1
    global F_st2
    global F_ed2
    
    D_add=[]
    D_st1=[]
    D_ed1=[]
    D_st2=[]
    D_ed2=[]
    
    E_add=[]
    E_st1=[]
    E_ed1=[]
    E_st2=[]
    E_ed2=[]
    
    F_add=[]
    F_st1=[]
    F_ed1=[]
    F_st2=[]
    F_ed2=[]
    
    for i in range(scale_p):
        A_gr.append(i+1)
        B_gr.append(i+1)
        C_gr.append(i+1)
        
    for letter in list(rule):
        rule_list.append(letter)
        
    for n in range(len(rule_list)):
        
        c = rule_list[n]
        if c=='A':
            s_a = len(A_gr)
            r_a = int(random(0,s_a-1))
            A_add.append(A_gr[r_a])
            r = len(x1)
            for j in range(r):
                if x1[j]<A_gr[r_a] and x2[j]>A_gr[r_a]:
                    x1.append(A_gr[r_a])
                    y1.append(y1[j])
                    z1.append(z1[j])
                    x2.append(x2[j])
                    y2.append(y2[j])
                    z2.append(z2[j])
                    
                    x2[j]=A_gr[r_a]
            A_gr = rmv(A_gr,r_a)
        elif c=='B':
            s_b = len(B_gr)
            r_b = int(random(0,s_b-1))
            B_add.append(B_gr[r_b])
            s = len(y1)
            for w in range(s):
                if y1[w]<B_gr[r_b] and y2[w]>B_gr[r_b]:
                    x1.append(x1[w])
                    y1.append(B_gr[r_b])
                    z1.append(z1[w])
                    x2.append(x2[w])
                    y2.append(y2[w])
                    z2.append(z2[w])
                    
                    y2[w]=B_gr[r_b]
            B_gr=rmv(B_gr,r_b)
        elif c=='C':
            s_c = len(C_gr)
            r_c = int(random(0,s_c-1))
            C_add.append(C_gr[r_c])
            t = len(z1)
            for p in range(t):
                if z1[p]<C_gr[r_c] and z2[p]>C_gr[r_c]:
                    x1.append(x1[p])
                    y1.append(y1[p])
                    z1.append(C_gr[r_c])
                    x2.append(x2[p])
                    y2.append(y2[p])
                    z2.append(z2[p])
                    
                    z2[p]=C_gr[r_c]
            C_gr=rmv(C_gr,r_c)
        elif c=='D':
            if len(B_add)+len(E_add)+len(C_add)+len(F_add)==0:
                #如果没有其他方向的分隔，就把D当做A来画
                s_d = len(A_gr)
                r_d = int(random(0,s_d-1))
                A_add.append(A_gr[r_d])
                s = len(x1)
                for j in range(s):
                    if x1[j]<A_gr[r_d] and x2[j]>A_gr[r_d]:
                        x1.append(A_gr[r_d])
                        y1.append(y1[j])
                        z1.append(z1[j])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        x2[j]=A_gr[r_d]
                A_gr=rmv(A_gr,r_d)
            else:
                s_d = len(A_gr)
                r_d = int(random(0,s_d-1))
                
                D_add.append(A_gr[r_d])
                D_cont1 = []
                D_cont2 = []
                D_cont1.append(0)
                D_cont2.append(0)
                
                for q in range(len(B_add)):
                    D_cont1.append(B_add[q])
                if len(E_add)>0:
                    pos_d_be = len(E_add)
                    for k in range(pos_d_be):
                        if E_st1[k]<A_gr[r_d] and E_ed1[k]>A_gr[r_d]:
                            D_cont1.append(E_add[k])
                D_cont1.append(scale_p)
                D_cont1.sort()
                D_pick1=int(random(1,len(D_cont1)-1))
                D_st1.append(D_cont1[D_pick1-1])
                D_ed1.append(D_cont1[D_pick1])
                
                for q in range(len(C_add)):
                    D_cont2.append(C_add[q])
                if len(F_add)>0:
                    pos_d_cf = len(F_add)
                    for k in range(pos_d_cf):
                        if F_st1[k]<B_gr[r_d] and F_ed1[k]>B_gr[r_d]:
                            D_cont2.append(F_add[k])
                D_cont2.append(scale_p)
                D_cont2.sort()
                D_pick2=int(random(1,len(D_cont2)-1))
                D_st2.append(D_cont2[D_pick2-1])
                D_ed2.append(D_cont2[D_pick2])
                
                s = len(x1)
                for j in range(s):
                    if x1[j]<=A_gr[r_d] and x2[j]>=A_gr[r_d] and y1[j]>=D_cont1[D_pick1-1] and y2[j]<=D_cont1[D_pick1] and z1[j]>=D_cont2[D_pick2-1] and z2[j]<=D_cont2[D_pick2]:
                        x1.append(A_gr[r_d])
                        y1.append(y1[j])
                        z1.append(z1[j])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        x2[j]=A_gr[r_d]
            
                A_gr = rmv(A_gr,r_d)
        elif c=='E':
            if len(A_add)+len(D_add)+len(C_add)+len(F_add)==0:
                #如果没有其他方向的分隔，就把E当做B来画
                s_e = len(B_gr)
                r_e = int(random(0,s_e-1))
                B_add.append(B_gr[r_e])
                r=len(y1)
                for j in range(r):
                    if y1[j]<B_gr[r_e] and y2[j]>B_gr[r_e]:
                        x1.append(x1[j])
                        y1.append(B_gr[r_e])
                        z1.append(z1[j])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        y2[j]=B_gr[r_e]
                B_gr=rmv(B_gr,r_e)
            else:
                s_e = len(B_gr)
                r_e = int(random(0,s_e-1))
                
                E_add.append(B_gr[r_e])
                E_cont1 = []
                E_cont2 = []
                E_cont1.append(0)
                E_cont2.append(0)
                
                for q in range(len(A_add)):
                    E_cont1.append(A_add[q])
                if len(D_add)>0:
                    pos_e_ad = len(D_add)
                    for k in range(pos_e_ad):
                        if D_st1[k]<C_gr[r_e] and D_ed1[k]>C_gr[r_e]:
                            E_cont1.append(D_add[k])
                E_cont1.append(scale_p)
                E_cont1.sort()
                    
                E_pick1=int(random(1,len(E_cont1)-1))
                E_st1.append(E_cont1[E_pick1-1])
                E_ed1.append(E_cont1[E_pick1])
                    
                for q in range(len(C_add)):
                    E_cont2.append(C_add[q])
                if len(F_add)>0:
                    pos_e_cf = len(F_add)
                    for k in range(pos_e_cf):
                        if F_st2<B_gr[r_e] and F_ed2>B_gr[r_e]:
                            E_cont2.append(F_add[k])
                E_cont2.append(scale_p)
                E_cont2.sort()
                
                E_pick2=int(random(1,len(E_cont2)-1))
                E_st2.append(E_cont2[E_pick2-1])
                E_ed2.append(E_cont2[E_pick2])
                
                r = len(y1)
                for j in range(r):
                    if x1[j]>=E_cont1[E_pick1-1] and x2[j]<=E_cont1[E_pick1] and y1[j]<=B_gr[r_e] and y2[j]>=B_gr[r_e] and z1[j]>=E_cont2[E_pick2-1] and z2[j]<=E_cont2[E_pick2]:
                        x1.append(x1[j])
                        y1.append(B_gr[r_e])
                        z1.append(z1[j])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        y2[j]=B_gr[r_e]
                
                B_gr = rmv(B_gr,r_e)
                
        elif c=='F':
            if len(A_add)+len(D_add)+len(B_add)+len(F_add)==0:
                #如果没有其他方向的分隔，就把F当做C来画
                s_f = len(C_gr)
                r_f = int(random(0,s_f-1))
                C_add.append(C_gr[r_f])
                t=len(z1)
                for j in range(t):
                    if z1[j]<C_gr[r_f] and y2[j]>C_gr[r_f]:
                        x1.append(x1[j])
                        y1.append(y1[j])
                        z1.append(C_gr[r_f])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        z2[j]=C_gr[r_f]
                C_gr=rmv(C_gr,r_f)
            else:
                s_f = len(C_gr)
                r_f = int(random(0,s_f-1))
                
                F_add.append(C_gr[r_f])
                F_cont1 = []
                F_cont2 = []
                F_cont1.append(0)
                F_cont2.append(0)
                
                for q in range(len(A_add)):
                    F_cont1.append(A_add[q])
                if len(D_add)>0:
                    pos_f_ad = len(D_add)
                    for k in range(pos_f_ad):
                        if D_st2[k]<C_gr[r_f] and D_ed2[k]>C_gr[r_f]:
                            F_cont1.append(D_add[k])
                F_cont1.append(scale_p)
                F_cont1.sort()
                
                F_pick1=int(random(1,len(F_cont1)-1))
                F_st1.append(F_cont1[F_pick1-1])
                F_ed1.append(F_cont1[F_pick1])
                
                for q in range(len(B_add)):
                    F_cont2.append(B_add[q])
                if len(E_add)>0:
                    pos_f_be = len(E_add)
                    for k in range(pos_f_be):
                        if E_st1[k]<A_gr[r_f] and E_ed1[k]>A_gr[r_f]:
                            F_cont2.append(E_add[k])
                F_cont2.append(scale_p)
                F_cont2.sort()
                
                F_pick2=int(random(1,len(F_cont2)-1))
                F_st2.append(F_cont2[F_pick2-1])
                F_ed2.append(F_cont2[F_pick2])
                
                t = len(z1)
                for j in range(t):
                    if x1[j]>=F_cont1[F_pick1-1] and x2[j]<=F_cont1[F_pick1] and y1[j]>=F_cont2[F_pick2-1] and y2[j]<=F_cont2[F_pick2] and z1[j]<=C_gr[r_f] and z2[j]>=C_gr[r_f]:
                        x1.append(x1[j])
                        y1.append(y1[j])
                        z1.append(C_gr[r_f])
                        x2.append(x2[j])
                        y2.append(y2[j])
                        z2.append(z2[j])
                        z2[j]=C_gr[r_f]
                        
                C_gr = rmv(C_gr,r_f)                        

def rmv(arr,item):
    outgoing = []
    for z in range(len(arr)-1):
        if z<item:
            outgoing.append(arr[z])
        else:
            outgoing.append(arr[z+1])
    return outgoing

def patch():
    num = []
    rec_c = len(x1)
    
    for u in range(rec_c):
        num.append(u)
    
    
    rec_c = len(x1)
    q = int(rec_c*keep)

    
    global xs1
    global ys1
    global zs1
    global xs2
    global ys2
    global zs2
    
    xs1 = []
    ys1 = []
    zs1 = []
    xs2 = []
    ys2 = []
    zs2 = []
    

    for g in range(q):
        xs1.append(x1[int(num[g])])
        xs2.append(x2[int(num[g])])
        ys1.append(y1[int(num[g])])
        ys2.append(y2[int(num[g])])
        zs1.append(z1[int(num[g])])
        zs2.append(z2[int(num[g])])
        

def colour():
    
    global rec_col
    
    rec_col = []
    
    add_no = 0
    for u in range(len(x1)):
        add1 = int(random(0,12))
        if add_no>(len(x1)/6):
            add1 = int(random(0,10))
        rec_col.append(add1)
        if add1>9:
            add_no = add_no+1
            
def keyPressed():

    
    whole_length = createWriter("data/whole_length.txt")
    
    box_xs1 = createWriter("data/box_xs1.txt")
    box_ys1 = createWriter("data/box_ys1.txt")
    box_zs1 = createWriter("data/box_zs1.txt")
    
    box_xs2 = createWriter("data/box_xs2.txt")
    box_ys2 = createWriter("data/box_ys2.txt")
    box_zs2 = createWriter("data/box_zs2.txt")
    
    list_A_add = createWriter("data/A_add.txt")
    list_B_add = createWriter("data/B_add.txt")
    list_C_add = createWriter("data/C_add.txt")
    list_D_add = createWriter("data/D_add.txt")
    list_D_st1 = createWriter("data/D_st1.txt")
    list_D_ed1 = createWriter("data/D_ed1.txt")
    list_D_st2 = createWriter("data/D_st2.txt")
    list_D_ed2 = createWriter("data/D_ed2.txt")
    list_E_add = createWriter("data/E_add.txt")
    list_E_st1 = createWriter("data/E_st1.txt")
    list_E_ed1 = createWriter("data/E_ed1.txt")
    list_E_st2 = createWriter("data/E_st2.txt")
    list_E_ed2 = createWriter("data/E_ed2.txt")
    list_F_add = createWriter("data/F_add.txt")
    list_F_st1 = createWriter("data/F_st1.txt")
    list_F_ed1 = createWriter("data/F_ed1.txt")
    list_F_st2 = createWriter("data/F_st2.txt")
    list_F_ed2 = createWriter("data/F_ed2.txt")
    
    if key == ENTER:
        
        
        whole_length.print(scale_p*l)
        whole_length.flush()
        whole_length.close()
        
        for i in range(len(xs1)):
            box_xs1.println(xs1[i]*l)
        box_xs1.flush()
        box_xs1.close()
        
        for i in range(len(ys1)):
            box_ys1.println(ys1[i]*l)
        box_ys1.flush()
        box_ys1.close()
        
        for i in range(len(zs1)):
            box_zs1.println(zs1[i]*l)
        box_zs1.flush()
        box_zs1.close()
        
        for i in range(len(xs2)):
            box_xs2.println(xs2[i]*l)
        box_xs2.flush()
        box_xs2.close()
        
        for i in range(len(ys2)):
            box_ys2.println(ys2[i]*l)
        box_ys2.flush()
        box_ys2.close()
        
        for i in range(len(zs2)):
            box_zs2.println(zs2[i]*l)
        box_zs2.flush()
        box_zs2.close()
            
        
        print("A_add printed")
        for i in range(len(A_add)):
            list_A_add.println(A_add[i]*l)
        list_A_add.flush()
        list_A_add.close()
        
        print("B_add printed")
        for i in range(len(B_add)):
            list_B_add.println(B_add[i]*l)
        list_B_add.flush()
        list_B_add.close()
        
        print("C_add printed")
        for i in range(len(C_add)):
            list_C_add.println(C_add[i]*l)
        list_C_add.flush()
        list_C_add.close()
        
        print("D_add printed")
        for i in range(len(D_add)):
            list_D_add.println(D_add[i]*l)
        list_D_add.flush()
        list_D_add.close()
        
        print("E_add printed")
        for i in range(len(E_add)):
            list_E_add.println(E_add[i]*l)
        list_E_add.flush()
        list_E_add.close()
        
        print("F_add printed")
        for i in range(len(F_add)):
            list_F_add.println(F_add[i]*l)
        list_F_add.flush()
        list_F_add.close()
        
        print("D_st1 printed")
        for i in range(len(D_st1)):
            list_D_st1.println(D_st1[i]*l)
        list_D_st1.flush()
        list_D_st1.close()
        
        print("E_st1 printed")
        for i in range(len(E_st1)):
            list_E_st1.println(E_st1[i]*l)
        list_E_st1.flush()
        list_E_st1.close()
        
        print("F_st1 printed")
        for i in range(len(F_st1)):
            list_F_st1.println(F_st1[i]*l)
        list_F_st1.flush()
        list_F_st1.close()
        
        print("D_st2 printed")
        for i in range(len(D_st2)):
            list_D_st2.println(D_st2[i]*l)
        list_D_st2.flush()
        list_D_st2.close()
        
        print("E_st2 printed")
        for i in range(len(E_st2)):
            list_E_st2.println(E_st2[i]*l)
        list_E_st2.flush()
        list_E_st2.close()
        
        print("F_st2 printed")
        for i in range(len(F_st2)):
            list_F_st2.println(F_st2[i]*l)
        list_F_st2.flush()
        list_F_st2.close()
        
        print("D_ed1 printed")
        for i in range(len(D_ed1)):
            list_D_ed1.println(D_ed1[i]*l)
        list_D_ed1.flush()
        list_D_ed1.close()
        
        print("E_ed1 printed")
        for i in range(len(E_ed1)):
            list_E_ed1.println(E_ed1[i]*l)
        list_E_ed1.flush()
        list_E_ed1.close()
        
        print("F_ed1 printed")
        for i in range(len(F_ed1)):
            list_F_ed1.println(F_ed1[i]*l)
        list_F_ed1.flush()
        list_F_ed1.close()
        
        print("D_ed2 printed")
        for i in range(len(D_ed2)):
            list_D_ed2.println(D_ed2[i]*l)
        list_D_ed2.flush()
        list_D_ed2.close()
        
        print("E_ed2 printed")
        for i in range(len(E_ed2)):
            list_E_ed2.println(E_ed2[i]*l)
        list_E_ed2.flush()
        list_E_ed2.close()
        
        print("F_ed2 printed")
        for i in range(len(F_ed2)):
            list_F_ed2.println(F_ed2[i]*l)
        list_F_ed2.flush()
        list_F_ed2.close()
        
            