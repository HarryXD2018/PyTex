# PyTex

## Features

This is a Python package that could generate LaTeX code based on the python object(e.g. List, Numpy Array, CSV table).

## Setup

~~~python
python setup.py install
~~~

To use my package, you need to install the package to the `site_packages` in your python file or virual environment file. 

## Function Introduction

~~~python
csv_to_tex(filedir, hline=True)
~~~

print correspond latex table code with the givin csv file.

~~~python
matrix_to_tex(mat, style='p')
~~~

print correspond latex matrix code with the two dimensional list.

~~~python
make_table_by_row(*rows)
~~~

print correspond latex table with data given by some rows. 



## Example

~~~python
from pytex4me import *
tex = PyTex()

csv_file = "example.csv"
tex.csv_to_tex(csv_file)
"""
\begin{table}[htbp]
	\centering
	\begin{tabular}{ccccc}
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
	\begin{tabular}{cccc}
	US &China &UK &France\\
	\hline
	New York &Shanghai &London &\\
	\hline
	\end{tabular}
\end{table}
"""
~~~

