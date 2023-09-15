import csv
import pandas as pd

woody_set = set([
    '수지', '시가박스', '백단향', '생강', '백후추', '흑후추', '육두구', '넛맥',
    '곰팡이', '헝겊', '판지', '지하실', '연필', '코르크', '잉크', '금속', '장뇌향',
    '커스타드', '크림', '캐러멜', '머랭', '스펀지', '마데이라 케이크', '토피', '사탕',
    '쌀 푸딩', '탄 토스트', '커피', '펜넬', '아니시드', '감초'
])
feinty_set = set([
    '플라스틱 우비', '플라스틱 통', '플라스틱 끈', '방수포', '그을린 플라스틱',
    '버터밀크', '치즈', '효모', '느글느글한', '오래된 신발', '구두약',
    '말린 차', '찻 주전자', '신선한 담뱃잎', '풋담배', '담뱃재',
    '가죽장식', '도서관', '새 가죽소파', '다이제(비스킷)',
    '꿀', '잡초', '밀랍', '광택약'
])
winey_set = set([
    '아마씨 오일', '촛농', '선탠로션', '선탠오일', '아몬드 오일',
    '셰리', '샤도네이', '소테른', '피노', '돌로로소', '아르마냑', '포트와인',
    '견과 헤이즐넛', '호두', '아몬드 초콜릿', '마지팬(아몬드 과자)',
    '초콜렛', '크림', '버터', '우유', '초콜렛', '코코아', '비터', '버터'
])
peaty_set = set([
    '이끼', '이끼 낀 물', '늪지', '흙', '먼지', '어망', '대마', '자작나무',
    '약', '크레오소트', 'TCP', '요오드', '석탄산', '병원', '보풀', '타르', '디젤', '오일', '해초',
    '스모키', '피트(이탄)', '모닥불', '불에 탄 통나무', '재', '향',
    '훈제 생선', '훈제', '조개', '훈제 굴', '바다 조개', '훈제 연어', '앤초비'
])
cereal_set = set([
    '죽', '날곡물', '시리얼', '옥수수 요리', '삶은 감자',
    '조리된 채소', '채소', '감자 요리', '으깬 감자 요리', '스위트콘', '스웨덴 순무', '당근', '순무',
    '맥아', '마마이트', '겨', '소 여물', '케이크', '맥아유', '홀릭스(맥아 가루를 섞은 우유)',
    '껍질', '말린 홉', '마리화나', '대마초', '에일', '아이언 토닉', '생쥐', '김빠진 맥주',
    '효모', '돼지고기 소세지', '삶은 돼지고기', '그래비소스'
])
floral_set = set([
    '향기', '향수', '섬유유연제', '분말 세제', '코코넛', '라벤더', '공기청정기',
    '온실', '꽃집', '젖은 토마토 화분', '풋 토마토', '제라늄',
    '잎', '완두콩 껍질', '잘린 풀 냄새', '푸른 나무 잎', '전나무', '크리스마스 트리', '잣',
    '건초', '건초더미', '헛간', '잘린 건초 냄새', '헤더(야생화)', '허브', '세이지'])
fruity_set = set([
    '감귤', '오렌지', '키위', '천도복숭아', '레몬 라임', '오렌지 겉껍질', '오렌지 껍질',
    '과일', '사과', '배', '복숭아', '살구', '딸기', '과일샐러드',
    '조리된 과일', '사과 스튜', '잼', '보리 설탕', '마멀레이드', '당과',
    '말린 과일', '청포도', '건포도', '무화과', '살구', '자두', '믹스드 필', '다진 파이', '과일 케이크',
    '솔벤트', '풍선껌', '젖은 페인트', '매니큐어 리무버'])
sulphur_set = set([
    '채소', '양배추 물', '순무', '고인물', '콩나물',
    '석탄', '가스', '폭죽', '성냥', '성냥갑', '탄화물', '탄소화합물', '화약', '코르다이트',
    '고무', '연필 고무', '지우개', '새 타이어', '불에 탄 고무',
    '모래', '각 세탁한 세탁물', '전분', '린넨', '모래사장', '유황'])
# main ---------------------------------------------------------------------------------------------------------------------------------------
opnFile = open('blended_malt.csv', 'r', encoding='utf-8')
rdr = csv.reader(opnFile)

colArr = []
whiskies = []

for idx, line in enumerate(rdr):
    if idx == 0:
        colArr = line
    else:
        whiskies.append(line)
opnFile.close()

for idx, whisky in enumerate(whiskies):
    new_aroma = []
    targetVal = whisky[colArr.index('aroma')]
 
    # 불필요 데이터 치환
    targetVal = targetVal.replace('[', '')
    targetVal = targetVal.replace(']', '')
    targetVal = targetVal.replace('"', '')
    targetVal = targetVal.replace("'", '')
    targetVal = targetVal.replace(' ', '')
    targetVal = targetVal.replace('\n', '')
    targetVal = targetVal.replace('\t', '')
    targetVal = targetVal.strip()
    targetVal = targetVal.rstrip()
    targetVal = targetVal.lstrip()
    targetVal = targetVal.split(',')

    #print(targetVal)

    # 아로마 데이터 추가           
    for keyword in targetVal:
        if keyword in woody_set and "나무향" not in new_aroma:
            new_aroma.append("나무향")
        elif keyword in feinty_set and "잔류액향" not in new_aroma:
            new_aroma.append("잔류액향")
        elif keyword in winey_set and "와인향" not in new_aroma:
            new_aroma.append("와인향")
        elif keyword in peaty_set and "피트향" not in new_aroma:
            new_aroma.append("피트향")
        elif keyword in cereal_set and "곡물향" not in new_aroma:
            new_aroma.append("곡물향")
        elif keyword in floral_set and "꽃향기" not in new_aroma:
            new_aroma.append("꽃향기")
        elif keyword in fruity_set and "과일향" not in new_aroma:
            new_aroma.append("과일향")
        elif keyword in sulphur_set and "유황" not in new_aroma:
            new_aroma.append("유황")
        # else:
        #     new_aroma.append(keyword) 
#    print(whisky[colArr.index('nameKor')], new_aroma)
    whisky[colArr.index('aroma')] = new_aroma
    #print(whisky[colArr.index('nameKor')], list(set(new_aroma))) 중복제거
print(whiskies)

df = pd.DataFrame(whiskies)

df.to_csv("./outputs/blended_malt_1.csv", index=False, encoding='utf-8-sig')
