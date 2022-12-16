from subprocess import Popen, PIPE
from urllib.request import urlopen
from urllib.error import URLError


def test_map(host, port):
    cmd = "datasette app --static assets:static-files --static images:images --template-dir=app/templates/ -h {h} -p {p} ".format(h=host, p=port)
    print('URL:', cmd)
    try:
        map_test = Popen(cmd, shell=False)    
    except:
        print('cmd error')
        return False
    try:
        urlopen(str('http://'+str(host)+':'+str(port)))
        print("success")
        return True
    except URLError as error:
        print(error)
        return False
    finally:
        print("end")
        map_test.kill()

test_map('127.0.0.1','8001')