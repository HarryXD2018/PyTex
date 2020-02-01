中文	[English](https://github.com/HarryXD2018/PyTex/blob/master/README_EN.md )

# PyTex

## 特征

这是一个可以将Python中的列表、Numpy类型的二元数组，CSV表格文件转化为Latex代码的Python第三方库。

## 安装

~~~python
python setup.py install
~~~

为了使用`PyTex`库，你需要将文件安装到`site_packages`文件夹中，或者虚拟环境的相应文件夹中。

## 函数介绍

~~~python
csv_to_tex(filedir, hline=True, vline=True, table_style=None)
~~~

根据 `filedir`所给出的CSV文件，打印出对应的Latex代码。在给定`table_style`的合法情况下，优先使用`table_style`，否则使用默认的`hline, vline`的参数。

~~~python
matrix_to_tex(mat, style='p')
~~~

根据给出的二维列表，也可以是二维的Numpy的二维数组，根据`style`的参数（默认为`'p'`）打印出Latex矩阵代码。

~~~python
make_table_by_row(*rows, hline=True, vline=True, table_style=None)
~~~

根据提交的可变长度的参数`rows`制表，**注意**：在函数中的参数`hline`, `vline`和`table_style`若要定义，需要明确声明。



## 实例

~~~python
from pytex4me import *
tex = PyTex()

csv_file = "example.csv"
tex.csv_to_tex(csv_file)
"""
\begin{table}[htbp]
	\centering
	\begin{tabular}{c|c|c|c|c}
	洲& 国家& 省& 市& 县\\
	\hline
	亚洲& 中国& 北京& 北京& 东城\\
	\hline
	北美洲& 墨西哥& & 卡门& \\
	\hline
	\end{tabular}
\end{table}
"""

matrix = [[0, 1], [1, 0]]
tex.matrix_to_tex(matrix, 'p')
"""
\begin{pmatrix}
	0& 1\\
	1& 0\\
\end{pmatrix}
"""

nation = ['US', 'China', 'UK', 'France']
city = ['New York', 'Shanghai', 'London']
tex.make_table_by_row(nation, city)
"""
\begin{table}[htbp]
	\centering
	\begin{tabular}{c|c|c|c}
	US &China &UK &France\\
	\hline
	New York &Shanghai &London &\\
	\hline
	\end{tabular}
\end{table}
"""
~~~

