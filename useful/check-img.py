import os
'''
此文件的作用是检测是否有损坏的jpg图片并找到它
'''
train_dir = '../progect/mytest/dataset/images/val/'

def progress(percent, width=50):
    '''进度打印功能'''
    if percent >= 100:
        percent = 100

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    print('\r%s %d%% ' % (show_str, percent), end='')

def is_valid_jpg(jpg_file):
    with open(jpg_file, 'rb') as f:
        f.seek(-2, 2)
        buf = f.read()
        f.close()
        return buf ==  b'\xff\xd9'  # 判定jpg是否包含结束字段

data_size = len([lists for lists in os.listdir(train_dir) if os.path.isfile(os.path.join(train_dir, lists))])
recv_size = 0
incompleteFile = 0
print('file tall : %d' % data_size)

for file in os.listdir(train_dir):
    if os.path.splitext(file)[1].lower() == '.png':
        ret = is_valid_jpg(train_dir + file)
        if ret == False:
            incompleteFile = incompleteFile + 1
            print('损坏的文件名称是：',file)
            #os.remove(train_dir + file)

    recv_per = int(100 * recv_size / data_size)
    progress(recv_per, width=30)
    recv_size = recv_size + 1

progress(100, width=30)
print('\nincomplete file : %d' % incompleteFile)
