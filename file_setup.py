# This python file is repsonsible for setting up the entire directory for Tensorflow Model Zoo
import os

Custom_Model_Name = 'my_ssd_mobnet'
Pretrained_Model_Name = 'ssd_mobilenet_v2_fpnlite_320X320_coco17_tpu-8'
Pretrained_Model_URL = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz'
TF_Record_Script_Name = 'generate_tfrecord.py'
Label_Map_Name = 'label_map.pbtxt'

paths = {
    'Model_Training_Path': os.path.join('.', 'Model_Training'),
    'Scripts_Path' : os.path.join('.', 'Scripts'),
    'API_Model_Path' : os.path.join('.', 'APIModels'),
    'Annotation_Path' : os.path.join('.', 'Model_Training', 'Annotations'),
    'Images_Path' : os.path.join('.', 'Model_Training', 'Images'),
    'Model_Path' : os.path.join('.', 'Model_Training', 'Models'),
    'Pretrained_Model_Path' : os.path.join('.', 'Model_Training', 'Pre-trained-models'),
    'Checkpoint_Path' : os.path.join('.', 'Model_Training', 'Models', Custom_Model_Name),
    'Output_Path' : os.path.join('.', 'Model_Training', 'Models', Custom_Model_Name, 'export'),
    'TFJS_Path' : os.path.join('.', 'Model_Training', 'Models', Custom_Model_Name, 'tfjsexport'),
    'TFLite_Path' : os.path.join('.', 'Model_Training', 'Models', Custom_Model_Name, 'tfliteexport'),
    'Protoc_Path' : os.path.join('.', 'Protoc')
}

files = {
    'Pipeline_Config' : os.path.join('.', 'Model_Training', 'Models', Custom_Model_Name, 'pipeline.config'),
    'TF_Record_Script' : os.path.join(paths['Scripts_Path'], TF_Record_Script_Name),
    'Labelmap' : os.path.join(paths['Annotation_Path'], Label_Map_Name)
}

for path in paths.values():
    if not os.path.exists(path):
        os.mkdir(path)