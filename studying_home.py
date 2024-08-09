'''
工作室名字：QY STAR工作室
根据地用户：
根据地用途：提供学习资料、在线课程推荐和学习经验分享
最喜欢的现有模块：
现有模块改进灵感：
原创模块：
原创模块一句话功能介绍：
python -m streamlit run G:\瞿烨资料新\2024暑假创赛营瞿烨\studying_home.py [ARGUMENTS]
st.snow()
st.balloons()
st.title('标题')
st.success('通关')
st.warning('警告')
st.error('报错')
st.info('提示信息')
with st.spinner('Laoding......'):
    sleep(3)
'''
import streamlit as st
from PIL import Image
from time import *

page = st.sidebar.radio(
    '目录', ['主页', '学习资料推荐', '在线课程推荐', '学习经验分享', '图片处理工具', '智能词典', '留言区', '调查问卷'])


def page1():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('lonely_day.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.title(':derelict_house_building:学习之家欢迎你！:male-teacher:')
    st.info('Welcome to the Learning Home, where there are many excellent learning resources for you to choose from!')
    st.info('欢迎来到学习之家，这里有很多优秀的学习资源供你选择！')
    st.write('————本网址由QY Star工作室制作，所有资源均公共提供')


def page2():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('菊次郎的夏天.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.error('本分页为空')


def page3():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('Shadow Of The Sun.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.info(':+1:这是国家中小学生教育平台，上面有许许多多各地的名师讲课，你可以提前预习、课后复习、免费补课，我个人认为这里老师讲的内容还是很不做的。:+1:')
    st.info(':+1:这是国家中小学生教育平台的网址：https://basic.smartedu.cn/')
    st.image('国家中小学教育平台主页.png')


def page4():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('lonely_day.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.error('本分页为空')


def page5():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('lonely_day.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.write(':cat:图片处理工具:cat:')
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(['原图', '改色1', '改色2', '改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 1, 0, 2))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 2, 0, 1))


def page6():
    with st.spinner('Laoding......'):
        sleep(1)
    with open('lonely_day.mp3', 'rb') as f:
        mybg = f.read()
    st.audio(mybg, format=('audio/mp3'), start_time=0)
    st.write(':trophy:智能词典:trophy:')

    with open('words_space.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i] = word_list[i].split('#')
    word_dict = {}
    for i in word_list:
        word_dict[i[1]] = [int(i[0]), i[2]]  # 单词：[计数，中文]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        time_list = f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i] = time_list[i].split('#')
    time_dict = {}
    for i in time_list:
        time_dict[int(i[0])] = int(i[1])

    word = st.text_input('请输入你想查询的单词：')
    if word in word_dict:
        st.write(word_dict[word])
        n = word_dict[word][0]
        if n in time_dict:
            time_dict[n] += 1
        else:
            time_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in time_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        if word == 'python':
            st.code('''恭喜你触发彩蛋，这是一行python代码！
                    print("hello codemao")''')
        if word == 'snow':
            st.snow()


def img_change(img, cr, cg, cb):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][cr]
            g = img_array[x, y][cg]
            b = img_array[x, y][cb]
            img_array[x, y] = (b, g, r)
    return img


def page7():
    st.title('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        message_list=f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split('#')
    for i in message_list:
        if i[1]=='阿短':
            with st.chat_message("🌈"):
                st.write(i[1],":",i[2])
        elif i[1]=='编程猫':
            with st.chat_message("🍥"):
                st.write(i[1],":",i[2])
        elif i[1] == '建议':
            with st.chat_message("🍙"):
                st.write(i[1],":",i[2])
    name=st.selectbox('我是：',['阿短','编程猫','建议'])
    new_message=st.text_input('输入想要说的话...')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in message_list:
                message += i[0]+'#'+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)



def page8():
    choice = st.radio('你认为我的网站怎么样，我做出调查：', ['一星', '二星', '三星', '四星', '五星'])
    if st.button('确认提交'):
        if choice == '一星' or '二星' or '三星':
            st.write('你认为我的程序哪里应该改进呢？在留言框里提出建议吧！')
        if choice == '四星' or '五星':
            st.write('感谢你的评价')


if page == '主页':
    page1()
elif page == '学习资料推荐':
    page2()
elif page == '在线课程推荐':
    page3()
elif page == '学习经验分享':
    page4()
elif page == '图片处理工具':
    page5()
elif page == '智能词典':
    page6()
elif page == '留言区':
    page7()
elif page == '调查问卷':
    page8()
