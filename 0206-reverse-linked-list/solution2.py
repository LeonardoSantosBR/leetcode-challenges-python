# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: #*recursive*
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

solution = Solution()
solution.reverseList([1,2,3])

#*annotations*:
# - Ida (empilhando): cada chamada é colocada no topo da pilha e fica pausada, esperando a próxima retornar.

# - Volta (desempilhando): a pilha é LIFO (último a entrar, primeiro a sair). Então quem resolve primeiro é a chamada do topo, 
#reverseList(3), que é o caso base e retorna direto. Aí ela sai da pilha e o controle volta para reverseList(2), que continua exatamente 
#de onde parou (na linha logo depois de new_head = self.reverseList(head.next)). Depois ela sai, e o controle volta para reverseList(1).

# Uma linked list é só uma cadeia de nós, e você a representa guardando a referência ao primeiro nó. Quem tem o head, tem a lista toda, 
#porque consegue caminhar por .next até chegar no None.

# Então, no nosso exemplo, new_head = 3 significa: uma referência ao nó 3, que agora está no início da cadeia 3 → 2 → 1 → None.
#O que muda de frame para frame é o estado da cadeia que começa nesse nó:
#No frame 3 (caso base): new_head é o nó 3, e a cadeia é só 3 → None
#Depois que o frame 2 ajusta os ponteiros: o mesmo nó 3 agora inicia 3 → 2 → None
#Depois que o frame 1 ajusta os ponteiros: o mesmo nó 3 inicia 3 → 2 → 1 → None