from io import BytesIO

from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import numpy

from PIL import Image

config_file = 'model/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'model/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')


def main(input_bytes):
    image_path = 'input_photo.jpg'
    input_image = Image.open(BytesIO(input_bytes))
    input_image.save(image_path)

    result = inference_detector(model, image_path)
    res = model.show_result(image_path, result, score_thr=0.3, show=False, wait_time=0,
                            win_name='result', bbox_color=(72, 101, 241),
                            text_color=(72, 101, 241))
    
    res_img = Image.fromarray(res[:,:,::-1])

    output_bytes_buff = BytesIO()
    res_img.save(output_bytes_buff, format='png')
    output_bytes = output_bytes_buff.getvalue()

    return output_bytes
