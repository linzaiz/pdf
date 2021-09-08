# OK!  camelot比pdfplumber更多选项。 但pdfplumber有提前文本等功能。
import camelot
import os
# anaconda prompt> activate venv1     conda install -c conda-forge camelot-py 或别确认，挑出tk、ghostscript、opencv-python【cv2】、camelot-py用pip安装

#能运行，参数还得调： tables = camelot.read_pdf(r'C:\tmp\2021物.pdf', flavor='stream', pages="1" , table_areas=[ '0,788,299,0' ]) # table区域之一'x0,y0,x1,y1'
#OK: tables = camelot.read_pdf(r"C:\Users\zhanglin\OneDrive - OTIS Elevator\测试pdf中识表.pdf", flavor='stream')  # flavor='lattice')要求安装ghostscript exe
#print(tables)
#print(tables[0].df)

#tables = camelot.read_pdf(r'C:\tmp\2021物.pdf', flavor='stream', pages="6", table_areas=[ '36,788,299,0', '300,788,585,0' ],
#                          row_tol=10.0, column_tol=0, strip_text=' ', columns=['56.5, 180, 219, 239, 259', '328.5, 452, 491, 511, 531'],
#                          layout_kwargs={'word_margin': 0.03, 'char_margin': 0.1, 'line_margin':2, 'detect_vertical': True}   # 'line_margin'行距大于此则分段。这三个参数是pdfminer.six的。
#                         ) # table区域之一'x0,y0,x1,y1'。 
                           # , split_text默False 跨cells的连续词是否分开。 , column_tol=2,
                           # , edge_tol=50 default50
                           # row_tol=10默2, word_margin默0.1, char_margin默2 对HB_plan很关键。   column_tol=3默0，line_margin默0.5没起作用. 
                           # layout_kwargs line_overlap默0.5 判断是否在同一行；char_margin默2 超过时判断为不同块(trunks),小于则算连续字符序列。详见笔记“PDF高级识别”
#                          # ,layout_kwargs 'char_margin' 'word_margin': 都是字符宽度的比。https://pdfminersix.readthedocs.io/en/latest/reference/composable.html
#                          #  传给pdfminer: , layout_kwargs={'detect_vertical': False}是否考虑纵向文本。                          
#                          
tables = camelot.read_pdf(r'C:\Users\zhanglin\OneDrive - OTIS Elevator\test\天津\计划\2021\00300003886_f6b2af9a_decrypted.pdf',
                          flavor='stream', pages="4",  # table_areas=[ '36,788,299,0', '300,788,585,0' ],
                          # columns=['56.5, 180, 219, 239, 259', '328.5, 452, 491, 511, 531'],
                          row_tol=10, layout_kwargs={'word_margin': 0.05, 'char_margin': 0.3} )
print(tables)

print(tables[0].df)
print(tables[0].df.head(60))


os.system("pause")