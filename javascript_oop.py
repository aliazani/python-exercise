class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)


d1 = JavaScriptObject({"Name": "ali"})

print(d1)
d1.language = 'python'
print(d1.language)
