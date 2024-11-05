# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HIlVc84nbwTHxVkHzyFWWTFpp3yJd_yx
"""

import pandas as pd
baza={
    "FISH":[ "sodiqova mahliyo", "mamadaliyev zikrullo", "yusubov temur", "nematova dildora", "sulaymonova mahliyo", "komilova dinara", "soliyeva oydinoy", "raxmonova feruza", "xusanova robiya", "sharipova azizaxon"  ],
    "YOSHI":[ '19', '19', '19', '19', '19', '19', '19', '19', '19', '19'],
    "MAKTABI":[ '18-maktab', '20-maktab', '30-maktab', '48-maktab', '53-maktab', '699-maktab','787-maktab', '823-maktab', '98-maktab', '199-maktab'  ],
    "JINSI":[ 'qiz bola', 'ogil bola', 'ogil bola', 'qiz bola', 'qiz bola', 'qiz bola', 'qiz bola', 'qiz bola', 'qiz bola', 'qiz bola' ],
    "MAZILI":[ 'fargona', 'andijon', 'shaxrisabiz', 'samarqand', 'rossiya', 'margilon', 'xarazm', 'toshkent', 'nuks', 'qoraqalpoq'  ]
}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['JINSI']=="qiz bola"]
print(filtr)

filtr=db[(db['JINSI']=="qiz bola") & (db['MAZILI']=='nuks')]
print(filtr)