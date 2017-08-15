from flask import Flask
app = Flask(__name__) #初始化

@app.route('/') #定义路由
def hello_world(): # 把修饰的函数注册为路由,把hello_world()函数注册为程序跟地址的处理程序（该函数称为视图函数）

    return 'Hello,World!' #响应（返回响应可以包含HTML简单字符串，也可以是复杂的表单）

@app.route('/user/<name>')#尖括号内容是动态部分
def name():
	return 'Hello,ginny'

if __name__=='__main__':#启动服务器
	app.run(debug=True)#选项参数可被app.run函数接受用于设置web服务器的操作模式.在开发过程中启用调试模式会带来一些便利，如激活调试器和重载程序。启用调试模式，把debug参数设为True
	                                                                                                                                           
																																			                                                                                                                                              

