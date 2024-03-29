# pip3 install –-index-url https://pypi.tuna.tsinghua.edu.cn/simple jinja2
# some miscs test
import jinja2
import os
import json
from datetime import datetime

print(os.path.dirname(__file__))  # output current path


def testj2():
    #env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
    #template = env.get_template()
    template = jinja2.Template('Hello {{ name }}!')
    buf = template.render(name="Joe")
    print(buf)

def test2():
    path = f"{os.path.dirname(__file__)}/j2"
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))
    template = env.get_template(f"0test.j2")
    buf = template.render(sports=['basketball', 'football', 'teniess', 'swiming'])
    genfilepath = f"genpy/autogen_sports.py"
    with open(genfilepath, 'w') as f:
        f.write(buf)

def test3():
    path = f"{os.path.dirname(__file__)}/j2"
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path))
    template = env.get_template(f"1test.j2")
    people = []
    with open(f"json/test.json", 'r') as f:
        people = json.load(f)['people']
    
    buf = template.render(name_sports=people)
    genfilepath = f"genpy/autogen_people_sports.py"
    with open(genfilepath, 'w') as f:
        f.write(buf)


def test4():
   path = f"{os.path.dirname(__file__)}/j2"
   env = jinja2.Environment(
       loader=jinja2.FileSystemLoader(path),
       trim_blocks=True,
       lstrip_blocks=False,
       extensions=["jinja2.ext.loopcontrols", "jinja2.ext.do"])
   template = env.get_template(f'2test.j2')
   template.globals["now"] = datetime.utcnow().strftime("%Y-%m-%d")
   buf = template.render(age={'ella': 15, 'tony': 19, 'jakey':14}, names=['tony', 'ella', 'jakey'])
   genfilepath = f"genpy/autogen.txt"
   with open(genfilepath, 'w') as f:
       f.write(buf)


if __name__ == '__main__':
    testj2()
    test2()
    test3()
    test4()