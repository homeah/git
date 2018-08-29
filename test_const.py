import const
const.NAME = 'FishC'
print(const.NAME)
try:
    const.NAME = "Fishc.com"
    print(const.NAME)
except TypeError as Err:
    print(Err)
try:
    const.name = 'FishC'
except TypeError as Err:
    print(Err)
