import xlsxwriter
import string

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
title = ''
content = ''


def write_title():
    title = input(f'Type title/s \n')
    ti = list(map(str, title.split()))
    len_list = len(ti)

    for k in range(len_list):
        x = (str(alphabet_list[k]) + str(1))
        print(x)
        d = (str(ti[k]))
        worksheet.write(x, str(d))
        print(f'Title successfully written')


def write_content_row():
    add = 1
    content = input(f'Type content \n')
    ti = list(map(str, content.split()))
    len_list = len(ti)

    for k in range(len_list):
        x = (str(alphabet_list[k]) + str(2))
        print(x)
        d = (str(ti[k]))
        worksheet.write(x, str(d))
        add += 1
        print(f'Content successfully written in column {2}')


write_title()
write_content_row()
workbook.close()
exit()