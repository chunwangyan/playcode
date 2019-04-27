# 二叉搜索树的构造、查询、删除
# 二叉搜索树：通过中序遍历能够得到有序序列的树形结构,一种性能介于顺序搜索和二分查找之间的搜索方法，插入与删除操作较二分查找有时明显

# 构造树的节点类
class TreeNode(object):

    # 节点类初始化函数
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    # 返回类节点的左孩子
    def hasLeftChild(self):
        return self.left

    # 返回类节点的右孩子
    def hasRightChild(self):
        return self.right

    # 判断本节点是否是左孩子节点
    def isLeftChild(self):
        return self.parent and self.parent.left == self

    # 判断本节点是否为右孩子节点
    def isRightChild(self):
        return self.parent and self.parent.right == self


# 构造一棵二叉搜索树
class BSTree(object):

    # 初始化一棵空树
    def __init__(self):
        self.root = None
        self.size = 0

    # 返回树的size
    def length(self):
        return self.size

    # 向搜索树插入一个节点x
    def insert(self, x):
        node = TreeNode(x)
        if not self.root:
            self.root = node
            self.size += 1
        else:
            currentNode = self.root
            while True:
                if x < currentNode.key:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = node
                        node.parent = currentNode
                        self.size += 1
                        break
                elif x > currentNode.key:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = node
                        node.parent = currentNode
                        self.size += 1
                        break
                else:
                    break

    # 查询key是否在搜索树中
    def find(self, key):
        if self.root:
            res = self._find(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _find(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)


    def findMin(self):
        if self.root:
            current = self.root
            while current.left:
                current = current.left
            return current
        else:
            return None

    def _findMin(self, node):
        if node:
            current = node
            while current.left:
                current = current.left
            return current

    def findMax(self):
        if self.root:
            current = self.root
            while current.right:
                current = current.right
            return current
        else:
            return None

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.find(key)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node):
        if not node.left and not node.right:  # node为树叶
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        elif node.left and node.right:  # 有两个儿子
            minNode = self._findMin(node.right)
            node.key = minNode.key
            self.remove(minNode)

        else:  # 有一个儿子
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.isRightChild():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:  # node为根
                    self.root = node.left
                    node.left.parent = None
                    node.left = None
            else:
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:  # node为根
                    self.root = node.right
                    node.right.parent = None
                    node.right = None


if __name__ == '_main_':
    # pass
    bst = BSTree()
    bst.__init__()
    print(bst.length())
