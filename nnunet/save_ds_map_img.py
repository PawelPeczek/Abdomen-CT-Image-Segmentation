import numpy as np
import matplotlib.pyplot as plt
#import nibabel as nib

folderPath = "/home/tureckova/Pictures/nnUNet/nnUNet_output/nnUNet/3d_lowres/Task07_Pancreas/nnUNetTrainer__nnUNetPlans/fold_2/ds/"

ds4 = np.load(folderPath+"pancreas_005_ds4.npy")
ds3 = np.load(folderPath+"pancreas_005_ds3.npy")
ds2 = np.load(folderPath+"pancreas_005_ds2.npy")
ds1 = np.load(folderPath+"pancreas_005_ds1.npy")
ds0 = np.load(folderPath+"pancreas_005_ds0.npy")
org = np.load(folderPath+"pancreas_005_org.npy")
#gt = nib.load("/home/tureckova/Pictures/nnUNet/nnUNet_preprocessed/Task07_Pancreas/gt_segmentations/pancreas_005.nii.gz").get_data()

indx = 51
print("Index: {}".format(indx))
print("Im shape: {}".format(org.shape))
print("ATM shape: {}".format(ds4.shape))
ds4_disp1 = ds4[0, indx, :, :]
ds3_disp1 = ds3[0, indx, :, :]
ds2_disp1 = ds2[0, indx, :, :]
ds1_disp1 = ds1[0, indx, :, :]
ds0_disp1 = ds0[0, indx, :, :]
im_disp = org[0, indx, :, :]

plt.subplot(321)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds4_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - top level")
plt.subplot(322)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds3_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - second level")
plt.subplot(323)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds2_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - third level")
plt.subplot(324)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds1_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - fourth level")
plt.subplot(325)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds0_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - fifth level")
plt.savefig(folderPath+"pancreas_005_ds_bgr.png")
plt.clf()

indx = 51
print("Index: {}".format(indx))
print("Im shape: {}".format(org.shape))
print("ATM shape: {}".format(ds3.shape))
ds4_disp1 = ds4[1, indx, :, :]
ds3_disp1 = ds3[1, indx, :, :]
ds2_disp1 = ds2[1, indx, :, :]
ds1_disp1 = ds1[1, indx, :, :]
ds0_disp1 = ds0[1, indx, :, :]
im_disp = org[0, indx, :, :]

plt.subplot(221)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds4_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - top level")
plt.subplot(222)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds3_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - second level")
plt.subplot(223)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds2_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - third level")
plt.subplot(224)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds1_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - fourth level")
# plt.subplot(325)
# plt.imshow(im_disp, cmap='gray')
# plt.imshow(ds0_disp1, cmap='jet', alpha=0.5)
# plt.title("DS map - fifth level")
plt.savefig(folderPath+"pancreas_005_ds_organ.png")
plt.clf()

indx = 51
print("Index: {}".format(indx))
print("Im shape: {}".format(org.shape))
print("ATM shape: {}".format(ds3.shape))
ds4_disp1 = ds4[2, indx, :, :]
ds3_disp1 = ds3[2, indx, :, :]
ds2_disp1 = ds2[2, indx, :, :]
ds1_disp1 = ds1[2, indx, :, :]
ds0_disp1 = ds0[2, indx, :, :]
im_disp = org[0, indx, :, :]

plt.subplot(321)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds4_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - top level")
plt.subplot(322)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds3_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - second level")
plt.subplot(323)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds2_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - third level")
plt.subplot(324)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds1_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - fourth level")
plt.subplot(325)
plt.imshow(im_disp, cmap='gray')
plt.imshow(ds0_disp1, cmap='jet', alpha=0.5)
plt.title("DS map - fifth level")
plt.savefig(folderPath+"pancreas_005_ds_tumor.png")
plt.clf()

