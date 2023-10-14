import json
from my_global import g_direct


def file_reader0(filename:str):
    with open(filename, 'r') as f:
        # for line in f:
        #     print(line)
        lines = f.readlines()
        print(lines)

def json_process(filename:str):
    with open(filename, 'w') as f:
        json.dump(g_direct, f)

    with open(filename, 'r') as f:
        # for line in f:
        #     print(line)
        # print(type(f.read()))
        # print(type(f))
        # print(type(f.readlines()))
        #direct1 = json.loads(f.read())
        direct2 = json.load(f)
        # for k, v in direct1.items():
        #     print(k.title())

        
        for k, v in direct2.items():
            if type(v) == type([]):
                for student in v:
                    print(student)
            #print(v)

if __name__ == "__main__":
    #file_reader0("./a.json")
    json_process("./b.json")