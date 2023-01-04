nb = 1

i = 1

cpt = 0


while nb < 1000:
  for i  in range(1,1000): 
    if nb % i == 0 :
      cpt = cpt + 1
  
  i+=1
  
  if cpt < 3:
    print(nb) 
   
  nb = nb + 1
  cpt = 0