Node = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e" ]
TimeTable = []
Morning = [ 
    #. A   B.  C.  D.  E.  F.  G.  H.  I.  J.  K.  L.  M.  N.  O.  P.  Q.  R.  S.  T.  U.  V.  W.  X.  Y.  Z.  a.  b.  c.  d.  e.
    [  0, 15,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # A
    [  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # B
    [  0,  0,  0,  3,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # C
    [  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10,  0 ], # D
    [  0,  0,  0,  0,  0, 30,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0 ], # E
    [  0,  0,  0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # F
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # G
    [  0,  0,  0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # H
    [  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # I
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # I
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # K
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # L
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0 ], # M
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 39,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0 ], # N
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 33,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # Q
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # P
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # Q
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # R
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # S
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # T
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # U
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # V
    [  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # W
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0 ], # X
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # Y
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 24,  0,  0,  0,  0 ], # Z
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 17,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # a
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0 ], # b
    [  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # c
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10 ], # d
    [  0,  0,  0,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]  # e
]
TimeTable.append(Morning)
Peak = [
    #. A   B.  C.  D.  E.  F.  G.  H.  I.  J.  K.  L.  M.  N.  O.  P.  Q.  R.  S.  T.  U.  V.  W.  X.  Y.  Z.  a.  b.  c.  d.  e.
    [  0, 19,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  4,  0,  0,  0,  0,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 13,  0 ],
    [  0,  0,  0,  0,  0, 38,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 49,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 42,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 32,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 25,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 30,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 22,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0 ],
    [  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 13 ],
    [  0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
]
TimeTable.append(Peak)
Evening = [
    #. A   B.  C.  D.  E.  F.  G.  H.  I.  J.  K.  L.  M.  N.  O.  P.  Q.  R.  S.  T.  U.  V.  W.  X.  Y.  Z.  a.  b.  c.  d.  e.
    [  0, 17,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # A
    [  0,  0, 18,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # B
    [  0,  0,  0,  4,  0,  0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # C 
    [  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11,  0 ], # D
    [  0,  0,  0,  0,  0, 33,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0 ], # E
    [  0,  0,  0,  0,  0,  0, 18,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # F
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # G 
    [  0,  0,  0,  0,  0,  0,  0,  0,  9,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # H
    [  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # I
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # J
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # K 
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # L 
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0 ], # M 
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 43,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0 ], # N 
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 37,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # O
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # P
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 28,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # Q
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 22,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # R
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # S
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # T
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # U
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # V 
    [  0,  0,  0,  0,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # W 
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  0,  0,  0,  0,  0,  0 ], # X
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # Y
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 27,  0,  0,  0,  0 ], # Z
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 19,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # a
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  3,  0,  0 ], # b 
    [  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ], # c
    [  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 11 ], # d
    [  0,  0,  0,  0,  0,  0,  9,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]  # e
]
TimeTable.append(Evening)

import time
import random
import argparse

def UCS(Start, Goal, StartTime):
  # 字串轉時間
  StartTimeStamp = int(StartTime[0:2]) * 60 * 60 + int(StartTime[2:4]) * 60 + int(StartTime[4:6])
  IntervalTime_1 = "000000"
  IntervalTimeStamp_1 = int(IntervalTime_1[0:2]) * 60 * 60 + int(IntervalTime_1[2:4]) * 60 + int(IntervalTime_1[4:6])
  IntervalTime_2 = "070000"
  IntervalTimeStamp_2 = int(IntervalTime_2[0:2]) * 60 * 60 + int(IntervalTime_2[2:4]) * 60 + int(IntervalTime_2[4:6])
  IntervalTime_3 = "190000"
  IntervalTimeStamp_3 = int(IntervalTime_3[0:2]) * 60 * 60 + int(IntervalTime_3[2:4]) * 60 + int(IntervalTime_3[4:6])
  IntervalTime_4 = "235959"
  IntervalTimeStamp_4 = int(IntervalTime_4[0:2]) * 60 * 60 + int(IntervalTime_4[2:4]) * 60 + int(IntervalTime_4[4:6])

  # 變數宣告
  FrontierNode = []
  FrontierCost = []
  ES = []

  # 初始化
  FrontierNode.append(Start)
  FrontierCost.append(0)

  Check = True
  IntervalID = 0

  while (Check):
    # 判斷Frontier是否為空
    if not FrontierNode:
        break

    MinValueID = FrontierCost.index(min(FrontierCost)) # 找出Frontier中Cost的最小值
    # 以下兩行為擷取往下搜尋的父節點
    ActiveFrontierName = FrontierNode[MinValueID] 
    LastActiveFrontierNode = ActiveFrontierName[len(ActiveFrontierName) - 1]
    # 確認該搜尋父節點的節點編號
    NodeID = Node.index(LastActiveFrontierNode)
  
    # 確認目前的時間區段
    ActiveTimeStamp = StartTimeStamp + FrontierCost[MinValueID] * 60
    if IntervalTimeStamp_1 <= ActiveTimeStamp < IntervalTimeStamp_2:
      IntervalID = 0
    elif IntervalTimeStamp_2 <= ActiveTimeStamp < IntervalTimeStamp_3:
      IntervalID = 1
    elif IntervalTimeStamp_3 <= ActiveTimeStamp <= IntervalTimeStamp_4:
      IntervalID = 2
    else:
      IntervalID = 0

    # 確認單方向的其中一種可能
    for i in range(len(Node)):
      # 確認有這條路線，並且也未走過
      if TimeTable[IntervalID][NodeID][i] != 0 and ActiveFrontierName.find(Node[i]) == -1:
        NodeName = FrontierNode[MinValueID] + Node[i]
        FrontierNode.append(NodeName)
        FrontierCost.append(FrontierCost[MinValueID] + TimeTable[IntervalID][NodeID][i])
        # 確認是否已到達終點
        if Node[i] == Goal:
          Check = False
          break
      # 確認有這條路線，並且也未走過
      elif TimeTable[IntervalID][i][NodeID] != 0 and ActiveFrontierName.find(Node[i]) == -1:
        NodeName = FrontierNode[MinValueID] + Node[i]
        FrontierNode.append(NodeName)
        FrontierCost.append(FrontierCost[MinValueID] + TimeTable[IntervalID][i][NodeID])
        # 確認是否已到達終點
        if Node[i] == Goal:
          Check = False
          break

    ES.append(FrontierNode[MinValueID])
    FrontierNode.pop(MinValueID)
    FrontierCost.pop(MinValueID)

  return NodeName, FrontierCost[len(FrontierCost) - 1]

parser = argparse.ArgumentParser()
parser.add_argument("PassPoint", help = "請輸入字串")

args = parser.parse_args()
PassPoint = args.PassPoint

# 基本參數設定
Parents = 30
Iteration = 150
MutationRate = 0.55
StartTime = "080000"
Generation = []

# 初始化
def Initiate(PassPoint, Parents):
  Generation.clear()
  for i in range(Parents):
    RandomList = random.sample(PassPoint, len(PassPoint))
    Generation.append(RandomList)
  return Generation

# 評估基因
def Evaluation(Parents, PassPoint, Generation):
  Result = []
  for i in range(Parents):
    Sum = 0
    for j in range(len(PassPoint) - 1):
      Path, Time = UCS(Generation[i][j], Generation[i][j + 1], StartTime)
      Sum = Sum + Time
    Result.append(Sum)
  return Result

# 選擇基因
def Reproduction(Result):
  TempA = []
  for i in range(len(Result)):
    TempA.append(1 / Result[i])
  Sum = 0
  TempB = []
  TempB.append(0)
  for j in range(len(TempA)):
    Sum = Sum + TempA[j] / sum(TempA)
    TempB.append(Sum)
  RV = []
  while (len(RV) < 2):
    RandomNumber = random.random()
    for k in range(len(TempB)):
      if (TempB[k] < RandomNumber <= TempB[k + 1]):
        RV.append(k)
  return RV

# 交配
def Crossover(Parents, PassPoint, Generation, RV):
  DNA_1 = Generation[RV[0]]
  DNA_2 = Generation[RV[1]]
  Generation.clear()
  i = 0
  if len(PassPoint) <= 3:
    while (i < Parents):
      R = random.randint(0, len(PassPoint) - 1)
      Region_1 = []
      Region_2 = []
      for j in range(0, R, 1):
        Region_1.append(DNA_1[j])
        Region_2.append(DNA_2[j])
      P1 = []
      P2 = []
      for j in range(len(PassPoint)):
        if DNA_2[j] not in Region_1:
          P2.append(DNA_2[j])
        if DNA_1[j] not in Region_2:
          P1.append(DNA_1[j])
      Generation.append(DNA_1[0 : R] + P2)
      Generation.append(DNA_2[0 : R] + P1)   
      i = i + 2
  else:
    while (i < Parents):
      R1 = random.randint(1, len(PassPoint) - 2)
      R2 = random.randint(1, len(PassPoint) - 2)
      Region_1 = []
      Region_2 = []
      if R1 < R2:
        for j in range(R1, R2 + 1):
          Region_1.append(DNA_1[j])
          Region_2.append(DNA_2[j])
      elif R1 > R2:
        for j in range(R2, R1 + 1):
          Region_1.append(DNA_1[j])
          Region_2.append(DNA_2[j])
        Temp = R1
        R1 = R2
        R2 = Temp
      else:
        continue
      P1 = []
      P2 = []
      for j in range(len(PassPoint)):
        if DNA_2[j] not in Region_1:
          P2.append(DNA_2[j])
        if DNA_1[j] not in Region_2:
          P1.append(DNA_1[j])
      Generation.append(P2[0 : R1] + DNA_1[R1 : R2 + 1] + P2[R1 :])
      Generation.append(P1[0 : R1] + DNA_2[R1 : R2 + 1] + P1[R1 :])
      i = i + 2
  return Generation

# 突變
def Mutation(Generation, Parents, MutationRate):
  for i in range(Parents):
    RandomNumber = random.random()
    if RandomNumber < MutationRate:
      R1 = random.randint(0, len(PassPoint) - 1)
      R2 = random.randint(0, len(PassPoint) - 1)
      Generation[i][R2], Generation[i][R1] = Generation[i][R1], Generation[i][R2]
  return Generation

Generation = Initiate(PassPoint, Parents)
Result = Evaluation(Parents, PassPoint, Generation)
ShortestTime = 10000
ShortestPath = ""
for i in range(Iteration):
  Min = min(Result)
  if Min < ShortestTime:
    ShortestPath = ""
    ShortestTime = Min
    Index = Result.index(Min)
    for j in range(0, len(PassPoint) - 1):
      Path, Time = UCS(Generation[Index][j], Generation[Index][j + 1], StartTime)
      if j == 0:
        for k in range(0, len(Path)):
          ShortestPath = ShortestPath + Path[k]
      else:
        for k in range(1, len(Path)):
          ShortestPath = ShortestPath + Path[k]

  RV = Reproduction(Result)
  Generation = Crossover(Parents, PassPoint, Generation, RV)
  Generation = Mutation(Generation, Parents, MutationRate)
  Result = Evaluation(Parents, PassPoint, Generation)

#print(ShortestTime)
#print(ShortestPath)
#print(Result)
Output = "([" + str(ShortestPath) +"]," + str(ShortestTime) + ")"
print(Output)



