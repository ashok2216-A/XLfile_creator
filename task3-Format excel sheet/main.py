import pandas as pd
writer = pd.ExcelWriter('output_file.xlsx', engine='xlsxwriter')

df = pd.DataFrame({'Name': ['E', 'F', 'G', 'H'],
                   'Age': [100, 70, 40, 60]})

df.to_excel(writer, sheet_name="Sheet1", index=False)


workbook = writer.book

worksheet = writer.sheets['Sheet1']

cell_format = workbook.add_format({'bold': True, 'font_color': 'blue'})
cell_format.set_bold()
cell_format.set_font_color('blue')

worksheet.set_column('B:B', None, cell_format)
header_format = workbook.add_format()
header_format.set_font_name('Bodoni MT Black')
header_format.set_font_color('green')
header_format.set_font_size(12)
header_format.set_italic()
header_format.set_underline()

for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

writer.close()