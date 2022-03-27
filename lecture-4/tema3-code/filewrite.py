with open("test.txt", "w+") as f:
    f.write("Hello world")
    f.seek(0)
    print(f.read())
