import os
import sys
from PIL import Image
from resizeimage import resizeimage

if len(sys.argv) < 2:
    print("input folder as parameter!")
    exit(0)

to_del = []
base = f'{sys.argv[1]}/'
start_num = int(sys.argv[2]) if len(sys.argv) > 2 else 0
for i, path in enumerate(os.listdir(base)):
    full_path = os.path.join(base, path)
    with Image.open(full_path) as image:
        if image.size[0] < 224 or image.size[1] < 224:
            print(f"Small pic: {full_path}")
            #os.remove(full_path)
            to_del.append(full_path)
            continue

        ending = str(start_num+i) + ".jpg"
        path_to_save = os.path.join(base, ending)
        to_del.append(full_path)
        cover = resizeimage.resize_cover(image, [224, 224])
        cover.save(path_to_save, image.format)

for path in to_del:
    os.remove(path)

print("Done :)")