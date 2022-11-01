
def es_primo(num ): 
    contador=0 
    for i in range(1,num+1): 
        if num & i==0: 
            contador+=1 
            print(contador) 


es_primo(20)
