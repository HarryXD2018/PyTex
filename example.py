from pytex4me import *

if __name__ == '__main__':
    tex = PyTex()
    nation = ['US', 'China', 'UK', 'France']
    city = ['New York', 'Shanghai', 'London']
    tex.make_table_by_row(nation, city)
