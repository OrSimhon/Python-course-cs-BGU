class System:
    def __init__(self):
        self.online_users = []

    @staticmethod
    def register(name, password):
        try:
            f = open('./users.txt', 'r')
        except:
            print("Congrats! You are the first user!")
        else:
            for line in f:
                if name == line.strip().split()[0]:
                    f.close()
                    raise ValueError(name + " is taken, choose different one")
            f.close()

        f = open('./users.txt', 'a')
        f.write(name + " " + password + '\n')
        f.close()

        print(name + " hast been registered!")

    def login(self, name, password):
        if name in self.online_users:
            print(name + " is already logged in!")
            return
        try:
            f = open('./users.txt', 'r')
        except:
            print("No registered users yet!")
            return
        else:
            for line in f:
                line = line.strip().split()
                if name == line[0] and password == line[1]:
                    self.online_users.append(name)
                    print(name + " has logged in!")
                    f.close()
                    return
            f.close()
        print("Wrong username or password!")


s = System()

# Register examples
# s.register('Hanna', '123123351')
# s.register('Amir', '68464651')

try:
    s.register('Bob', 'wrong_pass')
except Exception as e:
    print(e)

s.login('Hanna', '123123351')
s.login('Amir', '68464651')
