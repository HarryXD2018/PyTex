from pytex4me import *
import pandas as pd

if __name__ == '__main__':
    tex = PyTex()
    # This mode will print the result

    df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['one', 'two', 'thr'], columns=list('abcd'))
    tex.raw_tex(df)

    # table = [['Team1', 'Tom', 'Jack'], ['Team2', 'Lucy', 'Anne'], ['Team3', 'Joe']]
    # tex.raw_tex(table)

    # nation = ['US', 'China', 'UK', 'France']
    # city = ['New York', 'Shanghai', 'London']
    # tex.make_table_by_row(nation, city, vline=False)
    # tex.make_table_by_column(nation, city)
    # tex.code_insert("example.py", high_light=True, language='py')

    # tex_board = PyTex(True)  # If copy_to_clipboard is True, it won't print but copy to clipboard instead.
    # matrix = [[0, 1], [1, 0]]
    # tex_board.matrix_to_tex(matrix, 'p')
    # tex_board.csv_to_tex('example.csv', table_style='c|cccc')
