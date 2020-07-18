##This  is e email slicer.  when you write your email adress  it is checking your email adress  is it correct form .
###its is giving your username and domain name


email = input("enter your email adress")

if "@" not in email:
    print("please write correct email adress")
else:
    emaillist = email.split("@")

    print("your username:", emaillist[0])
    print("your domain name:", emaillist[1])
