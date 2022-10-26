#메인 코드
from add import add_func
from sub import sub_func
from mul import mul_func

#함수 선언

11
#전역 변수부
num1,num2,res=100,200,0

#메인 코드부
res = add_func(num1,num2)
print(num1,"+",num2,"=",res)
res = sub_func(num1,num2)
print(num1,"-",num2,"=",res)
res = mul_func(num1,num2)
print(num1,"*",num2,"=",res)
