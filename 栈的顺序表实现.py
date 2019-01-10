#栈的顺序表实现
class SStack():             #基于顺序表技术实现的栈类
    def __init__(self):     #用list对象_elems存储栈中元素
        self._elems = []
        
    def is_empty(self):
        return self._elems == []
        
    def top(self):
        if self._elems == []:
            raise raise StackUnderflow("in SStack.top()")
        return self._elems[-1]
        
    def push(self, elem):
        self._elems.append(elem)
        
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()
           
class StackUnderflow(ValueError): #栈下溢（空栈访问）
                pass
