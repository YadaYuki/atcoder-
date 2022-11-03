from math import sin,cos,radians


# ref: http://www.geisya.or.jp/~mwm48961/kou2/linear_image3.html
a,b,d = map(int,input().split())

cosd = cos(radians(d))
sind = sin(radians(d))

an = a * cosd- b * sind
bn = a * sind+ b * cosd

print(an,bn)