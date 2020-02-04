import numpy as np
import csv
import pyperclip


class PyTexError(Exception):
    def __init__(self, exp_args: str):
        Exception.__init__(self, exp_args)


class PyTex:
    def __init__(self, copy_to_clipboard=False):
        self.copy_to_clipboard = copy_to_clipboard

    def check_table_style(self, table_style: str, item_len):
        if table_style is None:
            return False
        return table_style.count("c") + table_style.count("|") == len(table_style)and item_len == table_style.count("c")

    @staticmethod
    def make_table_by_column(*column, hline=True):
        pass

    def make_table_by_row(self, *rows, caption=None, hline=True, vline=True, table_style=None):
        max_row_len = 0
        for row in rows:
            if len(row) > max_row_len:
                max_row_len = len(row)
        if not self.check_table_style(table_style, max_row_len):
            if vline:
                table_style = "|".join("c"*max_row_len)
            else:
                table_style = "c" * max_row_len
        tex_code = "\\begin{}[htbp]\n" \
                   "\t\\centering\n" \
                   "\t\\begin{}{}\n".format('{table}', '{tabular}', '{' + table_style + '}')
        for row in rows:
            tex_code += '\t'
            for index in range(0, max_row_len):
                try:
                    tex_code += "{}& ".format(str(row[index]))
                except IndexError:
                    tex_code += "& "
            tex_code = tex_code[:-2]
            tex_code += "\\\\\n"
            if hline:
                tex_code += "\t\\hline\n"
        if caption is None:
            tex_code += "\t\\end{tabular}\n\t%\\caption{}\n\\end{table}"
        else:
            tex_code += "\t\\end{}\n\t\\caption{}\n\\end{}".format("{tabular}", "{" + caption + "}", "{table}")
        if self.copy_to_clipboard:
            if pyperclip.paste() is not None:
                print("Warning: The content in clipboard will be replaced")
            pyperclip.copy(tex_code)
            print("Code is copied")
        else:
            print(tex_code)

    def csv_to_tex(self, file_dir, caption=None, hline=True, vline=True, table_style=None):
        csv_file = csv.reader(open(file_dir, 'r', encoding='UTF8'))
        data_item = [row for row in csv_file]
        item_len = len(data_item[0])
        if not self.check_table_style(table_style, item_len):
            if vline:
                table_style = "|".join("c"*item_len)
            else:
                table_style = "c"*item_len
        tex_code = "\\begin{}[htbp]\n" \
                   "\t\\centering\n" \
                   "\t\\begin{}{}\n".format('{table}', '{tabular}', '{'+table_style+'}')
        for row in data_item:
            tex_code += '\t'
            tex_code += "& ".join(row)
            if hline:
                tex_code += '\\\\\n\t\\hline\n'
            else:
                tex_code += '\\\\\n'
        if caption is None:
            tex_code += "\t\\end{tabular}\n\t\\%caption{}\n\\end{table}"
        else:
            tex_code += "\t\\end{tabular}\n" + "\t\\caption{}\n".format("{" + caption + "}") + "\\end{table}"
        if self.copy_to_clipboard:
            if pyperclip.paste() is not None:
                print("Warning: The content in clipboard will be replaced")
            pyperclip.copy(tex_code)
            print("Code is copied")
        else:
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
                if self.copy_to_clipboard:
                    if pyperclip.paste() is not None:
                        print("Warning: The content in clipboard will be replaced")
                    pyperclip.copy(tex_code)
                    print("Code is copied")
                else:
                    print(tex_code)
            else:
                try:
                    np_mat = np.array(mat)
                    return self.matrix_to_tex(np_mat, style=style)
                except TypeError:
                    raise PyTexError('Format not Matrix')

    @staticmethod
    def pic_insert(file_dir, caption=None, scale=None):
        tex_code = "\\begin{figure}[htbp]\n\t\\centering\n"
        if scale is None:
            tex_code += "\t\\scalebox{1}{\\includegraphics[width=.8\\textwidth]" + "{" + file_dir + "}\n"
        else:
            tex_code += "\t\\scalebox{{" + scale + "}}{\\includegraphics[width=.8\\textwidth]{{" + file_dir + "}}}\n"
        if caption is not None:
            tex_code += "\t\\caption{}\n".format("{"+caption+"}")
        else:
            tex_code += "\t%\\caption{}\n"
        tex_code += "\\end{figure}"
        print(tex_code)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file_dir', type=str)
    args = parser.parse_args()
    print(args.file_dir)
    args.file_dir: str
    file_name = args.file_dir[args.file_dir.rfind(u"\\") + 1:args.file_dir.rfind(u".")]
    file_type = args.file_dir[args.file_dir.rfind(u".") + 1:]
    if file_type == 'csv':
        tex = PyTex()
        tex.csv_to_tex(file_dir=args.file_dir, caption=file_name)
    elif file_type in ['jpg', 'jpeg', 'png', 'JPG', 'PNG', 'JPEG', 'eps']:
        tex = PyTex()
        tex.pic_insert(file_dir=args.file_dir, caption=file_name)
