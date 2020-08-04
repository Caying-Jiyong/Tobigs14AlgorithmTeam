# 테스트케이스의 수
num_testcase = int(input())

# 총 클릭수 구하기
for case in range(num_testcase):
	string = list(input())
	answer = 0
	for index in range(len(string)):
		# 알파벳 r까지는 3칸마다 클릭수 초기화
		if 0 <= ord(string[index]) - ord('a') + 1 <= 18:
			num_click = (ord(string[index]) - ord('a') + 1) % 3
			if num_click == 0:
				num_click = 3
		# 알파벳 s와 z의 경우 4라는 클릭수를 가짐
		elif string[index] == 's' or string[index] == 'z':
			num_click = 4
		# 공백 문자의 경우 1이라는 클릭수를 가짐
		elif string[index] == ' ':
			num_click = 1
		# 4칸마다 초기화되는 경우
		else:
			num_click = (ord(string[index]) - ord('a')) % 3
			if num_click == 0:
				num_click = 3
		answer += num_click
	print("Case #" + str(case+1) + ": " + str(answer))