import matplotlib.pyplot as plt
import glob
import cv2, os
from label import get_label

def data_gain():
  """

  files : 生成した画像のパスを格納したリスト
  list  : {accession : class(label)}

  """
  files = glob.glob('machine-genome-classification/data/img/*.png')
  #image = cv2.imread(files[0])
  list = get_label('~/sotuken/machine-genome-classification/data/csv/creatures.csv')
  file_list = []
  tmp = []
  label_list = []
  
  for file in files:
    file = os.path.split(file)[1].replace('.png', '')
    tmp.append(file)
    
  num = len(files)
  a = b = c = 0
  

  for n in range(num):

    if tmp[n] not in list:
      continue
    """
    if list[tmp[n]] == 0:
      a = a + 1
        
    if list[tmp[n]] == 1:
      b = b + 1
        
    if list[tmp[n]] == 2:
      c = c + 1
    """
    cls = list[tmp[n]]
    label_list.append(cls)
    file = cv2.imread(files[n])
    file_list.append(file)
    
  return file_list, label_list