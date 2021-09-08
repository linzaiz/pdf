# YL说stream且指定了columns后，识别得挺好。
import tabula  # pip install tabula-py (带python壳的tabula java app）
import os
                
tables = tabula.read_pdf(r'C:\Users\zhanglin\OneDrive - OTIS Elevator\test\天津\计划\2021\00300003886_f6b2af9a_decrypted.pdf',
                          # pages="all",  # area=[[ 36,788,299,0 ]],
                          # columns=[56.5, 180, 219, 239, 259],
                          #  )
                          stream=True
                        )

#tables = tabula.read_pdf(r'C:\Users\zhanglin\OneDrive - OTIS Elevator\test\天津\计划\2021\00300003886_f6b2af9a_decrypted.pdf',
#                          lattice=True # , stream=True,
#                        )
print(tables)

print(tables[0])
print(tables[0].head(60))


os.system("pause")