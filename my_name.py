thickness = int(input())
x = -1

for i in range(thickness):
    print(("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + 'x'*thickness + ('x'*thickness).rjust(thickness*3 - (i+1)) + ('x'*(thickness*4)).rjust(thickness*5 + i+1) + ('x'*(thickness)).center(thickness*3) + ('x'*(thickness)).center(thickness*3) + 'x'*(thickness*4))

for i in range(thickness):
    print(('x'*thickness).ljust(thickness*2) + ('x'*thickness).center(thickness*3) + ('x'*thickness).ljust(thickness*2) + ('x'*thickness).center(thickness*3) + ('x'*thickness).ljust(thickness*2) + ('x'*thickness).center(thickness*3) + ('x'*thickness).ljust(thickness*5) + 'x'*thickness + ('x'*thickness).rjust(thickness*2 - (i+1)) + ('x'*thickness).rjust(thickness*3 + i+1) + ('x'*thickness).rjust(thickness*5) + ('x'*thickness).rjust(thickness*3) + ('x'*thickness).rjust(thickness*2) + ('x'*thickness).rjust(thickness*3))

for i in range(thickness):
    if(x<0):
        print(("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ('x'*(thickness+x+4)).ljust(thickness*2) + ('x'*(thickness*4)).rjust(thickness*7 ) + ('x'*(thickness*4)).rjust(thickness*5) + ('x'*(thickness*4)).rjust(thickness*5))
        x+=1
    else:
        print(("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ("x"*thickness*4).ljust(thickness*5) + ('x'*(thickness+i+1)).ljust(thickness*2) + ('x'*(thickness*4)).rjust(thickness*7 ) + ('x'*(thickness*4)).rjust(thickness*5) + ('x'*(thickness*4)).rjust(thickness*5))

for i in range(thickness):
    print(('x'*thickness).ljust(thickness*5) + ('x'*thickness).ljust(thickness*2) + ('x'*thickness).center(thickness*3) + 'x'*thickness + ('x'*thickness).rjust(thickness + (i+1)) + ('x'*thickness).rjust(thickness * 4 - (i+1)) + ('x'*thickness).rjust(thickness*5) + ('x'*thickness).rjust(thickness + (i+1)) + ('x'*thickness).rjust(thickness*7 - (i + 1 )) + ('x'*thickness).rjust(thickness*2) + ('x'*thickness).rjust(thickness*3) + ('x'*thickness).rjust(thickness*2) + ('x'*thickness).rjust(thickness*3))

for i in range(thickness):
    print(('x'*thickness).ljust(thickness*5) + ('x'*thickness).ljust(thickness*2) + ('x'*thickness).center(thickness*3) + 'x'*thickness + ('x'*thickness).rjust(thickness*2 + (i+1)) + ('x'*thickness).rjust(thickness * 3 - (i+1)) + ('x'*thickness*3).ljust(thickness*4) + ('x'*thickness).ljust(thickness*2) + ('x'*thickness).rjust(thickness + (i+1)) + ('x'*(thickness*4)).rjust(thickness*6 - (i + 1)) +  ('x'*thickness).rjust(thickness*2) + ('x'*thickness).rjust(thickness*3) + ('x'*thickness).rjust(thickness*2) + ('x'*thickness).rjust(thickness*3))
