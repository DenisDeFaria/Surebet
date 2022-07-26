#Tu lances le programmme 


n=input("Nombre d'issues possible : ") # nombre de paris sur le match de possible pour couvrir toutes les options   
m=input("Mise maximale possible : ")   # Les côtes boostées en général on une mise maximale donc c'est ce qu'il faut renseigner 
i=input("issue de la mise max : ")     # Tu dois donner le numéro de la côte de la côte boosté

# Après tu vas devoir renseigner les différentes côtes donc la tu choisis en fonction des différents sites de paris afin d'avoir la meilleur côte possible, donc faut vraiment que tu sois sur quasi tous les sites pour optimiser le truc, je sais que winamax fait beaucoup de côte boostés donc check souvent chez eux
# Si il te dit pas de surebet ça veut dire que t'as pas de côte assez avantageuses pour t'assurer de faire de l'argent 
# Il va te donner toutes les issues et avec combien d'argent tu dois mettre, met en général quelque centimes genre 2-3 pour compenser la comission des sites mais si tu le fais pas c'est pas super grave c'est genre quelque centimes de diff 
# Il va te dire le taux de retour en gros ca te donner le pourcentage que tu gagnes sur ta mise total
# Et si tu suis bien le truc t'es sur de gagner et sa te donne combien tu vas gagner sur le surebet
# Dernier truc fait gaffe les côtes bouge souvent donc juste avant de faire ton paris vérifie bien les côtes sinon ca peut faire que t'es pas forcément gagnant


n=int(n)
m=int(m)
i=int(i)

def cotes(n):
    C=[]
    for k in range(n):
        c=input("Cotes de l'issue "+str(k+1)+" : ")
        C.append(float(c))
    return(C)

C = cotes(n)

def inverse(C):
    l=len(C)
    S=0
    for k in range(l):
        S=1/C[k]+S
    if S<1:
        return(True)
    else:
        return(False)

def inverse2(C):
    l=len(C)
    S=0
    for k in range(l):
        S=1/C[k]+S
    return(S)

def mise2(C,m,i):
    P=[]
    l=len(C)
    T=m*C[i-1]*inverse2(C)
    for k in range(l):
        if k==i-1:
            P.append(m)
        else:
            P.append(T/(C[k]*inverse2(C)))
    return(P)

P=mise2(C,m,i)

def fin(n,P):
    a="\n \n"
    S=0
    for j in range(len(P)):
        S=S+P[j]
    if inverse(C)==False:
        print("Pas de Surebet")
        print(str(1+1-inverse2(C)))
    else:
        b=1+1-inverse2(C)
        a=a+"Le taux de retoure est de : "+ str(b) + "\n"+ "Donc un gain de : "+ str(S*b-S) +"\n"
        for k in range(n):
            if k==n-1:
                a = a+"Miser pour l'issue "+str(k+1)+" : "+str(P[k])
            else:    
                a=a+"Miser pour l'issue "+str(k+1)+" : "+str(P[k])+"\n"

        print(a)


fin(n,P)
