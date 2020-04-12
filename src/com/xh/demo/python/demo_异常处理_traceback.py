'''
Title: traceback.format_exc()
Description: 

异常处理是日常操作了，但是有时候不能只能打印我们处理的结果，还需要将我们的异常打印出来，这样更直观的显示错误，因此需要用到 traceback模块来进行处理


traceback.print_exc() 跟 traceback.format_exc() 区别：
    - format_exc()：返回字符串；
    - print_exc()：则直接给打印出来。还可以接受file参数直接写入到一个文件。比如 traceback.print_exc(file=open('tb.txt','w+')) 写入到tb.txt文件去。
即 traceback.print_exc() 与 print(traceback.format_exc()) 效果是一样的。


参考地址：
    https://www.cnblogs.com/alummox/p/7465197.html

@author H.Yang
@email xhaimail@163.com
@date 2020/03/08
'''
import traceback

if __name__ == '__main__':
    
    try:  
        1/0  
    except Exception as e:  
        traceback.print_exc()  
        print(traceback.format_exc())
