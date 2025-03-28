#インポート

#グローバル変数の宣言
ELEMENT_SYMBOLS={
        '火':'$',
        '水':'~',
        '土':'@',
        '風':'#',
        '命':'&',
        '無':' '
        }
ELEMENT_COLORS={
        '火':1,
        '水':6,
        '土':3,
        '風':2,
        '命':5,
        '無':7
        }

#関数宣言

def main():
    monster_list=[
            {'name':'スライム',
             'hp':100,
             'max_hp':100,
             'element':'水',
             'ap':10,
             'dp':1},
            {'name':'ゴブリン',
             'hp':200,
             'max_hp':200,
             'element':'土',
             'ap':20,
             'dp':5},
            {'name':'オオコウモリ',
             'hp':300,
             'max_hp':300,
             'element':'風',
             'ap':30,
             'dp':10},
            {'name':'ウェアウルフ',
             'hp':400,
             'max_hp':400,
             'element':'風',
             'ap':40,
             'dp':15},
            {'name':'ドラゴン',
             'hp':600,
             'max_hp':600,
             'element':'火',
             'ap':50,
             'dp':20}
            ]
    friends=[
            {'name':'青龍',
             'hp':150,
             'max_hp':150,
             'element':'風',
             'ap':15,
             'dp':10},
            {'name':'朱雀',
             'hp':150,
             'max_hp':150,
             'element':'火',
             'ap':25,
             'dp':10},
            {'name':'白虎',
             'hp':150,
             'max_hp':150,
             'element':'土',
             'ap':20,
             'dp':5},
            {'name':'玄武',
             'hp':150,
             'max_hp':150,
             'element':'水',
             'ap':20,
             'dp':15}
            ]
    while True:
        player_name=input('プレイヤー名を入力してください>')
        if len(player_name) > 0:
            break
        print('エラー:プレイヤー名を入力してください')

    print('*** Puzzle & Monsters ***')
    party = orgnize_party(player_name,friends)
    kills=go_dungeon(party,monster_list)
    if kills == len(monster_list):
        print('*** GAME CLEARED!! ***')
    else:
        print('*** GAME OVERA ***')
    print(f'倒したモンスター数={kills}')

def do_battle(monster):
    print_monster_name(monster)
    print('が現れた!')
    print_monster_name(monster)
    print('を倒した!')
    return 1

def print_monster_name(monster):
    monster_name=monster['name']
    symbol=ELEMENT_SYMBOLS[monster['element']]
    color=ELEMENT_COLORS[monster['element']]

    #モンスター名を表示
    print(f'\033[3{color}m{symbol}{monster_name}{symbol}\033[0m',end='')

def go_dungeon(party,monster_list):
    kills =0
    print(f'{party['name']}のパーティー(HP={party['hp']})はダンジョンに到達した!')
    show_party(party)
    for m in monster_list:
            kills += do_battle(m)
            if party['hp'] <= 0:
                print(f'{party['name']}はダンジョンから逃げ出した')
                break
            print(f'{party['name']}はさらに奥に進んだ')
            print('======================')
    print(f'{party['name']}はダンジョンを制覇した!')
    return kills

def orgnize_party(player_name,friends):
    total_hp= -40
    total_dp=0
    for f in friends:
        total_hp += f['hp']
        total_hp += f['dp']

    party ={
            'name':player_name,
            'friends':friends,
            'hp':total_hp,
            'max_hp':total_hp,
            'dp':total_dp / len(friends)
            }
    return party

def show_party(party):
    print('<パーティー編成>----------')
    for f in party['friends']:
        print_monster_name(f)
        print(f' HP= {f['hp']}')
        print(f' 攻撃= {f['ap']}')
        print(f' 防御= {f['dp']}')
    print('--------------------------')
        
#メイン関数の呼び出し
main()
