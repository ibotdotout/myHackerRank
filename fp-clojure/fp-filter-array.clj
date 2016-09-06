;; https://www.hackerrank.com/challenges/fp-filter-array

(fn[delim lst]
  (filter #(< % delim) lst)
 )
