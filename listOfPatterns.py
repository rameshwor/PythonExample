###  shows list of patterns for making plural values ###


import re

def build_match_and_apply_functions(pattern,search,replace):
	def matches_rules(word):
		return re.search(pattern,word)
	def apply_rules(word):
		return re.sub(search,replace,word)

	return (matches_rule,apply_rules)



patterns = ( ('[sxz]$','$','es') , ('[aeioudgkrpt]h$','$','es') , ('(qu|[^aeiou])y$','y$','ies') , ('$','$','s') )

rules = [ build_match_and_apply_functions(pattern,search,replace) for (pattern,search,replace) in patterns]


def plural_noun(noun):
	for matches_rule,apply_rules in rules:
		if matches_rule(noun):
			return apply_rule(noun)


