class FizzBuzz(object):

    def __init__(self,num):
        self.num = num

    def process(self):
        n = self.num

        if n%3==0 and n%5==0:
            ret = 'FizzBuzz'
        elif n%3==0:
            ret = 'Fizz'
        elif n%5==0:
            ret ='Buzz'
        else:
            ret = str(n)
        return ret