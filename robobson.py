{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww26820\viewh13440\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def control(front_right, front_left, back_right, back_left, distance_right, distance_left):\
\
    if front_left > 0.25 or front_right > 0.25:\
        #se identificar a borda branca, parar\
        leftSpeed  = -20;\
        rightSpeed = -20;\
    elif back_left > 0.25:\
        leftSpeed = 30\
        rightSpeed =-30\
    elif distance_right < 300 and distance_left == 300:\
        # oponente na direita => vire a direita\
        leftSpeed  =  40;\
        rightSpeed = 40;\
    elif distance_right==300 and distance_left<300:\
        # oponente na esquerda => vira esquerda\
        leftSpeed  = 40;\
        rightSpeed =  40;\
    elif distance_right<300 and distance_left<300:\
        # oponente na frente => ataque\
        leftSpeed  = 40;\
        rightSpeed = 40;\
    elif distance_right==300 and distance_left==300:\
        # oponente perdido => procurar o oponente\
        leftSpeed  = 40;\
        rightSpeed =-20;\
\
        \
        \
    return \{\
        'leftSpeed':  leftSpeed  + 10,\
        'rightSpeed': rightSpeed + 10,\
        'log': [\
            \{ 'name': 'Distance Right', 'value': distance_right, 'min': 0, 'max': 300 \},\
            \{ 'name': 'Distance Left', 'value': distance_left, 'min': 0, 'max': 300 \}\
        ]\
    \}}