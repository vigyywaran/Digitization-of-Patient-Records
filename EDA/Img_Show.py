import os
import numpy as np
import cv2
cwd = os.getcwd()
folder_path = os.path.join(cwd, "Data_Folder/Data/bills/med_doc_bill_100001_noisy.jpg")
img = cv2.imread(folder_path, cv2.IMREAD_GRAYSCALE)
print (img.shape)