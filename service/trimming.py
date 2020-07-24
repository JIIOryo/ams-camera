import cv2

def trimming(file_: str, top: int, bottom: int, left: int, right: int) -> None:
    img = cv2.imread(file_)
    trimmed_img = img[top : bottom, left: right]
    cv2.imwrite(file_, trimmed_img)
    return
