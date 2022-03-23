obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

lst = []
def collectStrings(obj):
    for x in obj:
        if not isinstance(obj[x], dict):
            if isinstance(obj[x], str):
                if obj[x] not in lst:
                    lst.append(obj[x])
        else:
            collectStrings(obj[x])
    return lst

print(collectStrings(obj))
