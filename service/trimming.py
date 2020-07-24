import cv2

def trimming(file: str, top: int, bottom: int, left: int, right: int) -> None:
    img = cv2.imread(file)
    trimmed_img = img[top : bottom, left: right]
    cv2.imwrite(file, trimmed_img)
    return
