#Tu lances le programmme 


#nb_issue=input("Nombre d'issues possible : ") # nombre de paris sur le match de possible pour couvrir toutes les options   
#mise_max=input("Mise maximale possible : ")   # Les côtes boostées en général on une mise maximale donc c'est ce qu'il faut renseigner 
#issue_max=input("issue de la mise max : ")     # Tu dois donner le numéro de la côte de la côte boosté

# Après tu vas devoir renseigner les différentes côtes donc la tu choisis en fonction des différents sites de paris afin d'avoir la meilleur côte possible, donc faut vraiment que tu sois sur quasi tous les sites pour optimiser le truc, je sais que winamax fait beaucoup de côte boostés donc check souvent chez eux
# Si il te dit pas de surebet ça veut dire que t'as pas de côte assez avantageuses pour t'assurer de faire de l'argent 
# Il va te donner toutes les issues et avec combien d'argent tu dois mettre, met en général quelque centimes genre 2-3 pour compenser la comission des sites mais si tu le fais pas c'est pas super grave c'est genre quelque centimes de diff 
# Il va te dire le taux de retour en gros ca te donner le pourcentage que tu gagnes sur ta mise total
# Et si tu suis bien le truc t'es sur de gagner et sa te donne combien tu vas gagner sur le surebet
# Dernier truc fait gaffe les côtes bouge souvent donc juste avant de faire ton paris vérifie bien les côtes sinon ca peut faire que t'es pas forcément gagnant




def cotes(nb_issue):
    Cote=[]
    for k in range(nb_issue):
        c=input("Côtes de l'issue "+str(k+1)+" : ")
        Cote.append(float(c))
    return(Cote)

#Cote = cotes(nb_issue)

def inverse(Cote):
    l=len(Cote)
    inv=0
    for k in range(l):
        inv=1/Cote[k]+inv
    if inv<1:
        return(True)
    else:
        return(False)

def inverse2(Cote):
    l=len(Cote)
    inv=0
    for k in range(l):
        inv=1/Cote[k]+inv
    return(inv)

def mise2(Cote,mise_max,issue_max):
    P=[]
    l=len(Cote)
    T=mise_max*Cote[issue_max-1]*inverse2(Cote)
    for k in range(l):
        if k==issue_max-1:
            P.append(mise_max)
        else:
            P.append(T/(Cote[k]*inverse2(Cote)))
    return(P)

#P=mise2(Cote,mise_max,issue_max)

def fin(nb_issue, mise_max, issue_max):
    Cote = cotes(nb_issue)
    P=mise2(Cote,mise_max,issue_max)


    a="\n \n"
    S=0
    for j in range(len(P)):
        S=S+P[j]
    if inverse(Cote)==False:
        print("Pas de Surebet")
        print(str(1+1-inverse2(Cote)))
    else:
        b=1+1-inverse2(Cote)
        a=a+"Le taux de retoure est de : "+ str(b) + "\n"+ "Donc un gain de : "+ str(S*b-S) +"\n"
        for k in range(nb_issue):
            if k==nb_issue-1:
                a = a+"Miser pour l'issue "+str(k+1)+" : "+str(P[k])
            else:    
                a=a+"Miser pour l'issue "+str(k+1)+" : "+str(P[k])+"\n"

        print(a)

if __name__ == '__main__':
    nb_issue=input("Nombre d'issues possible : ") # nombre de paris sur le match de possible pour couvrir toutes les options   
    nb_issue=int(nb_issue)

    mise_max=input("Mise maximale possible : ")   # Les côtes boostées en général on une mise maximale donc c'est ce qu'il faut renseigner 
    mise_max=int(mise_max)

    issue_max=input("issue de la mise max : ")     # Tu dois donner le numéro de la côte de la côte boosté
    issue_max=int(issue_max)


    fin(nb_issue, mise_max, issue_max)
