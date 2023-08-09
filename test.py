def error_handler(funct):
    def wrapper(*args, **kwargs):
        try:
            result = funct(*args,**kwargs)
            return result
        except Exception as  e : 
            print(f"An error occured {e}")

    return wrapper 


@error_handler
def divide(a: int, b: int):
    return a/b

# first test 
answer1 = divide(10,5)
print(f"answer1 : {answer1}")
answer = divide(10,0)
print(f"answer2 : {answer}")


