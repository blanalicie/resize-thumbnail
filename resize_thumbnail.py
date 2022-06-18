import cv2
import os
import re
import shutil
import sys


def get_file_size(source_path: str) -> int:
    if os.path.isdir(source_path):
        raise IOError(f"Source path is directory : {source_path}")
    return os.path.getsize(source_path)

def get_extension(source_file_path: str) -> str:
    _, extension = os.path.splitext(source_file_path)
    return extension

def create_output_path(source_image_path: str, target: str) -> str:
    extension = get_extension(source_image_path)
    return re.sub(f"{extension}$", f"_{target}{extension}", source_image_path)

def resize_image_file(source_image_path: str, output_image_path: str, width: int, height: int):
    source_image = cv2.imread(source_image_path)
    source_image_width = source_image.shape[1]
    source_image_height = source_image.shape[0]
    if source_image_width <= width and source_image_height <= height:
        # Resize not required.
        shutil.copy2(source_image_path, output_image_path)
        return
    result_image = cv2.resize(source_image, (int(width), int(height)))
    cv2.imwrite(output_image_path, result_image)

def resize_image_file_for_youtube(source_image_path: str, output_image_path: str):
    # Thumbnail size limit for Youtube.
    SIZE_LIMIT = 2 * 1024 * 1024
    image_file_size = get_file_size(source_image_path)
    if image_file_size <= SIZE_LIMIT:
        # Resize not required.
        shutil.copy2(source_image_path, output_image_path)
        return
    
    # Image file info...
    source_image = cv2.imread(source_image_path)
    source_image_width = source_image.shape[1]
    source_image_height = source_image.shape[0]
    source_image_extension = get_extension(source_image_path)

    # Prioritize keeping image size large over than compression level low.
    compress_flag = [ cv2.IMWRITE_PNG_COMPRESSION, 9 ] if source_image_extension.lower() == ".png" else None

    # Get file size by actually resizing.
    tmp_image_path = f"{output_image_path}.tmp.png"
    try:
        shrink_ratio = 1.00
        while image_file_size > SIZE_LIMIT:
            shrink_ratio -= 0.05
            if shrink_ratio <= 0.25:
                # Source image size is over 8GB...?                
                raise Exception(f"Source image is too large: {image_file_size}")
            result_image = cv2.resize(source_image, (int(source_image_width * shrink_ratio), int(source_image_height * shrink_ratio)))
            cv2.imwrite(tmp_image_path, result_image, compress_flag)
            image_file_size = get_file_size(tmp_image_path)
        shutil.move(tmp_image_path, output_image_path)
    finally:
        if os.path.exists(tmp_image_path):
            os.remove(tmp_image_path)


def main(source_image_path: str):
    resize_image_file_for_youtube(source_image_path, create_output_path(source_image_path, "youtube"))
    resize_image_file(source_image_path, create_output_path(source_image_path, "twitter"), 1280, 720)


if __name__ == '__main__':
    param = sys.argv
    if len(param) != 2:
        exit("Invalid argument. (Usage: python resize_thumbnail.py /path/to/source-thumbnail-image.png)")
    main(param[1])
    print("Done.")
