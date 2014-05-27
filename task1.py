# encoding: utf-8
class Address (object):
    def __init__ (self, index, city, street, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.apartment = apartment
    def __str__ (self):
        return ("%s, %s, %s, %s" %(self.index, self.city, self.street, self.apartment))
    @staticmethod
    def parse (address):
        a = Address(None, None, None, None)
        list = address.split(",")
        #print(address)
        s_index = list[0].strip()
        if s_index != '':
            try:
                a.index = int(s_index)
            except ValueError:
                pass
        a.city = list[1].strip()
        a.street = list[2].strip()
        a.apartment = int(list[3].strip())
        return a
#a = Address (394001, "Воронеж", "Ленина", 1)
#s = str(a)
#a.parse(s)
#print(a)
f = open('address.txt', 'rw+')
lines = f.readlines()
f.close()
w = []
wo = []
for line in lines:
    a = Address.parse(line)
    if a.index == None:
        wo.append(a)
    else:
        w.append(a)
print ("With index:")
for a in w:
    print(a)
print ("Without index:")
for a in wo:
    print(a)
    for i in w:
        if (a.city == i.city) and (a.street == i.street):
            a.index = i.index
            w.append(a)
            wo.remove(a)
            print("> Found: %s" %(a.index))
            break
    else:
        print("> Not found")
o1 = open('good.txt', 'w')
for item in w:
  o1.write("%s\n" % item)
o1.close()
o2 = open('bad.txt', 'w')
for item in wo:
  o2.write("%s\n" % item)
o2.close()
