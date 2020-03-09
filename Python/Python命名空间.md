# Python命名空间与作用域

## 命名空间

### 什么是命名空间？

> `namespace`， A *namespace* is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries。
>
> 命名空间是一个 字典（dictionary） ，它的键就是变量名，它的值就是那些变量的值。

### python中命名空间的例子

**局部命名空间**：每个函数都有自己的命名空间，它记录了函数所使用的局部变量变量（参数、局部变量）等
**全局命名空间**：每个模块也有自己的命名空间，它记录了模块的变量、函数等
**内置命名空间**：python记录内置函数的空间

### 命名空间的生存周期

正如函数、模块都有它们的生命周期，依赖它们存在的命名空间一样具有生命周期。

**局部命名空间**：当函数返回结果、抛出异常时，被删除。**特别注意，每一个递归调用的函数都拥有自己的命名空间**。
**全局命名空间**：在模块被导入时创建，保存到解释器退出。
**内置命名空间**：在python解释器启动时创建，永远不会被删除。

### 命名空间的查找顺序

当python使用一个变量`x`时，会按以下顺序到所有可用的命名空间中去寻找该变量的值：

1. 局部命名空间
2. 全局命名空间
3. 内置命名空间
4. 如果以上均找不到，则抛出异常。如果以上在某个命名空间找到了，则会立刻停止寻找。

嵌套函数的情况：

   1、先在当前 (嵌套的或 lambda) 函数的命名空间中搜索

   2、然后是在父函数的命名空间中搜索

   3、接着是模块命名空间中搜索

   4、最后在内置命名空间中搜索

## 作用域

### 什么是作用域？

个人理解的就是一个变量可发挥作用的范围。

一个 *作用域* 是一个命名空间可直接访问的 Python 程序的文本区域

### 作用域的类型

- L （Local） 局部作用域
- E （Enclosing） 闭包函数外的函数中
- G （Global） 全局作用域
- B （Built-in） 内建作用域

[`global`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#global) 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；[`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。

以 ***L –> E –> G –>B\*** 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

Python除了**`def/class/lambda`** 外，其他如: **`if/elif/else/ try/except for/while`**并不能改变其作用域。定义在他们之内的变量，外部还是可以访问

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

```python
>>> After local assignment: test spam
>>> After nonlocal assignment: nonlocal spam
>>> After global assignment: nonlocal spam
>>> In global scope: global spam
```



## 参考文章

[Python 作用域和命名空间]: https://docs.python.org/zh-cn/3/tutorial/classes.html#python-scopes-and-namespaces
[Python命名空间的本质]: https://www.cnblogs.com/windlaughing/archive/2013/05/26/3100362.html



