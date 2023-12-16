import os
import shutil
from imgutils.metrics import ccip_difference



threshold = 0.1
# os.makedirs("split/haha")
ref_images_list = [i.split('.png')[0] for i in os.listdir("ref") if '.png' in i]
dir_list = []
print(ref_images_list)
for i in ref_images_list:
    dir_sample = os.path.join('split', i[:-1])
    dir_list.append(dir_sample)
    try:
        os.makedirs(dir_sample)
    except FileExistsError:
        pass
# print(ccip_difference('images/kushina4.png', 'images/kushina4.png'))

ref_images_list = [os.path.join("ref", i+".png") for i in ref_images_list]
print(ref_images_list)
print(dir_list)

images = os.listdir("images")
for i in images:
    print (i)
    img = os.path.join("images", i)
    for i, ref in enumerate(ref_images_list):
        if (ccip_difference(ref, img)) < threshold:
            destination = os.path.join(dir_list[i], os.path.basename(img))
            print(destination)
            shutil.copy2(img, destination)
            break


# print(ccip_difference('images/pain1.png', 'images/pain2.png'))
# print(ccip_difference('images/pain1.png', 'images/pain3.png'))
# print(ccip_difference('images/pain1.png', 'images/kushina1.png'))
# print(ccip_difference('images/pain2.png', 'images/kushina1.png'))
# print(ccip_difference('images/pain3.png', 'images/kushina1.png'))
