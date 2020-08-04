from itertools import combinations_with_replacement

# 테스트케이스의 번호
case = 1

# 0을 마주하기 전까지 계속해서 입력 받기
while (1):
	num_testcase = int(input())
	if num_testcase != 0:
		# 코드를 저장할 사전을 정의
		code = {}
		for _ in range(num_testcase):
			letters = input().split()
			code[letters[0]] = letters[1]
		# encrypted string
		string = []
		string.append(input())
		
		# may not be preceded by a 0 in the encrypted string
		# skip = list(string[0])
		# while('0' in string[len(string)-1]):
		# 	string.append(string[len(string)-1].remove('0'))
		# 0을 생략할 수 있는 부분이 아직 구현 미완성

		# 정답을 담을 리스트
		answer = []

		# encrypted string으로 해석될 수 있는 문자열을 answer 리스트에 담기
		for num_letter in range(1, len(string)+1):
			comb = list(combinations_with_replacement(code, num_letter))
			for p_case in comb:
				letter = ''
				for order in range(len(p_case)):
					letter += code[p_case[order]]
				if letter in string:
					answer.append(''.join(p_case))

		# 하나의 테스트케이스에 대해 정답 출력하기
		print("Case #" + str(case))
		case += 1
		for index in range(len(answer)):
			print(answer[index])
	else:
		break