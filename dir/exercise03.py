def verify_permissions(func):
    def add_new_func(*args,**kwargs):
        print("验证权限")
        result=func(*args,**kwargs)
        return result
    return add_new_func


def insert(id,name,age):
    print("插入",id,name,age)
    return "OK"
@verify_permissions
def delete(id):
    print("删除",id)
    return "NO"
insert = verify_permissions(insert)
a=insert(1001,"葫芦娃",7)
b=delete(1001)
print(a)
print(b)