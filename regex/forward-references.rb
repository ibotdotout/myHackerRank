# https://www.hackerrank.com/challenges/forward-references

# Forward reference is supported by JGsoft, .NET, Java, Perl, PCRE, PHP, Delphi and Ruby regex flavors.

Regex_Pattern = '^(\2tic|(tac))+$'

print !!(gets =~ /#{Regex_Pattern}/)
