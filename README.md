# Resize Thumbnail

Resize your thumbnail image for Youtube and Twitter.

----

## Preparation

- Install opencv-python to your environment.
  - `ex.) pip install opencv-python`

----

## Usage

- Run resize_thumbnail.py with thumbnail image file path.
  - `ex.) python resize_thumbnail.py /path/to/source-thumbnail-image.png`

- Then thumbnail images (for Youtube and Twitter) will be generated in the same directory as the original image.

----

## System requirements

- Any environment that runs Python 3.9.x (...maybe).

----

## About this script

- When making thumbnail images in 1080p, the file size often exceeds 2GB and cannot be used on Youtube.
- But it's so sad to resize to 720p after having made it in 1080p.
- So I wrote a script to resize image to just under the upper limit where the file size does not exceed 2GB.

