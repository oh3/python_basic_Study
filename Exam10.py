# 모듈

# import theater_modeul

# theater_modeul.price(3) # 3명이서 영화보러 갔을 때
# theater_modeul.price_morning(4) # 4명이서 조조할인
# theater_modeul.price_soldier(5) # 5명이서 군인할인

# 별명 붙혀서 사용
# import theater_modeul as mv

# mv.price(6)
# mv.price_morning(5)
# mv.price_soldier(3)

# 더 간단하게
# from theater_modeul import *
# from random import *
# price(3)
# price_morning(3)
# price_soldier(5)

# 2개만 갖다 쓸꺼야
# from theater_modeul import price, price_morning

# price(5)
# price_morning(5)

# 1개만 갖다 쓰면서 별명쓰기
from theater_modeul import price_soldier as price

price(5) #군인가격출력