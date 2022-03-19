from cv2 import inRange, waitKey
import numpy as np
import cv2
import time

# 시작하는 시간과 끝나는 시간 각각 찍은다음에 차이로 동작시간 체크
start_time = time.time()


image = cv2.imread('./img/451.png')

# 색상별 RGB 값
# 빨간색 검출
redLower = np.array([0,0,139])
redUpper = np.array([60 ,34,255])

# 주황색 검출
orangeLower = np.array([0,60,255])  
orangeUpper = np.array([80, 215, 255])

# 노랑색 검출
yellowLower = np.array([0,51,51])  
yellowUpper = np.array([204, 255, 255])

# 분홍색 검출
pinkLower = np.array([133,20,199])  
pinkUpper = np.array([203, 192, 255])

# 초록색 검출
greenLower = np.array([0,100,0])  
greenUpper = np.array([152, 255, 152])

# 파랑색 검출
blueLower = np.array([112,0,0])  
blueUpper = np.array([255, 248, 240])

# 보라색 검출
purpleLower = np.array([128,0,75])  
purpleUpper = np.array([255, 230, 255])

# 검정색 검출
blackLower = np.array([0,0,0])  
blackUpper = np.array([105, 105, 105])

# 회색 검출
greyLower = np.array([105,105,105])  
greyUpper = np.array([220, 220, 220])

# 갈색 검출
brownLower = np.array([0,0,128])  
brownUpper = np.array([220, 248, 253])




# 색상 비율담은 이미지 배열을 담을 배열
# img_ratio_list = list()

# # 이미지 폴더의 이미지들 전체를 돌면서 이미지당 색상 비율을 검출하고
# # 전체 이미지에 대한 색상 비율을 검출
# for i in range (1,501):
#     print(i)
#     # 이미지를 읽는다
#     imaeg = cv2.imread('./img/'+str(i)+'.png')
#     # 색상별 비율 담을 리스트 선언
#     # color_ratio = list()
#     color_ratio = list()
#     # 빨강색 검출
#     img_mask = cv2.inRange(image,redLower,redUpper)
#     ratio_red = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_red)

#     # 주황색 검출
#     img_mask = cv2.inRange(image,redLower,redUpper)
#     ratio_orange = cv2.countNonZero(img_mask)/(image.size/3)
    
#     color_ratio.append(ratio_orange)
    

#     # 노랑색 검출
#     img_mask = cv2.inRange(image,yellowLower,yellowUpper)
#     ratio_yellow = cv2.countNonZero(img_mask)/(image.size/3)
    
#     color_ratio.append(ratio_yellow)

#     # 분홍색 검출
#     img_mask = cv2.inRange(image,pinkLower,pinkUpper)
#     ratio_pink = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_pink)

#     # 초록색 검출
#     img_mask = cv2.inRange(image,greenLower,greenUpper)
#     ratio_green = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_green)

#     # 파랑색 검출
#     img_mask = cv2.inRange(image,blueLower,blueUpper)
#     ratio_blue = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_blue)

#     # 보라색 검출
#     img_mask = cv2.inRange(image,purpleLower,purpleUpper)
#     ratio_purple = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_purple)

#     # 검정색 검출
#     img_mask = cv2.inRange(image,blackLower,blackUpper)
#     ratio_black = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_black)

#     # 회색 검출
#     img_mask = cv2.inRange(image,greyLower,greyUpper)
#     ratio_grey = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_grey)

#     # 갈색 검출
#     img_mask = cv2.inRange(image,brownLower,brownUpper)
#     ratio_brown = cv2.countNonZero(img_mask)/(image.size/3)

#     color_ratio.append(ratio_brown)

#     img_ratio_list.append(color_ratio)


# # print(img_ratio_list)
# totla_ratio_sum = sum(img_ratio_list, [])

# print(totla_ratio_sum)

# total_sum_np = np.array(totla_ratio_sum)

# print(total_sum_np/50)
# # totla_ratio = totla_ratio_sum/500

# # print(totla_ratio)
# # 끝나는 시간
# end_time = time.time()

# print(end_time - start_time)





# def filterColor(color):
#     Lower = color+'Lower'
#     Upper = color+'Upper'
#     print(Lower)
#     print(Upper)

#     img_mask = cv2.inRange(image, Lower, Upper)
#     print(color + "Lower")
#     ratio = cv2.countNonZero(img_mask)/(image.size/3)
#     print(color+' pixel percentage:', np.round(ratio*100, 2))

#     result = cv2.bitwise_and(image, image, mask=img_mask) # 원본 이미지와 마스크를 합성


#     cv2.imshow('result',result)
#     waitKey(0)

# filterColor('red')



# # 색상 검출

bgrLower = np.array([0, 0, 139]) # 추출할 색의 하한(BGR) 
bgrUpper = np.array([60,34,255]) # 추출할 색의 상한(BGR)

# inRage(검사할 이미지, 하한값, 상한값) : 검사 할 이미지가 하한값과 상한값 사이에 들어오면 흰색 아니면 검은색으로 표시
img_mask = cv2.inRange(image, brownLower, brownUpper) # BGR로 부터 마스크를 작성

ratio_orange = cv2.countNonZero(img_mask)/(image.size/3)
print('orange pixel percentage:', np.round(ratio_orange*100, 2))

result = cv2.bitwise_and(image, image, mask=img_mask) # 원본 이미지와 마스크를 합성

resize_img = cv2.resize(result,(300,300))

cv2.imshow('result',resize_img)
waitKey(0)


# # 파란색 검출
# bgrLower = np.array([112,0,0]) # 추출할 색의 하한(BGR) 
# bgrUpper = np.array([255, 248, 240]) # 추출할 색의 상한(BGR)

# # inRage(검사할 이미지, 하한값, 상한값) : 검사 할 이미지가 하한값과 상한값 사이에 들어오면 흰색 아니면 검은색으로 표시
# img_mask = cv2.inRange(image, bgrLower, bgrUpper) # BGR로 부터 마스크를 작성

# ratio_orange = cv2.countNonZero(img_mask)/(image.size/3)
# print('blue pixel percentage:', np.round(ratio_orange*100, 2))

# result = cv2.bitwise_and(image, image, mask=img_mask) # 원본 이미지와 마스크를 합성


# cv2.imshow('result',result)
# waitKey(0)


# # 갈색 검출
# bgrLower = np.array([0,0,128]) # 추출할 색의 하한(BGR) 
# bgrUpper = np.array([220, 248, 253]) # 추출할 색의 상한(BGR)

# # inRage(검사할 이미지, 하한값, 상한값) : 검사 할 이미지가 하한값과 상한값 사이에 들어오면 흰색 아니면 검은색으로 표시
# img_mask = cv2.inRange(image, bgrLower, bgrUpper) # BGR로 부터 마스크를 작성

# ratio_orange = cv2.countNonZero(img_mask)/(image.size/3)
# print('brown pixel percentage:', np.round(ratio_orange*100, 2))

# result = cv2.bitwise_and(image, image, mask=img_mask) # 원본 이미지와 마스크를 합성


# cv2.imshow('result',result)
# waitKey(0)