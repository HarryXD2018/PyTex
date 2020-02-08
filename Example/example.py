from pytex4me import *

if __name__ == '__main__':
    tex = PyTex()
    # This mode will print the result

    nation = ['US', 'China', 'UK', 'France']
    city = ['New York', 'Shanghai', 'London']
    tex.make_table_by_row(nation, city, vline=False)
    tex.make_table_by_column(nation, city)

    tex_board = PyTex(True)  # If copy_to_clipboard is True, it won't print but copy to clipboard instead.
    matrix = [[0, 1], [1, 0]]
    tex_board.matrix_to_tex(matrix, 'p')
    tex_board.csv_to_tex('example.csv', table_style='c|cccc')
