import cv2
import os
import re
import sys


def get_file_size(source_path: str) -> int:
    if os.path.isdir(source_path):
        raise IOError(f"Source path is directory : {source_path}")
    return os.path.getsize(source_path)

def get_shrink_ratio(source_file_size: int) -> float:
    # Thumbnail size limit for Youtube.
    SIZE_LIMIT = 2 * 1024 * 1024
    
    shrink_ratio = 1.00
    while source_file_size * shrink_ratio > SIZE_LIMIT:
        shrink_ratio -= 0.05
        if shrink_ratio <= 0.25:
            # Source image size is over 8GB...?
            raise Exception(f"Source image is too large: {source_file_size}")
    return shrink_ratio

def resize_image_file(source_image, output_image_path: str, width: int, height: int):
    result_image = cv2.resize(source_image, (int(width), int(height)))
    cv2.imwrite(output_image_path, result_image)


def main(source_image_path: str):
    source_file_size = get_file_size(source_image_path)
    shrink_ratio = get_shrink_ratio(source_file_size)
    source_image = cv2.imread(source_image_path)
    source_image_width = source_image.shape[1]
    source_image_height = source_image.shape[0]
    _, extension = os.path.splitext(source_image_path)
    target_list = [
        ("youtube", source_image_width * shrink_ratio, source_image_height * shrink_ratio),
        ("twitter", 1280, 720),
    ]
    for target, width, height in target_list:
        output_image_path = re.sub(f"{extension}$", f"_{target}{extension}", source_image_path)
        resize_image_file(source_image, output_image_path, width, height)
        print(f"Output resized image: {output_image_path}")


if __name__ == '__main__':
    param = sys.argv
    if len(param) != 2:
        exit("Invalid argument. (Usage: python resize_thumbnail.py /path/to/source-thumbnail-image.png)")
    main(param[1])
    print("Done.")
