#! /usr/bin/env python

# python-mcdb "Example"

import mcdb

print
print(mcdb.__name__ + ' ' + mcdb.__version__)
print

## mcdb.make object

fn = "example.mcdb"

mk = mcdb.make(fn)
print(mk.__class__)
print("Creating %s (fd %d)" % (mk.name, mk.fd))

mk.add(b'123',      b'0123456789')
mk.add(b'abc',      b'def')
mk.add(b'alphabet', b'soup')
mk.add(b'123',      b'repeat')
mk.add(b'123',      b'again')

mk.finish()

del(mk)

## mcdb.read object

m = mcdb.read(fn)
m.madvise(mcdb.MADV_RANDOM)
print
print(m.__class__)

print("Reading mcdb %s (size %d)" % (m.name, m.size))
print

print(repr(m),'== example.mcdb')
print(len(m), '           == 5')

print(m['abc'],'         == def')
print(m.find('alphabet'),'        == soup')
print(m.get('123', 'error'),'  == 0123456789')
print(m.get('non-existent', '(dne)'),'       == (dne)')
print(m.getseq('123', 0),'  == 0123456789')
print(m.getseq('123', 1),'      == repeat')
print(m.getseq('123', 2),'       == again')

r = m.find('map')
while r is not None:
    print(r)
    r = m.findnext()
print

print(m.keys())
print

for k in m.keys():
  print(k, '=>', m.findall(k))

print
it = m.iteritems();
try:
    r = it.next()
    while r:
        print(r[0])
        r = it.next()
except StopIteration:
    True
print

if b'alphabet' in m:
    print('yes')
else:
    print('no')
print

m.madvise(mcdb.MADV_SEQUENTIAL)
def mcdb_dump(m):            # mcdbctl dump
    for r in m.iteritems():  # r = ('key', 'val')
        print("+%d,%d:%s->%s" % ( len(r[0]), len(r[1]), r[0], r[1] ))
    print

mcdb_dump(m)
