import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import names

name = []
for i in range(10):
    out = names.get_full_name()
    name.append(out)

nums = np.random.randint(10, 100,10, dtype=int)

df = pd.DataFrame({'Name':name,
                   'Marks':nums})

writer = ExcelWriter('output_file.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
