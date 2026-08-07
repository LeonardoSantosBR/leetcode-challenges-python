class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001 #*counting sort*
        for x in arr1: 
            count[x] += 1
        
        res = []
        for x in arr2:                
           res += [x] * count[x]
           count[x] = 0             
        for v in range(1001):         
           res += [v] * count[v]
        return res
        
solution = Solution()
solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])

# Counting sort é um algoritmo de ordenação que não compara elementos. 
# Ele nunca pergunta "a é maior que b?".
# Em vez disso, usa o próprio valor como endereço de memória.

#A ideia inteira cabe em uma frase: se você sabe quantas vezes cada valor aparece, 
# você já sabe a ordem final — basta despejar os valores lendo a tabela de trás pra frente… 
# ou melhor, de frente pra trás, na ordem dos índices.