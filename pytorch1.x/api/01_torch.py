import torch
# 创建Tensor
x = torch.empty(5, 3) # 创建一个5x3的未初始化的Tensor
print(x)

x = torch.zeros(5, 3, dtype=torch.long) # 创建一个5x3的long型全0的Tensor
print(x)

x = torch.eye(5, 3) # 对角线为1，其他为0
print(x)

x = torch.tensor([5.5, 3]) # 直接根据数据创建
print(x)

# 还可以通过现有的Tensor来创建，此方法会默认重用输入Tensor的一些属性，例如数据类型，除非自定义数据类型。
x = torch.randn_like(x, dtype=torch.float) # 指定新的数据类型,未初始化
print(x)

x = x.new_ones(5, 3, dtype=torch.float64)  # 返回的tensor默认具有相同的torch.dtype和torch.device
print(x)
# 我们可以通过shape或者size()来获取Tensor的形状
print(x.size()) # torch.Size([5, 3])
print(x.shape) # torch.Size([5, 3])


print('-----------------------------')
print(torch.rand(5, 3)) # 创建一个5x3的随机初始化的Tensor  随机样本位于[0, 1)均匀分布中
print(torch.Tensor(5,3).uniform_(0,1)) # 均匀分布

x1 = torch.randn(5, 3)
print(x1) # 标准正态分布中的样本,从标准正态分布（均值为0，方差为1，即高斯白噪声）中抽取的一组随机数。
x2 = torch.normal(0, 1, (5,3)) # torch.Tensor(5,3).normal_
print(x2) # 正态分布中的样本, 指定均值means和标准差std的离散正态分布中抽取的一组随机数。

print(x1.mean(), x2.mean())
print('-----------------------------')

print(torch.arange(0, 12, 2)) # 从s到e，步长为step tensor([ 0,  2,  4,  6,  8, 10])
print(torch.linspace(0, 12, 3)) # 从s到e，均匀切分成steps份   tensor([ 0.,  6., 12.])

print(torch.randperm(10)) # 把1到10这些数随机打乱得到的一个数字序列。


print('-----------------------------')

# y1 = tensor @ tensor.T
# y2 = tensor.matmul(tensor.T) #matmul可以进行张量乘法, 输入可以是高维
# tensor.mm只能进行矩阵乘法,也就是输入的两个tensor维度只能是(n×m)和(m×p)
# tensor.bmm是两个三维张量相乘, 两个输入tensor维度是(b×n×m)和(b×m×p), 第一维b代表batch size，输出为(b×n×p)

# z1 = tensor * tensor
# z2 = tensor.mul(tensor)


