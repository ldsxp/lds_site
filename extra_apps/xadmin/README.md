# xadmin 介绍



GitHub：https://github.com/sshwsfc/xadmin/tree/django2



## 修复 添加用户小组件出错



环境：

Python 3.5.6

Django 2.1

Xadmin

 

原因：

render函数在django2.1上有变化

 

解决方案：

1.在Python终端输入命令help('xadmin') 查看xadmin安装位置 得到如下输出

```sh
FILE
    /root/anaconda3/envs/learndjango/lib/python3.5/site-packages/xadmin/__init__.py
```

2.进入xadmin安装路径，编辑xadmin/views/dashboard.py

```python
 36     #render() got an unexpected keyword argument 'renderer'
 37     #修改bug, 添加renderer
 38     #by prism 2018/10/4
 39     def render(self, name, value, attrs=None, renderer=None):
```
