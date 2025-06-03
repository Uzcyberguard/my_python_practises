N=int(input("sovg'a narxini ayt:"))
A,B,C=map(int,input().split())
if A+B+C>=N:
  print("yes")
elif A+B+C<N:
  print("no")
