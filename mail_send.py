import sys
import smtplib
import qrcode
from optparse import OptionParser

Parser = OptionParser()
Parser.add_option("-E", "--E_mail", dest="Email", help="gönderici e posta adresi alanı")
Parser.add_option("-p", "--password", dest="passw", help="gonderici kisinin e posta sifresi alanı")
Parser.add_option("-e", "--e_mail", dest="email", help="alıcı e posta adresi alanı")
Parser.add_option("-m", "--message", dest="message", help="mesajın girildigi alan")
(inputs, argumets) = Parser.parse_args()

sender_e_mail = inputs.Email
password = inputs.passw
target_e_mail = inputs.email
message = inputs.message

image = qrcode.make(message)
image.save("message.png")

try:
    e_mail = smtplib.SMTP("smtp@gmail.com", 587)
    e_mail.starttls()
    e_mail.login(str(sender_e_mail), password)
    e_mail.sendmail(str(sender_e_mail), str(target_e_mail), message.png)
    e_mail.quit()
    sys.exit()

except KeyboardInterrupt:
    print("pressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()
