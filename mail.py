from email import message
import smtplib

smtp_host='smtp.gmail.com'
smtp_port=587

msg = message.EmailMessage()
msg.set_content("$B$3$s$K$A$O!"(BTaisei$B$G$9!#BND4ITNI$N0Y!"K\F|$N%$%Y%s%H$r7g@J$5$;$FD:$-$^$9!#(B") 
msg['Subject'] = "$B7g@JO"Mm(B"
msg['From'] = "taiseiyo11@gmail.com"
msg['To'] = "drn29309@kwansei.ac.jp"
 
# $B%a!<%k%5!<%P!<$X%"%/%;%9(B
server = smtplib.SMTP(smtp_host, smtp_port)
#$B0E9f2=$N3+;O(B
server.ehlo()
server.starttls()
#TLS (Transport Layer Security) $B%b!<%I$G(B SMTP $B@\B3$7$^$9!#B3$/A4$F$N(BSMTP $B%3%^%s%I$O0E9f2=$5$l$^$9!#(B
server.login("taiseiyo11@gmail.com","taiseiyo11")
server.send_message(msg)
server.quit()
