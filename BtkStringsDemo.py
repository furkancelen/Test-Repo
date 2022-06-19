website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
print(result)
# 2- 'website' içinden www karakterlerini alın.
substring = website[7:10]
print(substring)
# 3- 'website' içinden com karakterlerini alın.
_substring = website[-3:]
print(_substring)
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
__substring = course[:15] + course[-15:]
print(__substring)
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
reverse = course[::-1]
print(reverse)

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

#  6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32, mesleğim mühendis.'

print(f"Benim adım {name} {surname}, Yaşım {age}, mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini "W" ile değiştirin.

mystring = "Hello world"

print(mystring[0:6] + "W" + mystring[-4:])


# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

s = "abc"

print(s * 3) 