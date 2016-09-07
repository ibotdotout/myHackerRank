;; https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list

;;(fn [lst] ((map second (filter #(odd? (first %1)) (map-indexed vector lst)))))
(fn [lst] (take-nth 2 (rest lst)))
