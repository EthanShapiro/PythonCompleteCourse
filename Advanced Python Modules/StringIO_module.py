import io

message = 'This is just a normal string.'
f = io.StringIO(message)
print(f.read())
print(f.seek(0))
