distancia=int(input("quantos kilomesteros vc rodou"))   
preço=distancia*50
cobrar=distancia*45
if distancia>200:
  print("de acordo com os kilosmestros rodados {} km,ira pagar 45 centavos entao fica  {}".format(distancia,cobrar))
else:  
    print("de acordo com os kilosmestros rodados {} km,ira pagar 50 centavos entao fica  {} ".format(distancia,preço))