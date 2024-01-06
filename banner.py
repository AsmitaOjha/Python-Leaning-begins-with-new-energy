def banner_text(text):
    screen_width = 80
    if len(text)>screen_width-4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text =="*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width-4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("if life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that'sto laugh and smile and dance and sing,")
banner_text("")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be sily chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And ... always look on the bright side of life...")
banner_text("*")
result = banner_text("nothing is returned")
print(result)

numbers = [4,2,7,5,8,3,9,6,1]
print(numbers.sort()) # This will print None, as the sort() method modifies the list in-place and returns None.
print(numbers)