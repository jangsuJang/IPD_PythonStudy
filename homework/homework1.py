#-*- coding:utf-8 -*-
import ast

input_string = '''
{

'message': '2017. 11. 15. 오후 08:21:30 오늘 찌삼 다녀왔는데 주인분이 바뀌신 것 같았어요!! 이전 무한리필에서 우삼겹 삼겹은 그대로 인데 양념갈비가 빠지고 꽃목살 가브리살 등겹살..등등 으로 바뀌었는데 양념 절여달라고 하시면 달달짭짤항 양념도 고기에 해 주셔요! 고기도 가브리살 진짜 껍질 쫀득한게 너무 맛있네요 ㅠㅜ 주인분 너무 친절하고 너무 기분 좋게 먹고와서 제보합니다. 점심때 메뉴엔 없는데 학생분들 한정 떡만두국??이엇나 따로 판매하신다 들었어요!',

'reactions': {'data': [],
              'summary': {'total_count': 35}
             },

'created_time': '2017-11-16T01:25:07+0000',

'comments': { 'data': [ 
                        { 
                          'created_time': '2017-11-16T01:49:29+0000',
                          'message': '사장님 로그인 하셔야..',
                          'id': '1855249371432296_1855272548096645'
                        },
                        {
                           'created_time': '2017-11-16T01:  32:41+0000',
                           'message': '조*덕 금요일날 가자 ㅎ', 
                           'id':'1855249371432296_1855264341430799'
                        } 
                      ]
            }
}
'''
input_dic = ast.literal_eval(input_string)


#빈칸을 채워주세요

message = #todo 
like = #todo 
comment_one = #indo 
comment_two = #todo

##############

print("포스트의 내용은 : " + message)
print("*************")
print("좋아요의 갯수는 : " + str(like))
print("*************")
print("첫번째 덧글 내용은 : " + comment_one)
print("*************")
print("두번쨰 덧글 내용은 : " + comment_two)






