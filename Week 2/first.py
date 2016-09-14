import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

print("Hi there! Let's play some dice. Enter the following information to predict your future")
name = raw_input("Enter your name " )
age = int(raw_input("Enter your age " ))
num1 = int(raw_input("Enter a number between 1 and 10 " ))
predictions = ['Alcohol will be your best friend today', 'A grey hair is going to show itself tomorrow', 'You might as well give up on love', '']


def future():
    if num1 > 0 and num1 < 11:
        print "hello "+name+" you are " + str(num1)
        for i in range (len(predictions)):
        	if i == num1:
        		#print predictions[i]
        		global textforemail 
        		textforemail = predictions[i]
        		#print textforemail
    
    else:
        print "Please enter a number between 1 and 10."
    
future();

fromaddr = "suraa423@newschool.edu"
toaddr = "aditisurana22@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Behold your future"

# print textforemail
body = textforemail
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "****")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()