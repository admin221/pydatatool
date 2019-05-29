annotation_path = "/home/all/datasets/caltech/extract/train03_new/set04_V003_I01376.txt"

import pydatatool as pdt

# anno = pdt.caltech.load_txt(annotation_path)
# param = pdt.caltech.get_default_filter()
# anns, annId, objId = pdt.caltech.txt2coco(4,3,1376,anno)

pth = "/home/all/datasets/caltech/extract/train03_new"
annotations_train_10x, image_ids_train, annId_str, objId_str = pdt.caltech.txts2cocos(pth,0,0,{})
pdt.scut.save_coco(annotations_train_10x,image_ids_train,'../output/json/caltech_train_10x_new.json')


pth = "/home/all/datasets/caltech/extract/test_1x_new"
annotations_test_1x, image_ids_test, annId_str, objId_str = pdt.caltech.txts2cocos(pth,annId_str,objId_str,{})
pdt.scut.save_coco(annotations_test_1x,image_ids_test,'../output/json/caltech_test_1x_new.json')
