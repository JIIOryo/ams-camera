import cv2

def trimming(input_path: str, output_path: str, top: int, bottom: int, left: int, right: int) -> None:
    img = cv2.imread(input_path)
    trimmed_img = img[top : bottom, left: right]
    cv2.imwrite(output_path, trimmed_img)
    return
