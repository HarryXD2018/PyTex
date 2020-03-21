[中文](https://github.com/HarryXD2018/PyTex/blob/master/README.md)	English

# PyTex

## Features

This is a Python package that could generate LaTeX code based on the python object(e.g. List, Numpy Array, CSV table). While using the package in script mode or dragging a csv file or picture in the command mode, the program will generate the Tex code as return. If necessary, the Tex code can be copied automatically. 

## Setup

~~~python
python setup.py install
~~~

To use my package, you need to install the package to the `site_packages` in your python file or virual environment file. 

## Function Introduction

~~~python
csv_to_tex(filedir, hline=True, vline=True, table_style=None)
~~~

print correspond latex table code with the givin csv file.

~~~python
matrix_to_tex(mat, style='p')
~~~

print correspond latex matrix code with the two dimensional list.

~~~python
make_table_by_row(*rows, hline=True, vline=True, table_style=None)
~~~

print correspond latex table with data given by some rows. 



## Example

~~~python
from pytex4me import *
tex = PyTex()

csv_file = "example.csv"
tex.csv_to_tex(csv_file)
"""
Output:

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
Output:

\begin{pmatrix}
	0& 1\\
	1& 0\\
\end{pmatrix}
"""

nation = ['US', 'China', 'UK', 'France']
city = ['New York', 'Shanghai', 'London']
tex.make_table_by_row(nation, city)
"""
Output:

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

Check file `Example` for further detail. 