number = 100
day= 'three'
# %s = string %c 문자 1개 %d integer %f float %o 8진수 %x 16진수 %% Literal%(문자 %)
a = 'I ate %d apples, so I was sick for %s days.' %(number, day)
b = '1ddafsasd  {} dasfajlkdjfal'.format("{}사이에 문자열이 들어가나?")
c = 'hello {name} {age}'.format(name='kyubum', age=26)
name = 'kyubum'
d = f"나의 이름은 {name} 입니다."

print(a)
print(b)
print(c)
print(d)