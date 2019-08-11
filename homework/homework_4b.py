from homework.homework_4a import SpamSender

receiver_email = ["isa12python@gmail.com", "luminoforek@gmail.com"]

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="https://infoshareacademy.com">InfoShare Academy</a> 
       has many great courses.
    </p>
  </body>
</html>
"""

test_email = SpamSender("isa12python@gmail.com", receiver_email, "iSAforever")
test_email.email_sender("Homework_4", html, "smtp.gmail.com", 465)