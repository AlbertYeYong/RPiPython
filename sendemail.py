import smtplib
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('YourGoogeTest', 'YourPw')
to = 'John@xxx.com'
_from = 'YourGoogeTest@gmail.com'
subject = 'This is a test'
header = 'To:' + to + '\n'
header = header + 'From:' + _from + '\n'
header = header + 'Subject:' + subject + '\n'
body = 'This is a test message from my Python script!'
message = header + body
smtpserver.sendmail(_from, to, message)
smtpserver.quit()
