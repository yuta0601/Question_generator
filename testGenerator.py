# -*- coding: utf-8 -*-
import random


def main():
    capitals = {
            '北海道': '札幌市',
            '青森県': '青森市',
            '岩手県': '盛岡市',
            '宮城県': '仙台市',
            '秋田県': '秋田市',
            '山形県': '山形市',
            '福島県': '福島市',
            '茨城県': '水戸市',
            '栃木県': '宇都宮市',
            '群馬県': '前橋市',
            '埼玉県': 'さいたま市',
            '千葉県': '千葉市',
            '東京都': '東京',
            '神奈川県': '横浜市',
            '新潟県': '新潟市',
            '富山県': '富山市',
            '石川県': '金沢市',
            '福井県': '福井市',
            '山梨県': '甲府市',
            '長野県': '長野市',
            '岐阜県': '岐阜市',
            '静岡県': '静岡市',
            '愛知県': '名古屋市',
            '三重県': '津市',
            '滋賀県': '大津市',
            '京都府': '京都市',
            '大阪府': '大阪市',
            '兵庫県': '神戸市',
            '奈良県': '奈良市',
            '和歌山県':'和歌山市',
            '鳥取県': '鳥取市',
            '島根県': '松江市',
            '岡山県': '岡山市',
            '広島県': '広島市',
            '山口県': '山口市',
            '徳島県': '徳島市',
            '香川県': '松江市',
            '愛媛県': '松山市',
            '高知県': '高知市',
            '福岡県': '福岡市',
            '佐賀県': '佐賀市',
            '長崎県': '長崎市',
            '熊本県': '熊本市',
            '大分県': '大分市',
            '宮崎県': '宮崎市',
            '鹿児島県': '鹿児島市',
            '沖縄県': '那覇市'
            }
    # 都道府県の順番をシャッフル
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)

    # 問題と正解の空ファイル
    with open('question.txt', 'w') as f:
        f.write('')

    with open('answer.txt', 'w') as f:
        f.write('')

    # 47都道府県をループしてそれぞれ問題を作成する
    for question_num in range(len(prefectures)):
        correct_answer = capitals[prefectures[question_num]]    # 正当のindexを取得
        wrong_answers = list(capitals.values())             # 辞書の値を全て取得しリスト化
        del wrong_answers[wrong_answers.index(correct_answer)]  # リストから正解を削除
        wrong_answers = random.sample(wrong_answers, 3)     # 誤答リストからランダムに3つ取得
        answer_option = wrong_answers + [correct_answer]    # 3つの誤答と正解を選択肢リストとする
        random.shuffle(answer_option)                   # 選択肢リストをシャッフル

        # 問題文と回答選択肢を問題ファイルに書く
        with open('question.txt', 'a') as f:
            f.write('{}. {}の都道府県庁所在地は?\n'.format(question_num + 1, prefectures[question_num]))
            # 選択肢
            for i in range(4):
                f.write(' {}. {}\n'.format('ABCD'[i], answer_option[i]))

            f.write('\n')

        with open('answer.txt', 'a') as f:
            # 答えの選択肢をファイルに書く
            f.write('{}. {}\n'.format(question_num + 1, 'ABCD'[answer_option.index(correct_answer)]))



if __name__=='__main__':
    main()