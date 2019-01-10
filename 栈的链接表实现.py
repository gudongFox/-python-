#栈的链接表实现
class StackUnderflow(ValueError): #栈下溢（空栈访问）
                pass
#建立节点模型：
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        
class LStack()；#基于链接表技术实现的栈类，用LNode作为结点
    def __init__(self):
        self._top = None
        
    def is_empty(self):
        return self._top is None
        
    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem
        
    def push(self, elem):
        self._top = LNode(elem, self._top)
        
    def pop(self):
        if self._top is None :
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self.top = p.next
        return p.elem
