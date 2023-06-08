#!/usr/bin/env python3
class Polynomial(object):
    def __init__(self, *args, **kwargs):
        self.numbers = []
        for elem in args:
            if type(elem) is list:
                self.numbers = elem
        
        
        if not self.numbers:
            if args:
                self.numbers = list(args) 
            else:
                for name,value in kwargs.items():
                    for i in range(1+int(name.split("x")[1])-len(self.numbers)):
                        self.numbers.append(0)
                    self.numbers[int(name.split("x")[1])]=value


        for i in range(len(self.numbers)-1, 0, -1):
            if self.numbers[i] == 0:
                del self.numbers[i]
            else:
                break 

    def __str__(self):
        polynom=""
        #polynom with length 1
        if len(self.numbers) == 1:
            polynom += str(self.numbers[0])
            return polynom

        for i in reversed(range(len(self.numbers))):
            #conficien is zero => no value
            if self.numbers[i]==0:
                continue
            #add number sign
            if polynom:
                if self.numbers[i]>0: 
                    polynom+= " + "
                else:
                    polynom+= " - "
            if i == 0:
                polynom+= "{0}".format(str(abs(int((self.numbers[0])))))
                return polynom
            if i == 1:
                if abs(self.numbers[1]) == 1:
                    polynom += "x"
                else:
                    polynom += "{0}x".format(str(abs(int(self.numbers[1]))))
            else:
                if abs(self.numbers[i]) == 1:
                    polynom += "x^{0}".format(i)
                else:
                    polynom += "{0}x^{1}".format(str(abs(int(self.numbers[i]))), i)
        return polynom
        
    def __eq__(self, second_pol):
        if str(self) == str(second_pol):
            return True
        return False

    def derivative(self):
        buff = self.numbers.copy()
        del buff[0]     #derivation of number is zero
        for i in range(len(buff)):
            buff[i]=buff[i]*(i+1)
        return Polynomial(buff)

    def at_value(self, x1, x2=None):
        res = self.numbers[-1]
        for i in reversed(range(len(self.numbers)-1)):
            res=(res*x1)+self.numbers[i]
        if not x2:
            return res
        else:
            res2=self.numbers[-1]
        for i in reversed(range(len(self.numbers)-1)):
            res2=(res2*x2)+self.numbers[i]
        return res2-res

    def __mul__(self, second_pol):
        buff = [0]*(1 + len(self.numbers) + len(second_pol.numbers))
        for i in range(len(self.numbers)):
            for j in range(len(second_pol.numbers)):
                buff[i+j] += self.numbers[i]*second_pol.numbers[j]
        return Polynomial(buff)

    def __pow__(self, n):
        if n < 0:
            raise ValueError("Wrong value")
        if n == 0: 
            return 1
        if n == 1:
            return Polynomial(self.numbers)
        if n > 1:
            buff = self
            for i in range(n-1):
                buff *= self
            return Polynomial(buff)

