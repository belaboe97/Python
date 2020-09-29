# SOLVING PROBLEM WITH DECORATOR FUNCTION

#def main(some_other_func):
#     
#    def wrap_func():
#
#        print('step1')
#        print('step2')
#        print('step3')
#        some_other_func()
#        print('step7')
#        print('step8')
#        print('step9')

#    return wrap_func

#@main
#def steps():
#    print('step4')
#    print('step5')
#    print('step6')

#decorated_func =  main(steps)
#decorated_func()

#OFFICAL SOLVING OF PROBLEM

def steps(x,y):
    for i in range(x,y+1):
        print('step'+ str(i))

def main():
    print('step1')
    print('step2')
    print('step3')
    steps(4,10)

main()

