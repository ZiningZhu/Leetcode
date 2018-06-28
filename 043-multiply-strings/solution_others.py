# Cheating solution
return str(int(num1) + int(num2))

# Manually convert to int, multiply, then convert back:
class Solution(object):
    def multiply(self, num1, num2):

        d ={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        d1 ={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

        n1 = 0
        n2 = 0
        l1 = len(num1)
        l2 = len(num2)
        for c,i in enumerate(num1):

            n1+= d[i]*10**(l1-c-1)

        for c, i in enumerate(num2):
            n2+= d[i]*10**(l2-c-1)


        prod = n1*n2
        print(prod)
        if prod ==0:
            return "0"
        l = []
        while prod:
            d, r = divmod(prod, 10)
            l.append(d1[r])
            prod = d

        s = ""
        for i in l[::-1]:
            s = s+ i

        return(s)
