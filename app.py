from flask import Flask
<<<<<<< .mine

=======

>>>>>>> .theirs
from flask import render_template
import datetime
import os,sys

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('chifan.html')



@app.route('/<id>')
def choose(id):

    err = 0 #错误标志

    #读取文件内容
    f = open(os.path.dirname(os.path.realpath(__file__)) + '\\test.txt', 'r')
    first_line_day = int(f.readline())
    second_line_addtime = int(f.readline()) #分钟和时间的总和
    third_line_id = int(f.readline())
    f.close()

    #采集当前时间
    nowtime = datetime.datetime.now()
    day = nowtime.day
    minute = nowtime.minute
    hour = nowtime.hour

    now_addtime = minute + 60 * hour

    if (first_line_day != day):
        '''第二天更新数据'''
        second_line_addtime = 0


    #避免服务器请求fav.ico
    try:
        temp = int(id)
    except:
        err = 1
        print ('done')



    # 更新数据
    if ((now_addtime - second_line_addtime) > 1 and err == 0 ):
        first_line_day = day
        second_line_addtime = now_addtime
        third_line_id = id

        f2 = open(os.path.dirname(os.path.realpath(__file__)) + '\\test.txt', 'w')
        f2.writelines(str(first_line_day) + '\n')
        f2.writelines(str(second_line_addtime) + '\n')
        f2.writelines(str(third_line_id))
        f2.close()


    #选择地点
    third_line_id = int(third_line_id)
    if (third_line_id >= 0 and third_line_id <20 ):
        area = '外卖'
    elif (third_line_id >= 20 and third_line_id <40 ):
        area = '西门'
    elif (third_line_id >= 40 and third_line_id <60 ):
        area = '北门'
    elif (third_line_id >= 60 and third_line_id <80 ):
        area = '小铺'
    elif (third_line_id >= 60 and third_line_id <=100 ):
        area = '学府'


    #显示时间
    last_hour = second_line_addtime // 60
    last_min = second_line_addtime % 60

    return render_template('xuanze.html', time_hour = last_hour, time_min = last_min, post_id = third_line_id, area = area)




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
