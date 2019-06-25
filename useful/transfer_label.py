import numpy as np
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
import os
'''
此文件的作用是将voc2012中的彩色标注的标签转换为单通道的标签
'''

classes = ['background', 'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'dining table',
           'dog', 'horse', 'motorbike', 'person', 'potted plant',
           'sheep', 'sofa', 'train', 'tv/monitor']

#VOC2012
colormap = [[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128],
            [128, 0, 128], [0, 128, 128], [128, 128, 128], [64, 0, 0], [192, 0, 0],
            [64, 128, 0], [192, 128, 0], [64, 0, 128], [192, 0, 128],
            [64, 128, 128], [192, 128, 128], [0, 64, 0], [128, 64, 0],
            [0, 192, 0], [128, 192, 0], [0, 64, 128]]
#CamVid
colorcam=[[128, 128, 128],[128, 0, 0],[192, 192, 128],[255, 69, 0],[128, 64, 128],
          [60, 40, 222],[128, 128, 0],[192, 128, 128],[64, 64, 128],[64, 0, 128],
          [64, 64, 0],[0, 128, 192]]


cm2lbl = np.zeros(256 ** 3)
for i, cm in enumerate(colormap):
    cm2lbl[(cm[0] * 256 + cm[1]) * 256 + cm[2]] = i


def image2label(im):
    # 输入为标记图像的矩阵，输出为单通道映射的label图像
    data = im.astype('int32')
    idx = (data[:, :, 0] * 256 + data[:, :, 1]) * 256 + data[:, :, 2]
    return np.array(cm2lbl[idx])


def change_label(label_url, label_name):
    label_img = load_img(label_url)
    label_img = img_to_array(label_img)
    label_img = image2label(label_img)  # 将图片映射为单通道数据
    print(np.max(label_img))
    label_single = Image.fromarray(label_img)
    label_single = label_single.convert('L')
    save_path = '../../../../../mnt/sda1/FangQ/CamVid_label_train'
    save_path = os.path.join(save_path, label_name)  # 确定保存路径及名称
    label_single.save(save_path)

# val_file_path = '../../../../../mnt/sda1/hgl/data/VOC2012/ImageSets/Segmentation/val.txt'  # 文件名存放路径
#
# label_file_path = '../../../../../mnt/sda1/hgl/data/VOC2012/SegmentationClass/'  # 原label存放路径
#
# with open(val_file_path, 'r') as f:
#     file_names = f.readlines()
#     count = 0
#     for name in file_names:
#         count += 1
#         name = name.strip('\n')  # 去掉换行符
#         label_name = name + '.png'  # label文件名
#         label_url = os.path.join(label_file_path, label_name)
#         print('这是第 %s 张' % count)
#         print(label_url) #../../../../../mnt/sda1/hgl/data/VOC2012/SegmentationClass/2007_004052.png
#         change_label(label_url, label_name)


#########start 获取文件路径、文件名、后缀名############
img_file_path='../progect/Tensorflow-SegNet-master/CamVid/list/CamVid_train.txt'
label_file_path='../progect/SS-tuor/CamVid/train_labels/'

def GetName(dir):  #获得后缀为png的文件名，带后缀
    listName = []
    img_list = os.listdir(dir)
    img_list = sorted(img_list)
    for fileName in img_list :
        if os.path.splitext(fileName)[1] == '.png':
            fileName = os.path.splitext(fileName)[0]
            label_name = fileName + '.png'  # label文件名
            listName.append(label_name)
    return listName

#########end 获取文件路径、文件名、后缀名############

file=open(img_file_path, 'r')
i=0
for line in file:
    image_path,label_path = line[:-1].split(' ')
    label_name=label_path[-19:]  #切出图片名称
    print(label_name)
    print(label_path)
    i=i+1
    print('这是第 %s 张' % i)
    change_label(label_path, label_name)


