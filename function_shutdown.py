# design  function which returns the shut down when we pass yes 
#shutdown abort when pss no
#sorry when other thing is pssed

def shut_down(s):
    s1=s.lower()
    if s1=='yes':
        return 'shut down'
    elif s1=='no':
        return 'shutdown abort'
    else :
        return 'sorry'
out=shut_down(input('enter the option yes or no or other \n'))
print(out)