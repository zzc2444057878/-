

# # 题目1
# # 思路1：一个二维数组，其中有两个元素，第一个元素是一个左边的栈，第二个元素是右边的栈
# class Stack_1:
#     def __init__(self):
#         self.array = [[],[]]
#
#     def l_push(self,node):
#         self.array[0].append(node)
#
#     def l_pop(self):
#         if not self.array[0]:
#             return None
#         else:
#             return self.array[0].pop()
#
#     def r_push(self,node):
#         self.array[1].append(node)
#
#     def r_pop(self):
#         if not self.array[1]:
#             return None
#         else:
#             return self.array[1].pop()
#
# # 思路2：两个栈分别从数组的两端开始向中间走，
# class Stack_2:
#     def __init__(self):
#         self.array = []
#
#     def l_push(self,node):
#         self.array.insert(0,node)
#
#     def l_pop(self):
#         if self.array:
#             return self.array.pop(0)
#         else:
#             return None
#
#     def r_push(self,node):
#         self.array.append(node)
#
#     def r_pop(self):
#         if self.array:
#             return self.array.pop()
#         else:
#             return None

# 题目3，大数加法
class NumberAdd:
    def add(self,):
        num1 = input('输入第一个大数：')
        num2 = input('输入第二个大数：')
        if int(num1) >= 0:
            num1_list = [int(i) for i in num1]
        else:
            num1_list = [-int(i) for i in num1[1:]]
        if int(num2) >= 0:
            num2_list = [int(j) for j in num2]
        else:
            num2_list = [-int(j) for j in num2[1:]]

        max_length = max(len(num1_list),len(num2_list))
        min_length = min(len(num1_list),len(num2_list))


        if min_length != max_length:
            # 在较短的list前面补0，直到与较长的list长度相同
            if len(num1_list) == min_length:
                for i in range(max_length - min_length):
                    num1_list.insert(0,0)
            else:
                for j in range(max_length-min_length):
                    num2_list.insert(0,0)

        num3_list = []
        # 进位
        carry = 0
        for i in range(-1,-max_length-1,-1):
            if num1_list[i] + num2_list[i] + carry >= 0:
                # 余数
                remainder = (num1_list[i] + num2_list[i] + carry) % 10
                carry = (num1_list[i] + num2_list[i] + carry) // 10
                num3_list.append(str(remainder))
            else:
                # 余数
                remainder = (num1_list[i] + num2_list[i] + carry) % -10
                carry = int((num1_list[i] + num2_list[i] + carry) / 10)

                # 对两个列表的最后一个数进行判断，如果它们对10取模为0
                if i != -max_length:
                    num3_list.append(str(abs(remainder)))
                elif  i == -max_length and carry == 0:
                    num3_list.append(str(remainder))
                else:
                    num3_list.append(str(abs(remainder)))
        #　在最高位中，如果两个数的最高位相加大于等于10,则长度加1，最高位为该数字
        if carry:
            num3_list.append(str(carry))

        num3_list.reverse()
        if num3_list[0] == '0':
            del num3_list[0]
        return ''.join(num3_list)

a = NumberAdd()
print(a.add())