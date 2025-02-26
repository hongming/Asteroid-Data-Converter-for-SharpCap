import pandas as pd
import re

# 读取文件
with open('asteroids.txt', 'r') as file:
    lines = file.readlines()

# 初始化列表存储处理后的数据
processed_data = []

# 处理每一行
for line in lines:
    # 使用正则表达式拆分每一行
    match = re.match(r'\((.*?)\)\s+(.*?)\s+([\d\.-]+)\s+([\d\.-]+)\s+\((.*?)\)', line)
    if match:
        # 提取编号
        id_num = match.group(1)
        # 提取名称
        name = match.group(2).strip()
        # 提取RA并转换为小数
        ra = float(match.group(3)) / 15.0
        # 提取DEC
        dec = float(match.group(4))
        
        # 组合为包含6组数据的字符串
        result = f"{id_num}|{name}|Asteroid|{ra}|{dec}||||"
        processed_data.append(result)

# 创建DataFrame
df = pd.DataFrame(processed_data, columns=['Data'])

# 保存为CSV文件
df.to_csv('asteroid_for_sharpcap.csv', index=False, header=['IDs|Names|Type|RA(decimal hours)|Dec(degrees)|VMag|RMax(arcmin)|RMin(arcmin)|PosAngle'])

print("处理完成，结果已保存为asteroid_for_sharpcap.csv")