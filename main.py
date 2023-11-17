import torch

# 定义第一个矩阵的维度
dim1 = (20, 6, 90, 90)
# 定义第二个矩阵的维度
dim2 = (20, 90, 90)

# 随机生成两个矩阵
matrix1 = torch.rand(dim1)
matrix2 = torch.rand(dim2)
matrix2 = torch.unsqueeze(matrix2,1)

# 矩阵相乘
result = torch.matmul(matrix1, matrix2)

# 输出结果的维度
print(result.size())