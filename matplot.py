import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

#Data를 지정함. File을 불러오는 것 또한 가능
x = np.arange(0, 10.5, 0.5)
y = np.sin(x)


#Data를 label을 붙여 dictionary로 저장
data_dict = {'data_x':x, 'data_y':y}
#파일 불러오기
x1, y1 = np.loadtxt(r'D:\matplot\Wavelength\370(100,dirct).txt', skiprows=17, usecols=(0,1), max_rows=3648, unpack=True)


#기본적으로 plotting을 함
#선의 종류는 linestyle = solid, dashed, dotted, dashdot 이 있음
plt.plot('data_x', 'data_y', data = data_dict, linestyle = 'dashed', label = 'Sin function', color = 'black', marker = '*')

#Axis에 label을 붙임. rotation = 1을 통해 세로쓰기
plt.xlabel("x", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("sin(x)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

#범례를 출력함. 위치는 우상단이 1.0, 1.0 및 좌하단이 0.0, 0.0 
plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

#Axis의 범위를 지정함
#plt.axis의 옵션은 다음과 같음; 'on' | 'off' | 'equal' | 'scaled' | 'tight' | 'auto' | 'normal' | 'image' | 'square'
plt.xlim([0,10])
plt.ylim([-2, 2])

#Axis의 scale을 설정함. log, linear, symlog, logit 가능
plt.xscale('linear')
plt.yscale('linear')

#Graph 아래 채우기
plt.fill_between(x, -2, y, alpha = 0.2, color = 'indigo')

#Grid를 그리기
plt.grid(True, axis = 'both', alpha = 0.5, linestyle = 'dashdot')

#눈금 표시
plt.xticks(np.arange(0., 10.1, ))
plt.yticks(np.arange(-2., 2.1, 1))

#제목 설정
plt.title('Sin function', loc = 'center', pad = 15, font = 'Arial', fontsize = 15)


#수직, 수평선 그리기
plt.hlines(-0.5, 1, 5, linestyles = 'dashed', linewidth = 2, color = 'black')
plt.vlines(2, -1, 0, linestyles = 'dotted', linewidth = 2, color = 'black')

#관습적으로 사용
plt.show()

