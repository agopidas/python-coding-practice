def reverse_string(n):

    str = ""
    for i in n:
        str=i+str
    return str


a=reverse_string("abhilash")
print(a)


def reverse(string):
    string="".join(reversed(string))
    return string

a=reverse("abhilash")
print(a)


