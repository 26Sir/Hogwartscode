import pandas as pd

# 读取 Excel 表格
df_A = pd.read_excel('C:\\Users\\Administrator\\Desktop\\test\\AAA.xlsx', sheet_name='Sheet1')
df_B = pd.read_excel('C:\\Users\\Administrator\\Desktop\\test\\BBB.xlsx', sheet_name='Sheet1')

# 执行计算
df_C = df_A['A'] + df_B['B']

# 将结果输出至 C 表格
df_C.to_excel('C.xlsx', index=False)