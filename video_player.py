#-*- coding:utf-8 -*-
import cv2
from Image_processer import CirclesAndSquares

file_path = "/Users/madao/Documents/tracking/demo_video.mp4"

# 動画の読み込み
cap = cv2.VideoCapture(file_path)
circles_and_squares = CirclesAndSquares(threshold=50)

# 動画終了まで繰り返し
while True:
    circles_and_squares.reset_object_coordinates()
    # フレームを取得
    ret, frame = cap.read()
    if frame is None:
        break
    gray = cv2.GaussianBlur(frame, (33, 33), 1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    circles = circles_and_squares.get_center_of_circle(gray)
    squares = circles_and_squares.get_center_of_square(gray)

    circles_and_squares.draw_circles_and_save_center_point(circles, frame)
    circles_and_squares.draw_square_and_save_center_point(squares, frame)
    circles_and_squares.reset_bIn()
    new_tgts = circles_and_squares.get_new_center_points()
    circles_and_squares.update_center_points(new_tgts)

    # フレームを表示
    cv2.imshow("Frame", frame)
    # qキーが押されたら途中終了
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

circle_num = circles_and_squares.circle_counter
square_num = circles_and_squares.square_counter
print(circle_num, " circles, ", square_num, " rectangles")
cv2.destroyAllWindows()
