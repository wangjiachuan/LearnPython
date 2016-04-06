import json
def compare_json(a, b):
    aa = json.loads(a)
    bb = json.loads(b)

    print(aa)
    print(bb)

    len_a = len(aa)
    len_b = len(bb)
    if len_a != len_b:
        return False
    else:
        for key in aa:
            if not bb.has_key(key):
                return False
            else:
                if sorted(aa[key]) != sorted(bb[key]):
                    return False
    return True
                    

if __name__ == "__main__":
    a = '{"ROAD": [{"id": 123}, {"name": "no1"}]}'
    b = '{"ROAD": [{"name": "no1"}, {"id": 123}]}'
    print compare_json(a, b)
