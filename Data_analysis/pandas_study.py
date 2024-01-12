#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

data = {
    '语文': [90, 98, 87, 90],
    '数学': [92, 87, 90, 98]
}

df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
yuwen_series = df['语文']
max_yuwen = yuwen_series.max()  # 语文最高分
print('语文最高分{max_score}'.format(max_score=max_yuwen))

# 创建出总分列, 由每一行的语文和数学分数相加
df['总分'] = df['语文'] + df['数学']
max_sum = df['总分'].max()

stu_name = df['总分'].idxmax()
print('{stu}总分最高, {score}'.format(stu=stu_name, score=max_sum))
# pd.read_sql()


df.index.name = '姓名'
df.columns.name = '科目'

print(type(df.values))
print(df.values)
print(df.values[0][0])

for col in df:
    print(col, df[col])
for k,v in df.iteritems():
    print(k,v)