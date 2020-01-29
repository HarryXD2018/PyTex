import numpy as np
import csv


class PyTexError(Exception):
    def __init__(self, args: str):
        Exception.__init__(self, args)


class PyTex:
    def __init__(self):
        pass

    @staticmethod
    def make_table_by_row(*rows, hline=True):
        max_row_len = 0
        for row in rows:
            if len(row) > max_row_len:
                max_row_len = len(row)
        tex_code = "\\begin{}[htbp]\n" \
                   "\t\\centering\n" \
                   "\t\\begin{}{}\n".format('{table}', '{tabular}', '{' + 'c' * max_row_len + '}')
        for row in rows:
            tex_code += '\t'
            for index in range(0, max_row_len):
                try:
                    tex_code += "{} &".format(str(row[index]))
                except IndexError:
                    tex_code += " &"
            tex_code = tex_code[:-2]
            tex_code += "\\\\\n"
            if hline:
                tex_code += "\t\\hline\n"
        tex_code += "\t\\end{tabular}\n\\end{table}"
        print(tex_code)

    @staticmethod
    def csv_to_tex(file_dir, hline=True):
        csv_file = csv.reader(open(file_dir, 'r', encoding='UTF8'))
        data_item = [row for row in csv_file]
        item_len = len(data_item[0])
        tex_code = "\\begin{}[htbp]\n" \
                   "\t\\centering\n" \
                   "\t\\begin{}{}\n".format('{table}', '{tabular}', '{'+'c' * item_len+'}')
        for row in data_item:
            tex_code += '\t'
            line = "& "
            tex_code += line.join(row)
            if hline:
                tex_code += '\\\\\n\t\\hline\n'
            else:
                tex_code += '\\\\\n'
        tex_code += "\t\\end{tabular}\n\\end{table}"
        print(tex_code)

    def matrix_to_tex(self, mat, style='b'):
        if style not in ['p', 'b', 'V', 'v']:
            raise PyTexError('Style Invalid', )
        else:
            tex_code = "\\begin{}\n".format('{' + style + 'matrix}')
            if isinstance(mat, np.ndarray) and mat.ndim == 2:
                for row in mat:
                    tex_code += '\t'
                    for item in row:
                        tex_code = tex_code + str(item) + '& '
                    tex_code = tex_code[:-2]
                    tex_code = tex_code + '\\\\\n'
                tex_code += "\\end{}\n".format('{' + style + 'matrix}')
                print(tex_code)
            else:
                try:
                    np_mat = np.array(mat)
                    return self.matrix_to_tex(np_mat, style=style)
                except TypeError:
                    raise PyTexError('Format not Matrix')
