from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image
from torchvision import transforms

# tensorboard --logdir=logs --port=6006

# https://github.com/zergtant/pytorch-handbook/blob/master/chapter4/4.2.2-tensorboardx.ipynb

# demo01
writer = SummaryWriter("logs")
image_path = "../imagelib/img/lena.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

writer.add_image("train", img_array, 1, dataformats='HWC')
# y = 2x
for i in range(100):
    writer.add_scalar("y=2x", 2 * i, i)

# demo02
img = Image.open(image_path)

# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)

# Normalize
print(img_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])

writer.add_image("Normalize", img_norm)
# writer.add_image("Normalize", img_norm,2)

writer.close()