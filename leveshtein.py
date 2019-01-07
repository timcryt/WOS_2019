def levenshtein(s1, s2):
	l = [[0 for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]
	for i in range(len(s1) + 1):
		l[0][i] = i
	for i in range(len(s2) + 1):
		l[i][0] = i
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			l[j][i] = min(l[j-1][i] + 1, l[j][i-1] + 1, l[j-1][i-1] + 1)
			if s1[i-1] == s2[j-1]:
				l[j][i] = min(l[j][i], l[j-1][i-1])
	return l

def levenshtein_distance(s1, s2):
	return levenshtein(s1, s2)[len(s2)][len(s1)]

def levenshtein_distance_description(s1, s2):
	l = levenshtein(s1, s2);
	s = ""
	i = len(s1)
	j = len(s2)
	while i > 0 or j > 0:
		if j == 0:
			i -= 1
			s += "D"
		elif i == 0:
			j -= 1
			s += "I"
		elif s1[i-1] == s2[j-1] and l[j-1][i-1] == l[j][i]:
			i -= 1
			j -= 1
			s += "M"
		elif l[j-1][i-1] + 1 == l[j][i]:
			i -= 1
			j -= 1
			s += "R"
		elif l[j-1][i] + 1 == l[i][j]:
			j -= 1
			s += "I"
		else:
			i -= 1
			s += "D"
	return s[::-1]

print(levenshtein_distance_description("aaaa", ""))
