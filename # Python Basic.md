# Python 入门基础
***************************************************************
## 一、Pycharm Reference
1. **Pycharm 默认添加脚本头部注释**
https://www.cnblogs.com/zachyard/p/12818649.html

2. **Pycharm在虚拟环境下创建新项目**
```python
# cmd 命令行进入，创建python 虚拟环境
python -m venv -h
python -m venv vendemo	# 创建一个名为venvdemo的虚拟环境

# 当要将虚拟环境配置到其他盘时，用命令行进入其他磁盘下的目录，
# 可先输入盘符，如进入d盘，可先输入d:\
# 再cd到根目录下执行命令
```


  > _**Pycharm中创建新项目**_ ，相当于是在虚拟环境下建立了一个子文件夹，子文件夹自动生成下有Include、Lib、Scripts、pyvenv.cfg，假设我们想将我们在Pycharm中练习的脚本存放到My_study，将pythonproject替换成my_study。


3. **pycharm快捷键** 
![img](https://cdn.nlark.com/yuque/0/2021/png/22725236/1636092955256-7aeeff5e-fe53-4482-972d-b1fac5f3cb7d.png)

***************************************************************

## **二、数据类型**
### (一) 常用数据类型
1. String 字符串
  + +合并字符串
  + \t  制表符
  + \n 换行符	
2. Number 数字
    + int 整数
    + float 浮点
    + complex 复数
3. Bool 布尔
4. List 列表
  + 可变, []
5. Tuple 元组
  + 不可变, ()
6. Dict 字典
  + {}, 存储键值对, 如: name: admin
7. Set 集合
  + {} / set(), 无序, 元素不重复
8. None 类型
  + None不支持任何运算也没有任何内建方法
  + None和任何其他的数据类型比较, 永远返回False
  + None有自己的数据类型NoneType，不能创建其他NoneType对象（它只有一个值None）
  + None与0、空列表、空字符串不一样
  + 可以将None赋值给任何变量，也可以给None值变量赋值
  + None是没有像len,size等属性的，要判断一个变量是否为None，直接使用

### (二) 数据类型的转换
1. 数值型 - 字符串	str
2. 字符串 - 数值型(整型 / 浮点型)	int/float
3. **int 无法转换成float 类型的字符串**, float 可以转成int 类型
4. 字符串 - 列表	
	+ string. split(sep = None, maxsplit = -1)	将字符串以一定规则切割成列表
5. 列表 - 字符串
	+ 'sep'.join(iterable)	将列表以一定规则转成字符串, **只有列表中为字符串类型才能使用join**
6. 字符串 - bytes	encode
7. bytes - 字符串	decode
8. 元组, 列表, 集合间的转换
	+ 列表 - 集合	set
	+ 元组 - 集合	set
	+ 列表 - 元组	tuple
	+ 集合 - 元组	tuple
	+ 元组 - 列表	list
	+ 集合 - 列表	list

***************************************************************

## 三、函数
### （一）内置函数
#### 1. 字符串

+ 常用内置函数

```python
	+ string.capitalize()	# 将字符串的首字母大写，其他字母小写
	+ string.casefold()		# 将全部字母小写, casefold除了英文字母可以转化外，还可以转化其他语言
	+ string.lower()		# 将全部字母小写
	+ string.upper()		# 将字符串全部大写
	+ string.swapcase()		# 将字符串中进行大小写转换
	+ string.isspace()		# 判断字符串是否由空格组成的字符串
	+ string.istitle()		# 判断字符串是否是一个标题类型
	+ string.isupper()		# 判断字符串中的字母是否都是大写
	+ string.islower()		# 判断字符串中的字母是否都是小写
	+ string.zfill(width)	# 为字符串定义长度，如不满足，缺少的部分用0填补，填补在字符串左侧, width: 新字符串希望的宽度
	+ string.count(item)	# 计数
	+ string.startswith(item)	# 判断字符串开始位置是否时某成员, item: 查询的元素, 返回一个布尔值
	+ string.endswith(item)		#判断字符串结尾是否是某成员, item: 查询的元素，返回一个布尔值
	+ string.find(item)		# 查找元素的位置, find找不到元素, 会返回-1
	+ string.index(item)	# 查找元素的位置, index 找不到元素, 直接报错
	+ string.strip(item)	# 去掉字符串左右两边的指定元素，默认是空格
		+ lstrip 仅去掉字符串开头的指定元素或空格
		+ rstrip 仅去掉字符串结尾的指定元素或空格
	+ string.replace(old, new, max)	# 替换字符串的元素, max表示替换几次，默认全部替换
```

+ 格式化字符串	**重点**

  1. %s, %

     my name is %s, my age is %s' % ('dewei', 33)

  2. {}.format

     my name is {}, my age is {} . format('dewei', 33)

  3. f''

     name = 'dewei'

     age = 33

     f'my name is {name}, my age is {age}'. 

#### 2. 列表
```python
	+ list.append(new_item)	# 将元素添加到列表的结尾
	+ list.insert(index, new_item)	# 在指定索引位置插入值
	+ list.count(item)	# 计数
	+ list.remove(item)	# 删除列表中的某个元素
	+ list.reverse()	#将当前列表顺序进行反转
	+ list.sort(cmp = None, key = None, reverse = False) # 按一定功能排序
      ○ cmp -- 可选参数，制定排序方案的函数
      ○ key -- 参数比较
      ○ reverse -- 排序规则,  reverse = True降序, reverse = False升序（默认）
	+ list.clear()	#将当前列表中的数据清空
	+ list.copy()	# 当当前列表复制一份相同的列表, 新列表和旧列表内容相同, 但内存空间不同
	+ list.extend(item) # 将其他列表或元组中的元素导入到当前列表中，只能导入列表和元组、字符串、字典类型，其中字符串导入后会被拆分成单个字符，字典类型只能导入key
	+ list.pop(index)	# 通过索引删除并获取列表的元素
	+ del list(index)	# 通过del删除索引
```

#### 3. 字典
```python
**字典添加数据**
	+ dict[key] = value	# 字典没有索引，添加或修改，根据key是否存在所决定， 一次只能添加或修改一个值，value还可以做运算
	+ dict.update (new_dict)	# 添加新的字典，如新字典与原字典相同的key, 则该key的value会被新字典的value覆盖
	+ dict.setdefault(key, value) # key需要获取的key, value 如key不存在字典, 将会添加key并将value设成默认值

**获取字典的Key和value**
	+ dict.keys()	# 获取字典的所有key, 生成一个为一个伪列表，可以用list转换成列表
	+ dict.values()	# 获取字典的所有value, 生成一个伪列表

	+ dict[key]		# []内传key, 不进行赋值操作, 即为获取
	+ dict.get(key, default = None)	# 如果获取的key不存在, 则直接报错, get如果获取的key不存在, 则返回默认值, 开发中优先使用get函数
		[]和get的区别: []方法key不存在, 报错, get函数key不存在, 则返回默认值

**字典的删除**
	+ dict.clear()	# 清空当前的字典中的所有数据
	+ dict.pop(key)	# 删除字典中指定的key，并将其结果返回，如key不存在则报错
	+ dict.del(key)	# 删除字典中指定的key键
	+ del dict 	# 删除整个字典

**字典的复制**
	+ dict.copy()	# 将当前字典复制到一个新的字典
	
**成员判断**
	+ key in dict	# 判断key是否在字典中
	+ not in 	# 判断key不存在字典中
	+ bool(dict.get(key))	# 判断key是否存在, 当vlaue值为None
```

#### 4. 集合
```python
	+ set.add(item)	# 添加元素，如果集合中已存在则函数不执行
	+ set.update(iterable)	# 加入一个新的集合（或列表，元组，字符串），如新集合内的元素在原集合中存在则无视
	+ set.remove(item)	# 将集合中的某个元素删除，如元素不存在将会报错
	+ set.clear()	# 清空当前集合中的所有元素
	+ del set	# 删除集合
	+ a_set.difference(b_set...)		# 集合的差集
	+ a_set.intersection(b_set...)		# 集合的交集
	+ a_set.union(b_set...)	    	# 集合的并集
	+ a_set.isdisjoint(b_set)		# 判断两个集合是否包含相同的元素, 如果没有返回True, 否则返回False

	+ &, |, ^, -	# 交并补差
```


### （二）自定义函数
```python
def	函数名(arg1, arg2, ...):
	...
	return	# 只能在函数体内使用
# return与print的区别
	print	只是单纯的将对象打印, 不支持赋值语句
	return	是对函数执行结果的返回, 也支持赋值语句

```
函数的传参
> def add(a, b, *args, **kwargs), 参数的定义从左到右依次是 必传参数, 默认参数, 可变元组参数, 可变字典参数, 必传参数与默认参数的传参多样化, 顺序发生变化时, 一定要使用赋值语句进行传参

+ 必传参数
+ 默认参数
+ 不确定参数

1. 必传参数
> 函数中定义的参数没有默认值, 在调用时如果不传入则报错
```python
    def add(a, b):
        return a + b

    result = add(1, 2)
    print(result)
```
2. 默认参数
> 在定义函数的时候, 定义的参数含有默认值, 通过赋值语句给他是默认的值,如果默认参数在调用函数的时候给予了新的值, 函数将优先使用后传入的值进行工作
```python
    def add(a, b=1):
        return a + b

    result = add(1)
    print(result) 
```

3. 不确定参数
> 没有固定的参数名和数量(不知道要传的参数名具体是什么)
```python
    def add(*args, **kwargs):
        ...
    add(1, 2, 3, name = 'dewei', age = 33)
    *args 	# 将无参数的值合并成元组
    **kwargs # 将有参数与默认值的赋值语句合并成字典
```

*******************************************************************

## 四、逻辑判断与流程控制
### (一) if 语句
```python
	if bool_result:
		do
	elif bool_result:
		elifdo
	else:
		elsedo
```

### (二) for 循环
```python
	for item in iterable:	
	# iterable: 可循环的数据类型, 如列表, 元组, 字符串, 字典
	# item: iterable中的每一个元素
		print(item)

	for key, value in items():
		print(key, value)
		# items 无参数
		# key: for循环中获取的字典当前元素的Key
		# value: for循环中对应key的value值
```

### (二) while 循环
```python
	while bool_result:
		do
# 在满足条件下会无限循环，不满足条件后将停止循环
		continue	# 循环遇到continue将停止本次数据循环, 进入下一次循环
		break	# 停止循环（遍历）
```



## 五、类的定义和使用
### (一) 构造函数
```python
# 构造函数的创建(构造函数，放在最前面)
   def __init__(self, a, b):
   self.a = a
   self.b = b
```
### (二) 私有函数和私有变量
> 只希望类业务内部使用, 不希望被使用调用

+ 类内部可以调用私有函数与变量
+ 无法被实例化的对象调用的类中的函数与变量

### (三) 装饰器
还需要去复习
b站视频讲解链接
https://www.bilibili.com/video/BV1SZ4y1s7cv/?spm_id_from=333.337.search-card.all.click&vd_source=ff056e055bec004de28e90a76e649263
CSDN博客链接
https://blog.csdn.net/ncepu_Chen/article/details/106075394

