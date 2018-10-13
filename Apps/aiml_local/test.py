from Apps import aiml

alice = aiml.Kernel()

alice.learn('cn-test.aiml')
alice.learn("contact.aiml")
alice.learn("who.aiml")
alice.learn("nk.aiml")
alice.learn('contact.aiml')
alice.learn('news.aiml')
alice.learn('url0.aiml')

def Contact():
    print("我知道可多部门拉~有学校办公室（党办、校办）党委组织部、党校，新闻中心，党委统战部，机关党委，纪委、监察室，党委学生工作部")
    print("不信你考考我")
    while True:
        input_message = input("Enter your message >> ")
        if input_message == "q":
            return input_message
        str = alice.respond(input_message)
        print (str)
        if str != "":
            print("快夸夸我，我想知道更多，我不想聊这件事了")


def News():
    print("你想知道哪个学院的最新公告呀？")
    print("选择：计算机，信安...")
    input_message = input("Enter your message >> ")
    if re.match("计算机", input_message):
        print(alice.respond("计算机"))
    input_message = input("Enter your message >> ")
    str = alice.respond("计算机 " + input_message)
    print (str)

    if input_message == "q":
        return input_message


def Teacher():
    if input_message == "q":
        return input_message


def getUrl():
    print("好多人都问我信息门户，南开校历，网费查询...你想知道什么")
    input_message = input("Enter your message >> ")
    print(alice.respond(input_message))
    if input_message == "q":
        return input_message

def major(request):
    print("你好呀，我是可爱的南小开")

    print("我猜你想问：")
    print("联系部门、最新公告、找老师、日常网站")
    while True:
        input_message = input("Enter your message >> ")
        if input_message == "联系部门":
            input_message = Contact()
        if input_message == "最新公告":
            input_message = News()
        if input_message == "找老师":
            input_message = Teacher()
        if input_message == "日常网站":
            input_message = getUrl()
        if input_message == "q":
            break
