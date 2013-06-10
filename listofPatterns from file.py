## listofPatterns from file ## 



import re

def build_match_and_apply_functions(pattern,search,replace):
	def matches_rules(word):
		return re.search(pattern,word)
	def apply_rules(word):
		return re.sub(search,replace,word)

	return (matches_rule,apply_rules)



rules=[]

with open('rules-file.txt',encoding='utf-8') as pattern_file:
	for line in pattern_file:
		pattern,search,replace=line.split(None,3)
		rules.append(build_match_and_apply_functions(pattern,search,replace))




def plural_noun(noun):
	for matches_rule,apply_rules in rules:
		if matches_rule(noun):
			return apply_rule(noun)




