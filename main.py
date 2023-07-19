class Toggle:
    def Toggle(self, str):
        s = ""
        for i in str:
            o = ord(i)
            if o >= 65 and o <= 97:
                s += chr(o + 32)
            else:
                s += chr(o - 32)

        return s
string = input()
object = Toggle()
print(object.Toggle(string))