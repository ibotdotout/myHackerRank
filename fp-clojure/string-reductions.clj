;https://www.hackerrank.com/challenges/string-reductions

; about contains? 
; http://stackoverflow.com/a/11963279

(println (clojure.string/join (reduce #(if (contains? (set %1) %2) %1 (conj %1 %2)) [] (read-line))))
