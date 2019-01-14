import os.path
# 发送邮件
import smtplib
# 构造邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

# ---------------------------------- email -----------------------------------------------------------------------
# # 对应发送端一
from_addr = 'tabaha@sina.com'
to_addr = 'cyyun1@sina.com'
to_addrs = ['cyyun1@sina.com', '498547626@qq.com']

# # 二
# from_addr = '3171962010@qq.com'
# to_addr = 'cyyun1@sina.com'
# to_addrs = ['cyyun1@sina.com', '498547626@qq.com']
# ***************************** 邮件内容 ***************************************************************


# 格式化邮件地址，如果包含中文，需要通过Header对象进行编码
def _format_addr(s):
    # 结果为tuple类型，取出对应部分
    name, addr = parseaddr(s)
    pair = (Header(name, 'utf-8').encode(), addr)
    return formataddr(pair)


# # 邮件的正文内容，字符串
# # 大概意思应该是 smtp.sina.com 会解析邮件正文内容，
# # 如果里面包含“from:XXX@sina.com”信息，与 msg [‘From’] 一致，就算作 match。
# *************************** 纯文本文件--邮件内容形式一：字符串 **************************
# msg = """
# to:%s
# from:%s
# Hello,I am smtp server
# """ % (to_addrs, from_addr)

# ************************** 纯文本文件--邮件内容形式二：使用MIMETest **********************
# content
# plain表示纯文本
text = 'hello, send by Python...'
msg = MIMEText(text, 'plain', 'utf-8')

# header
msg['From'] = _format_addr('Python <%s>' % from_addr)

# # ******* one address to receive *****************
# msg['To'] = _format_addr('Generator <%s>' % to_addr)
# # ******* two or more addresses to receive **************
# https://stackoverflow.com/questions/46992648/smtplib-tuple-object-has-no-attribute-encode
to_addrs_formate = [_fo8rmat_addr('Generator <%s>' % to_addrs[0]), _format_addr('Generator <%s>' % to_addrs[1])]
# string 不是list
msg['To'] = ','.join(to_addrs_formate)

msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# ************************** HTML文件--邮件发送内容形式三：使用MIMETest ***********************
# html_str = '<html><body><h1>Hello</h1>' + \
#            '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
#            '</body></html>'
# msg = MIMEText(html_str, 'html', 'utf-8')
# to_addrs_formate = [_format_addr('Generator <%s>' % to_addrs[0]), _format_addr('Generator <%s>' % to_addrs[1])]
# msg['From'] = _format_addr('Python <%s>' % from_addr)
# msg['To'] = ','.join(to_addrs_formate)
#
# msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# ************************** 附件--邮件发送内容形式四：使用MIMEMultipart, MIMEText, MIMEBase ***********************
# # 添加多个附件，则是下列各方法的组合；添加n个附件，n个方法
#
# msg = MIMEMultipart()
#
# # header
# to_addrs_formate = [_format_addr('Generator <%s>' % to_addrs[0]), _format_addr('Generator <%s>' % to_addrs[1])]
# msg['From'] = _format_addr('Python <%s>' % from_addr)
# msg['To'] = ','.join(to_addrs_formate)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
# # content 添加到msg
# msg.attach(MIMEText('send a file', 'plain', 'utf-8'))
#
# # file
# # ************** 附件file-----html ***************************
# proDir = os.path.split(os.path.realpath(__file__))[0]
# filePath = os.path.join(proDir,'result', 'HTMLReport.html')
#
# # ************** 方法一：使用MIMEBase ************
# with open(filePath, 'rb') as f:
#     filehtml = MIMEBase('html', 'html', filename='HTMLReport.html')
#     # file header 定义附件名
#     filehtml.add_header('Content-Disposition', 'attach', filename='HTMLReport.html')
#     filehtml.add_header('Content-ID', '<0>')
#     filehtml.add_header('X-Attachment-Id', '0')
#     # file read
#     filehtml.set_payload(f.read())
#     # base64
#     encoders.encode_base64(filehtml)
#     # 附件添加到msg
#     msg.attach(filehtml)

# # ************  方法二：使用MIMEText ***********
# with open(filePath, 'rb') as f:
#     filehtml = MIMEText(f.read(), 'base64', 'utf-8')
#     # filehtml header
#     filehtml['Content-Type'] = 'application/octet-stream'
#     filehtml['Content-Disposition'] = 'attachment; filename="HTMLReport.html"'
#     # 附件添加到msg
#     msg.attach(filehtml)

# # *********** 附件file-----image ***************************
# proDir = os.path.split(os.path.realpath(__file__))[0]
# filePath = os.path.join(proDir, 'result', 'e.png')
# # ************** 方法一：使用MIMEBase *************
# 第一张图片
# with open(filePath, 'rb') as f:
#     fileImage = MIMEBase('image', 'png', filename='e.png')
#     # fileImage header 定义附件名
#     fileImage.add_header('Content-Disposition', 'attach', filename='a.png')
#     fileImage.add_header('Content-ID', '<0>')
#     fileImage.add_header('X-Attachment-Id', '0')
#     # fileImage read
#     fileImage.set_payload(f.read())
#     # base64
#     encoders.encode_base64(fileImage)
#     # 附件添加到msg
#     msg.attach(fileImage)

# # 添加第二张图片
# with open('test2.png', 'rb') as f:
#     mime2 = MIMEBase('image', 'png', filename='test2.png')
#     # 加上必要的头信息:
#     mime2.add_header('Content-Disposition', 'attachment', filename='test2.png')
#     mime2.add_header('Content-ID', '<1>')
#     mime2.add_header('X-Attachment-Id', '1')
#     # 把附件的内容读进来:
#     mime2.set_payload(f.read())
#     # 用Base64编码:
#     encoders.encode_base64(mime2)
#     # 添加到MIMEMultipart:
#     msg.attach(mime2)

# # ************  方法二：使用MIMEText ***********
# with open(filePath, 'rb') as f:
#     fileImage = MIMEText(f.read(), 'base64', 'utf-8')
#     fileImage['Content-Disposition'] = 'attachment; filename = "e.png"'
#     msg.attach(fileImage)

# # ************  方法三：使用MIMEImage ***********
# imagefile = open(filePath, 'rb').read()
# fileImage = MIMEImage(imagefile)
# # fileImage['Content-Type'] = 'application/octet-stream'
# fileImage['Content-Disposition'] = 'attachment; filename="HTMLReport.html"'
# fileImage.add_header('Content-ID','<0>')
# mg.attach(fileImage)
# ************************** HTML文件、正文有图片--邮件发送内容形式四：使用MIMETest ***********************

# proDir = os.path.split(os.path.realpath(__file__))[0]
# filePath = os.path.join(proDir, 'result', 'e.png')
#
# msg = MIMEMultipart()
#
# # header
# to_addrs_formate = [_format_addr('Generator <%s>' % to_addrs[0]), _format_addr('Generator <%s>' % to_addrs[1])]
# msg['From'] = _format_addr('Python <%s>' % from_addr)
# msg['To'] = ','.join(to_addrs_formate)
# msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()
#
# # ************************* 正文为html内容 ******************************************
# # 图片添加到正文的html语句 '<p><img src="cid:0"></p>'
# # cid:0表示附件中的第一张图片；cid:1表示附件中的第二张图片
#
# # content
# html_str = '<html><body><h1>Hello</h1>' + \
#            '<p>send by <a href="http://www.python.org">Python</a>...</p>' + \
#            '<p><img src="cid:0"></p>' +\
#            '</body></html>'
# msgContent = MIMEText(html_str, 'html', 'utf-8')
# msg.attach(msgContent)
#
# # ********* 图片作为附件添加 *********************************************
# # file
# # # ************** 方法一：使用MIMEBase *************
# with open(filePath, 'rb') as f:
#     fileImage = MIMEBase('image', 'png', filename='e.png')
#     # fileImage header 定义附件名
#     fileImage.add_header('Content-Disposition', 'attach', filename='a.png')
#     fileImage.add_header('Content-ID', '<0>')
#     fileImage.add_header('X-Attachment-Id', '0')
#     # fileImage read
#     fileImage.set_payload(f.read())
#     # base64
#     encoders.encode_base64(fileImage)
#     # 附件添加到msg
#     msg.attach(fileImage)
#
# # # ************  方法二：使用MIMEText ***********
# # with open(filePath, 'rb') as f:
# #     fileImage = MIMEText(f.read(), 'base64', 'utf-8')
# #     fileImage['Content-Disposition'] = 'attachment; filename = "e.png"'
# #     fileImage['Content-Type'] = 'image/png; filename = "e.png'
# #     # 将图片附件添加到正文需要用到'Content-ID'; <n>对应cid=n
# #     fileImage['Content-ID'] = '<0>'
# #     msg.attach(fileImage)


# ----------------------------------------------------------------------------------------------------------------
# ---------------------------------- smtplib ----------------------------------------------------------------------
# # 发送端
host = 'smtp.sina.com'
port = 25
sslPort = 465
# 发送端
username = 'tabaha@sina.com'
password = 'cyyun987654'

# # 发送端 二
# host = 'smtp.qq.com'
# sslPort = 465
# port = 25
# # SSL “设置-账户 获取授权码作为passport”
# username = '3171962010@qq.com'
# password = 'hkpbympjfnpydeci'

# ------------------------------ smtplib --------------------------------------------------------------------------
# ****************************** 实例化smtplib *******************************************************************
# 发送邮件的三种方式： https://www.cnblogs.com/netsa/p/7992280.html
# -------------------- 普通方式，通信过程不加密 -------------------------------------
# # 实例化smtplib对象一：使用无参构造；在使用connect方法链接MUA
# smtp = smtplib.SMTP()
# smtp.connect(host, port)

# # 实例化smtp对象二：使用有参构造，直接链接MUA
smtp = smtplib.SMTP(host, port)

# -------------------- tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口 ---------
# # # 创建安全连接方式二：tls
# # 创建SMTP对象后，立刻调用starttls()，创建安全连接
# smtp = smtplib.SMTP(host, port)
# smtp.starttls()

# --------------------- 纯粹的ssl加密方式，通信过程加密，邮件数据安全 ---------------------
# # 创建安全连接方式一：ssl 使用SMTP_SSL()
# # 此种方式不成功
# # smtp = smtplib.SMTP_SSL()
# # smtp.connect(host, port)
# # 创建安全连接方式一：ssl 使用SMTP_SSL()
# smtp = smtplib.SMTP_SSL(host, sslPort)

# **************************** 登录发送端邮箱 **********************************
smtp.ehlo()
# 发送端邮箱登录
smtp.login(username, password, initial_response_ok=True)

# **************************** 设置控制台日志 ***************************************
# 设置控制台日志级别 打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。
smtp.set_debuglevel(1)

# ********************************** 发送邮件 ********************************************************************
# smtp.sendmail(from_addr, to_addr,  msg)
# smtp.sendmail(from_addr, to_addr,  msg.as_string())
smtp.sendmail(from_addr, to_addrs,  msg.as_string())

# ************************ 退出发送邮件服务 *************************************
smtp.quit()

# print('邮件发送成功！')




# ********************************************************************************************************
# SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议
# 它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

# https://help.aliyun.com/knowledge_detail/51584.html
# MIME，英文全称为“Multipurpose Internet Mail Extensions”，即多用途互联网邮件扩展，是目前互联网电子邮件普遍遵循的邮件技术规范。
# MIME 协议的 RFC 地址：https://www.ietf.org/rfc/rfc2045.txt 。
# 一封普通的文本邮件的信息包含一个头部分（例如：From、To、Subject 等等）和一个体部分。
# 体部分通常为单体类型（例如：text、image、audio、video、application 等等）或是复合类型（即：multipart）。
# 头部分和体部分之间用一个空行进行分隔，并且体部分的类型由信头内容类型字段 Content-Type 描述。

# MIME 的信体部分:
# 邮件中常见的简单类型有 text/plain(纯文本)和 text/html(超文本)。
# 复杂的邮件内容格式采用 multipart 类型，可以包括纯文本/超文本、内嵌资源（图片）、附件类型等等。
# multipart 类型的邮件体被分为多个段，每个段又包含段头和段体两部分，这两部分之间也以空行分隔
# Content-Type	段体的类型
# Content-Transfer-Encoding	段体的传输编码方式
# Content-Disposition	段体的安排方式
# Content-ID	段体的 ID
# Content-Location	段体的位置(路径)
# Content-Base	段体的基位置


# 发送一封电子邮件的过程：
# 　　发件人 -> MUA（发送端） -> MTA -> MTA -> 若干个MTA - 【MDA】 <- MUA <- 收件人

# MUA：Mail User Agent——邮件用户代理
# MTA：Mail Transfer Agent——邮件传输代理，就是那些Email服务提供商
# MDA：Mail Delivery Agent——邮件投递代理
# smtplib模块主要负责发送邮件：连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。

# from email.mime.text import MIMEText -----------  MIMEText 文本邮件对象
# from email.mime.image import MIMEImage -----------  MIMEImage 图片作为附件的对象
# from email.mime.base import MIMEBase   -----------   MIMEBase 任何对象
# from email.mime.multipart import MIMEMultipart  -----------   MIMEMultipart 邮件对象的组合


# 内容类型（Content-Type），表现形式为：Content-Type: [type]/[subtype]。
#
# 其中 type 的形式为：
# text：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的。
# Image：用于传输静态图片数据。
# Audio：用于传输音频或者音声数据。
# Video：用于传输动态影像数据，可以是与音频编辑在一起的视频数据格式。
# Application：用于传输应用程序数据或者二进制数据。
# Message：用于包装一个 E-mail 消息。
# Multipart：用于连接消息体的多个部分构成一个消息，这些部分可以是不同类型的数据。
# 其中 subtype 用于指定 type 的详细形式，常用的 subtype 如下所示：
# text/plain（纯文本）
# text/html（HTML 文档）
# application/xhtml+xml（XHTML 文档）
# image/gif（GIF 图像）
# image/jpeg（JPEG 图像）
# image/png（PNG 图像）
# video/mpeg（MPEG 动画）
# application/octet-stream（任意的二进制数据）
# message/rfc822（RFC 822 形式）
# multipart/alternative（HTML 邮件的 HTML 形式和纯文本形式，相同内容使用不同形式表示。）
# 内容传输编码（Content-Transfer-Encoding），指定内容区域使用的字符编码方式。
# 通常为：7bit，8bit，binary，quoted-printable，base64。


# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
# 要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。

# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage