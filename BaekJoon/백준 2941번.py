##함수 선언 부분##

##변수 선언 부분##
Str = []
##메인 함수 부분##
if __name__ == "__main__" :
    Str = input()
    Str = Str.replace('c=','1')
    Str = Str.replace('c-', '1')
    Str = Str.replace('dz=', '1')
    Str = Str.replace('d-', '1')
    Str = Str.replace('lj', '1')
    Str = Str.replace('nj', '1')
    Str = Str.replace('s=', '1')
    Str = Str.replace('z=', '1')

    print("%d"%len(Str))