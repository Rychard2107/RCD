def sequencia(n):
    sequence = [0, 1]
    while len(sequence) < n:
        a = sequence[-1] + sequence[-2]
        sequence.append(a)
    return sequence
n=int(input("Digite uma posição da sequência:"))
result = sequencia(n)
print("Essa é a sua sequência: ",result)
print("alteração")



        

        
    
    
        
        
    