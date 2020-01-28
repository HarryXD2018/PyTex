# PyTex

## Features

This is a Python package that could generate LaTeX code based on the python object(e.g. List, Numpy Array, CSV table).

## Setup

~~~python
python setup.py install
~~~

To use my package, you need to install the package to the `site_packages` in your python file or virual environment file. 

## Example

~~~python
from pytex4me import *
tex = PyTex()

csv_file = "example.csv"
print(tex.csv_to_tex(csv_file))
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
print(tex.matrix_to_tex(matrix, 'p'))
"""
\begin{pmatrix}
	0& 1\\
	1& 0\\
\end{pmatrix}
"""
~~~

