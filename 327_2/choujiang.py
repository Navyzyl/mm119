import random
names=['aaa','bbb','ccc']
passwords=['111','222','333']
cards=['1565','4546','4664']

denglu_name='aaa'
denglu_password='111'
denglu_card='1565'
rum_num=random.randint(0,9)
print('****************抽奖**************')
if denglu_name is not None and denglu_card is not None:
    print(f'{denglu_name}你的卡号为{denglu_card}')
    if str(rum_num)==denglu_card[-1]:
        print(f'恭喜您获奖，本次中奖数字为{rum_num}')
    else:
        print(f'很遗憾，你没中奖，本次中奖数字为{rum_num}')
else:
    print('需登陆账号进行抽奖')