#Escriba un programa en python para eliminar un nodo con la clave dada en un arbol de busqueda
#binario (BST) dado

#Definicion: Nodo de arbol binario
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def delete_Node(root, key):
    #Si la raiz no existe simplemente devuelvala
    if not root:
        return root
    #Encuentre el nodo en el subarbol izquierdo si el valor clave es menor que el valor de la raiz
    if root.val > key:
        root.left = delete_Node(root.left, key)
    #Encuentre el nodo en el subarbol derecho si el valor clave es mayor que el valor de la raiz    
    elif root.val < key:
        root.right = delete_Node(root.right, key)
    #Elimnar el nodo si root.value==key
    else:
        #Si no hay hijos correctos, elimine el nodo y la nueva raiz seria root.left
        if not root.right:
            return root.left
        #Si no quedan hijos, elimine el nodo y la nueva raiz seria root.right
        if not root.left:
            return root.right
        #Si existen hijos izquierdo y derecho en el nodo, remplace su valor
        #Con el valor minimo en el subarbol derecho. Ahora elimina ese nodo minimo
        #En el subarbol derecho
        temp_val = root.right
        mini_val = temp_val.val
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.val
        #Eliminar el nodo minimo en el subarbol derecho
        root.right = delete_Node(root.right, root.val)
    return root

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(7)
print("Original node: ")
print(preOrder(root))
result = delete_Node(root, 4)
print("After deleting specified node: ")
print(preOrder(result))
















