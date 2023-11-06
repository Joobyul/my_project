import csv

DEBUG=True

dirpath="C:\\Users\\LG\\Desktop\\새 폴더\\work&test.py\\"
filename=dirpath+"GolfMemberInfo.csv"
if DEBUG: print(f'filename => {filename}')

# 골프회원정보 클래스 만들기
class GolfMemberInfo(Exception):
    def __init__(self, filename):
        self.filename = filename
        self.members = []

    def load_members(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.members = list(reader)
        except FileNotFoundError:
            self.members = []

    def save_members(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            fieldnames = ['name', 'score', 'distance', 'experience']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.members)


    def add_member(self, name, score, distance, experience):
        for member in self.members:
            if member['name'] == name:
                print("이미 존재하는 회원입니다.")
                return

        member = {
            'name': name,
            'score': score,
            'distance': distance,
            'experience': experience
        }
        self.members.append(member)
        self.save_members()

    def get_lowest_score_member(self):
        lowest_score_member = min(self.members, key=lambda x: x['score'])
        return lowest_score_member

    def get_highest_distance_member(self):
        highest_distance_member = max(self.members, key=lambda x: x['distance'])
        return highest_distance_member

    def get_longest_experience_member(self):
        longest_experience_member = max(self.members, key=lambda x: x['experience'])
        return longest_experience_member


# 클래스 객체 만들기
golf_club = GolfMemberInfo('GolfMemberInfo.csv')
golf_club.load_members()

# 회원 정보 입력 받기
while True:
    name = input("회원 이름을 입력하세요 (종료하려면 'q' 입력): ")

    if name == 'q':
        break

    score = int(input("회원의 타수를 입력하세요: "))
    distance = int(input("회원의 비거리를 입력하세요: "))
    experience = int(input("회원의 경력을 입력하세요: "))

    golf_club.add_member(name, score, distance, experience)

# 타수가 가장 적은 회원 출력
lowest_score_member = golf_club.get_lowest_score_member()
print("타수가 가장 적은 회원:", lowest_score_member['name'])

# 비거리가 가장 많이 나온 회원 출력
highest_distance_member = golf_club.get_highest_distance_member()
print("비거리가 가장 많이 나온 회원:", highest_distance_member['name'])

# 구력이 가장 오래된 회원 출력
longest_experience_member = golf_club.get_longest_experience_member()
print("경력이 가장 오래된 회원:", longest_experience_member['name'])
