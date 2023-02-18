'''
    学生信息库
'''

students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },

    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3:{
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4:{
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5:{
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
}

# 检查学生信息
def check_info(**kwargs):
    if 'name' not in kwargs:
        print('缺少学生姓名')
    if 'age' not in kwargs:
        print('缺少学生年龄')
    if 'class_number' not in kwargs:
        print('缺少学生班级')
    if 'sex' not in kwargs:
        print('缺少学生性别') 
    return True  

# 获取全部用户
def get_all_students():
    for keys, values in students.items():
        print('学号:{}, 学生姓名:{}, 学生年龄:{}, 学生班级:{}, 学生性别:{}'.format(
            keys, values.get('name'), values.get('age'), values.get('class_number'), values.get('sex')
            ))
    return students

# 添加用户
def add_students(**kwargs):
    check = check_info(**kwargs)
    if check != True:
        print(check)
        return
    keys = max(students) + 1

    students[keys] = {
        'name': kwargs('name'),
        'age': kwargs('age'),
        'class_number': kwargs('class_number'),
        'sex': kwargs('sex')
    }


def delete_students(student_id):
    if student_id not in students:
        print('学号{}不存在'.format(student_id))
    else:
        user_info = students.pop(student_id)
        print('学号为{}, {}的学生信息已被删除'.format(student_id, user_info['name']))


def update_students(student_id, **kwargs):
    if student_id not in students:
        print('学号{}不存在'.format(student_id))

    check = check_info(**kwargs)
    if check != True:
        print(check)
        return
    
    students[student_id] = kwargs
    print('同学信息更新完毕')

 

def get_user_by_id(student_id):
    return students.get(student_id)


def search_users(**kwargs):
    values = list(students.values())
    key = None
    value = None
    result = []

    if 'name' in kwargs:
        key = 'name'
        value = kwargs[key]

    elif 'age' in kwargs:
        key = 'age'
        value = kwargs[key]

    elif 'class_number' in kwargs:
        key = 'class_number'
        value = kwargs[key]

    elif 'sex' in kwargs:
        key = 'sex'
        value = kwargs[key]
    else:
        print('没有发现搜索的关键字')
        return

    for user in values:
        if user[key] == value:
            result.append(user)
    return result
    
print(search_users(name = 'dewei'))
