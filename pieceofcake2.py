n, h, v = map(int, input().split())

ah = h
av = v

bh = h
bv = n - v

ch = n - h
cv = v

dh = n - h
dv = n - v

areas = [ah*av, bh*bv, ch*cv, dh*dv]
max_area = max(areas)
volumes = 4 * max_area

print(volumes)
