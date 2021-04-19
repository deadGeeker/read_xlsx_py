# 导入excel读取模块xlrd, 版本为1.2.0
from xlrd import open_workbook
# 导入绘图模块matplotlib
import matplotlib.pyplot as plt

# 定义一个函数，函数的作用是通过xlsx文件名读取对应的文件，并返回列总数据x_data, y_data
def read_xlsx(filename):
    x_data = []
    y_data = []
    wb = open_workbook(str(filename))
    for s in wb.sheets():
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row, col).value)
            x_data.append(values[0])
            y_data.append(values[1])
    return x_data, y_data

x, y = read_xlsx("test.xlsx")
# plt.plot(x 轴数据, y 轴数据, 曲线类型,曲线线宽)
plt.plot(x, y, 'bo-', linewidth=1)
plt.title(u"TR14 phase detector")
plt.xlabel(u"input-deg")
plt.ylabel(u"output-V")
plt.show()