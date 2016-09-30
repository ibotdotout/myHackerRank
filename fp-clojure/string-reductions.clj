;https://www.hackerrank.com/challenges/string-reductions

; about contains? 
; http://stackoverflow.com/a/11963279

(->>
  (read-line)
  (reduce #(if (contains? (set %1) %2) %1 (conj %1 %2)) [] )
  (apply str)
  println
)

; shortest answer
; (println (apply str (distinct (read-line))))

