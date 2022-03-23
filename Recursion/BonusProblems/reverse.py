def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]

print("Reverse of {} is {}".format("python", reverse("python")))
print("Reverse of {} is {}".format("appmillers", reverse("appmillers")))
print("Reverse of {} is {}".format("0123456789", reverse("0123456789")))
