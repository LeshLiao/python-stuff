
# You could pass the function memory to another variable.

def hello():
    print("Hello!")

print(hello)

hi = hello
print(hi)

hi()

# Another example

say = print
say("I can print something by say function.")
