import time,functools

def TestFun(fun):
    @functools.wraps(fun)
    def fun2(self, *args, **kwargs):
        a = [];b = a
        self.innerwindow.showtext('['+ time.strftime("%H:%M:%S", time.localtime())+']' + ' -INFO- ' + 'Invoke function ' + fun.__name__ + '().')
        try:
            a = fun(self,*args, **kwargs)
        except Exception as e:
            self.innerwindow.showtext('['+ time.strftime("%H:%M:%S", time.localtime())+']' + ' -ERROR- ' + 'Error at function ' + fun.__name__ + '() :'+repr(e) + '.')
        if a is not b:
            self.innerwindow.showtext('['+ time.strftime("%H:%M:%S", time.localtime())+']' + ' -INFO- Function ' + fun.__name__ + '() Return: '+ str(a) + '.')
        self.innerwindow.showtext('['+ time.strftime("%H:%M:%S", time.localtime())+']' + ' -INFO- ' + 'Finish function ' + fun.__name__ + '().')
    return fun2
