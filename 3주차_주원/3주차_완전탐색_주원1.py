# 주어진 입력 받기
values = list(map(int, input().split()))
num_trees = values[0]
cut_cost = values[1]
sell_price = values[2]
trees = []

for _ in range(num_trees):
	trees.append(int(input()))

total_answer = 0
# i는 자른 나무의 길이
for i in range(1, max(trees)+1):
	answer = 0
	# 각각의 나무를 이제 잘라보자
	for j in range(num_trees):
		# 자를 길이가 나무 길이보다 같거나 작아야 자를 수 있음
		if trees[j] >= i:
			# i 길이의 나무 조각의 수
			num_pieces = int(trees[j] / i)
			# 나무 길이가 자른 길이와 나누어 떨어지느냐에 자르는 횟수가 달라짐
			if trees[j] % i == 0:
				num_cut = int(trees[j] / i) - 1
			else:
				num_cut = int(trees[j] / i)
			# 비용적으로 손해라면 이 나무는 자를 필요가 없음
			if (num_pieces * sell_price * i - num_cut * cut_cost > 0):
				answer += num_pieces * sell_price * i - num_cut * cut_cost
	# 이 길이로 모든 나무를 잘랐을 때 최대로 벌 수 있어야 함
	if (answer > total_answer):
		total_answer = answer

print(total_answer)