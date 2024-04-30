import requests
async def func(param1, param2):
    do_stuff()
    google = await requests.get('https://www.google.com')
    return google

def do_stuff():
    for i in range(5):
        yield i

def main():
    result = func()
    print(result)
main()