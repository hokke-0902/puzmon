#インポート

#グローバル変数の宣言

#関数宣言

def main():
    player_name=input('プレイヤー名を入力してください')
    print('*** Puzzle & Monsters ***')
    kills=go_dungeon(player_name)
    print('*** GAME CLEARED!! ***')
    print(f'倒したモンスター数={kills}')

def go_dungeon(player_name):
    print(f'{player_name}はダンジョンに到達した!')
    print(f'{player_name}はダンジョンを制覇した!')
    return 5

#メイン関数の呼び出し
main()
