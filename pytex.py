import numpy as np
import csv


class PyTexError(Exception):
    def __init__(self, args):
        Exception.__init__(self, args)


class PyTex:
    def __init__(self):
        pass

    def make_table(self, *rows):
        pass

    def csv_to_tex(self, file_dir, hline=True):
        csv_file = csv.reader(open(file_dir, 'r', encoding='UTF8'))
        data_item = [row for row in csv_file]
        item_len = len(data_item[0])
        tex_code = "\\begin{}[htbp]\n\t\\centering\n\t\\begin{}{}\n".format('{table}', '{tabular}', '{'+'c' * item_len+'}')
        for column in data_item:
            tex_code += '\t'
            for index in range(0, len(column) - 1):
                tex_code = tex_code + str(column[index]) + '& '
            if hline:
                tex_code += str(column[len(column) - 1]) + '\\\\\n\t\\hline\n'
            else:
                tex_code += str(column[len(column) - 1]) + '\\\\\n'
        tex_code += "\t\\end{tabular}\n\\end{table}"
        return tex_code

    def make_matrix(self, mat, style='b'):
        if style not in ['p', 'b', 'V', 'v']:
            err = "Style Invalid"
            raise PyTexError(err)
        else:
            tex_code = "\\begin{}\n".format('{' + style + 'matrix}')
            if isinstance(mat, np.ndarray) and mat.ndim == 2:
                for column in mat:
                    tex_code += '\t'
                    for item in column:
                        tex_code = tex_code + str(item) + '& '
                    tex_code = tex_code[:-2]
                    tex_code = tex_code + '\\\\\n'
                tex_code += "\\end{}\n".format('{' + style + 'matrix}')
                return tex_code.rstrip()
            else:
                try:
                    np_mat = np.array(mat)
                    return self.make_matrix(np_mat, style=style)
                except TypeError as e:
                    err = "Format not Matrix"
                    raise PyTexError(err)


if __name__ == '__main__':
    table = PyTex()
    array = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
    array_1 = [[1, 1], [1, 1], [1, 1], [1, 1]]
    print(table.csv_to_tex(r'C:\Users\chenh\Desktop\Location_detector\trail_data.csv', True))
    # for style in ['p', 'b', 'V', 'v']:
    #     print(table.make_matrix(array_1, style=style))

