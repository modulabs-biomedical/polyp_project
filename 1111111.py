import glob
import os

# filenameList= [k.split('/')[-1].split('.')[0] for k in glob.glob(os.path.join(self.img_root, '*.bmp'))]

for k in glob.glob(os.path.join('bbdd/', '*.bmp')):
    aa = k.split('\\')[-1].split('.')[0]
    print(aa)

# shuffle(filenameList)

# nSamples = len(filenameList)
# nTraining = int(fraction_value*nSamples)
# nValidation = int((1-fraction_value)*nSamples)
# 
# dirs = [self.img_root, self.gt_root]
# for index in range(nTraining):
#     for d in dirs:
#         srcFilename = os.path.join(d, filenameList[index] + '.bmp')
#         dstFilename = os.path.join(d, 'train_' + filenameList[index]+ '.bmp')
#         shutil.move(srcFilename, dstFilename)