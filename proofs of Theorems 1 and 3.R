#Read the data
#1. Direct moral ties
c<-read.table("\\Users\\axabadia\\Desktop\\Moral Ties\\proofs_moral ties\\fc.txt", header=F)
c<-c/100
#2. Indirect moral ties
imt<-read.table("\\Users\\axabadia\\Desktop\\Moral Ties\\proofs_moral ties\\cc.txt",header=F)
#3. Group cohesiveness
t<-read.table("\\Users\\axabadia\\Desktop\\Moral Ties\\proofs_moral ties\\ct.txt",header=F)
D<-list()
for(i in 1:length(c[,1])){
  D[i]<-c[i,1]^2
}
D<-as.numeric(D)
#Calculate expected values
Ec<-mean(c[,1])
Et<-mean(t[,1])
Eimt<-mean(imt[,1])
ED<-mean(D)
#Calculate variances
Vc<-var(c[,1])
Vt<-var(t[,1])
Vimt<-var(imt[,1])
Vc;Vimt
#Proof of Theorem 1
sEimt<-Et*ED
Eimt;sEimt;Et*(Ec^2+Vc)
#Proof of Theorem 3
var(imt[,1]);var(t[,1])*(var(D)+ED^2)+var(D)*Et^2


