学习笔记
这周内 了解了树和对的实现以及应用
一、树
树是二维数据结构。树由节点和边组成，每条边连接两个节点，两个节点之间的关系为父节点和子节点。

树包含一个根节点，位于第0层，其余的节点依次位于第1层、第2层、第3层等。

链表是特殊化的树，树是特殊化的图。

二、二叉树
二叉树：每个节点最多有两个子节点，分别为左子节点和右子节点。

二叉树的遍历有三种：前序遍历、中序遍历、后序遍历。

前序遍历：依次访问根节点、左子树、右子树。

中序遍历：依次访问左子树、根节点、右子树。

后序遍历：依次访问左子树、右子树、根节点。

三、二叉搜索树
二叉搜索树是一棵空树或者具有下列性质的二叉树：

左子树上所有节点的值均小于根节点的值；

右子树上所有节点的值均大于根节点的值；

左子树和右子树也分别为二叉查找树。

二叉搜索树的中序遍历为升序排列。

二叉搜索树的查询、插入、删除操作的时间复杂度是O(log n)。

四、堆和二叉堆
堆是可以迅速找到一堆数种的最大或者最小值的数据结构。常见的有二叉堆和斐波那契堆。

二叉堆的操作的时间复杂度：

查找最大/最小元素的时间复杂度是O(1)；

删除最大/最小元素的时间复杂度是O(log n)；

插入元素的时间复杂度是O(log n)。

二叉堆通过完全二叉树实现。对于大顶堆，根节点的值最大，任意节点的值总是大于或等于其子节点的值；对于最小堆，根节点的值最小，任意节点的值总是小于或等于其子节点的值。

由于二叉堆通过完全二叉树实现，因此二叉堆常用的实现方式是数组。
