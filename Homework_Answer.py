import json

import requests

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list


def main(stuid):
    info = get_all_course(stuid)
    homrwork_list = get_homework_list(stuid, info['openClassId'], info['courseOpenId'])
    homeworkId = homrwork_list['homeworkId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
    data = {
        'homeWorkId': homeworkId
    }
    html = requests.post(url=url, data=data).json()['data']
    title = html['title']
    with open(f'{title}.txt', 'w', encoding='utf8') as f:
        for i in html['questions']:
            f.write(f'{int(i["sortOrder"]) + 1},{i["title"]}\n')
            try:
                for j in json.loads(i['dataJson']):
                    select = j["SortOrder"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D')
                    if select == 0:
                        select = 'A'
                    elif select == 1:
                        select = 'B'
                    elif select == 2:
                        select = 'C'
                    elif select == 3:
                        select = 'D'
                    elif select == 4:
                        select = 'E'
                    elif select == 5:
                        select = 'F'
                    f.write(f'{select},{j["Content"]}\n')
                answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D').replace(
                    '4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I').replace('9',
                                                                                                              'J').replace(
                    '10', 'L')
                f.write(f'Answer:{answer}\n')
            except:
                pass
        input("作业答案已生成在软件目录下。请回车退出")


if __name__ == '__main__':
    main('')
