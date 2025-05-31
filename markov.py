import sympy

le=4
def experiment(A,x0,n):
    while n>0:
        x0=A*x0
        n=n-1
    return x0
def exper_(nn,vv,coord,n):
    S=None
    for i in range(len(nn)):
        if S==None:
            S=coord[i]*((nn[i])**n)*vv[i]
        else:
            S=coord[i]*((nn[i])**n)*vv[i]+S
    return S.evalf()

l=sympy.Symbol('l')

Ab=sympy.matrices.Matrix([[0.1,0.5,0.2,0.2],
                         [0.6,0.2,0,0.05],
                         [0,0.1,0,0],
                         [0.3,0.2,0.8,0.75]
                         ])
Ab=sympy.matrices.Matrix([[0.1,0.5,0.2,1],
                         [0.6,0.2,0,0],
                         [0,0.1,0,0],
                         [0.3,0.2,0.8,0]
                         ])
A=sympy.matrices.Matrix(
                        [
[0,0,1,0],
[1,0,0,0],
[0,0,0,1],
[1,0,0,0]
                            ]
                            )
A=Ab

print("A:\n",A,"\n")
x0=sympy.matrices.Matrix([[0.991],[0.001],[0.0],[0]])
print("x0:\n",x0,"\n")
beta_=sympy.matrices.Matrix()

vektory_i_chisla=A.eigenvects()
vc=vektory_i_chisla
#print(vc)
nn=[]
vv=[]
for i in range(le):
    print("i=",i)
    print(vc[i][2][0])
    beta_=beta_.col_insert(i,vc[i][2][0])
    nn.append(vc[i][0])
    vv.append(vc[i][2][0])
E=sympy.matrices.eye(le)
beta=[]
beta_vse=[]
for i in range(le):
    beta1=[]
    for j in range(le):
        stri=str("beta_")+str(j)+"_"+str(i)
        stri=sympy.Symbol(stri)
        #print(type(stri))
        beta1.append(stri)
        beta_vse.append(stri)
    beta.append(beta1)
beta=sympy.matrices.Matrix(beta)
for i in range(le):
    beta_s=[]
    for j in range(le):
        stri="beta_"+str(i)+"_"+str(j)
        stri=sympy.Symbol(stri)
        beta_s.append(stri)
    E=[[0] for i in range(le)]
    E[i]=[1]
    E=sympy.matrices.Matrix(E)
    beta_s=sympy.linsolve((beta_,E),beta_s).args[0]
    for j in range(le):
        beta[i+j*le]=beta_s[j]


new_coords=x0.transpose()*beta.transpose()
print("eigen numbers:\t",nn)
#for i in range(le):
#    print(nn[i],sympy.Abs(nn[i]))
#exit()
print("eigen vectors:\t",vv)
print("novye kkorinaty(v iskusstvennom bazise:)\t\n",new_coords)
S=None
SS=[]
for i in range(le):
    if nn[i]==1.0:
        if S==None:
            S=new_coords[i]*vc[i][2][0]
        else:
            S=S+new_coords[i]*vc[i][2][0]
    else:
        if -1.0==nn[i]:
            SS.append(new_coords[i]*vc[i][2][0])
        else:
            sss=new_coords[i]*vc[i][2][0]
            
                
            
    if 1.0==sympy.Abs(nn[i]):
        if S==None:
            S=new_coords[i]*vc[i][2][0]
        else:
            S=S+new_coords[i]*vc[i][2][0]
if S==None:
    S=sympy.matrices.Matrix([[0],[0],[0],[0]])
#print("sistema stremktsya k :\n",S,"\n_____________\n")
#print("experiment daet:\n",experiment(A,x0,21),"\n________")
#exper_(nn,vv,coord,n):
#print("proba formuloi:\n",exper_(nn,vv,new_coords,21),"\n________")
exit()
for i in range(1,45):
    #print(i,"experiment daet:\n",experiment(A,x0,i),"\n________")
    print("eshe:\t",((nn[1])**i*new_coords[1]*vc[1][2][0]+(nn[2])**i*new_coords[2]*vc[2][2][0]).evalf())
