import json
from my_global import g_direct


def file_reader0(filename:str):
    """file reader

    Args:
        filename (str): input is file path
    """
    with open(filename, 'r') as f:
        # for line in f:
        #     print(line)
        lines = f.readlines()
        print(lines)

def json_process(filename:str):
    """json process func

    Args:
        filename (str): file path

    Returns:
        _type_: alwalys return true
    """ 
    with open(filename, 'w') as f:
        json.dump(g_direct, f, indent=4)

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
        return True

def test_dict_jsons_conver():
    dict = {"name": "Ally", "age": 15}

    # 1. from python dict to a json str
    j = json.dumps(dict)
    print(j)
    print(f"j is a {type(j)}")

    # 2. from json str to python dict
    dict2 = json.loads(j)
    print(f"dict2 is a {type(dict2)}")
    print(dict2)

    # json file to python dict 
    with open("a.json", 'r') as f_obj:
        j_dict = json.load(f_obj)
        print(f"j_dict is {type(j_dict)}")
        print(j_dict)
        # python dict to a json file
        with open("c.json", 'w+') as f:
            json.dump(j_dict, f, indent=4)


if __name__ == "__main__":
    #file_reader0("./a.json")
    json_process("./b.json")
    test_dict_jsons_conver()