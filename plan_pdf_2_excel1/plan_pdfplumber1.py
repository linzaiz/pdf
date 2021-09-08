import pdfplumber  # pip install pdfplumber
import pandas as pd

pdf = pdfplumber.open(r"c:\temp\zhiyuan\hb\计划\《2021河北招生计划》物理组.pdf")

for page in pdf.pages[0:2]:
    # page = pdf.pages[0]
    tbl_settings = {
        "vertical_strategy": "text", 
        "horizontal_strategy": "text",
        "explicit_vertical_lines": [],
        "explicit_horizontal_lines": [],
        "snap_tolerance": 3,      # 偏离n像素内的平行线将被捕捉到相同的水平或垂直位置。
        "join_tolerance": 3,       # 同一直线上的两个线段若相距n像素之内则连成一个线段。
        "edge_min_length": 3,     # 短于edge_min_length的边将在尝试重建表之前被丢弃
        "min_words_vertical": 1,    # 2 会造成第6页等最下面两行抓不到。
        "min_words_horizontal": 1,  # 2或3 会造成第一列丢字
        "keep_blank_chars": True,
        "text_tolerance": 3,        # 若下面两个或之一没定义则默认用这个代替。
        #"text_x_tolerance": None,   # 当文本策略搜索单词时，它将期望每个单词中的各个字母横向相差不超过text_tolerance像素。
        #"text_y_tolerance": None,
        "intersection_tolerance": 3,   # 当尝试将线段连结成单元格时，正交边缘必须在intersection_tolerance像素内才认为是相交（单元格的边角）。
        #"intersection_x_tolerance": None,
        #"intersection_y_tolerance": None,
    }

    # pageright = page.within_bbox((297, 70, 595, 841.5))
    # tables = pageright.extract_tables(table_settings=tbl_settings)

    print(page.page_number, page.width, page.height)

    pageleft = page.within_bbox((0, 70, 297.5, 841.5))                   # page.crop(()) 是粗略框一下，压线的字也能抓到。
    tableleft = pageleft.extract_table(table_settings=tbl_settings)
    print(tableleft)
    dfleft = pd.DataFrame(tableleft, columns=tableleft[0])
    print(dfleft)


    pageright = page.within_bbox((297, 70, 595, 841.5))
    tableright = pageright.extract_table(table_settings=tbl_settings)
    print(tableright)


print( "ok?" )