;; https://www.hackerrank.com/challenges/functions-or-not

(use '[clojure.string :only (join split)])

(def t (Integer/parseInt (read-line)))
(dotimes [_ t] 
  (def n (Integer/parseInt (read-line)))
  (def dict {})
  (def is-func? true)
  (dotimes [_ n]
    (def input (split (read-line) #"\s"))
    (def k (input 0))
    (def v (input 1))
    (if (not= (dict k) nil) (if (not= (dict k) v) (def is-func? false)))
    (def dict (into dict [input]))
  )
  (println (if is-func? "YES" "NO"))
)


; short anwser to pass the test but may not cover all real-world cases

;(dotimes [_ (read)]
;  (def n (read))
;  (def sets (set (repeatedly n #(first [(read) (read)]))))
;  (println (if (= (count sets) n) "YES" "NO"))
;)
