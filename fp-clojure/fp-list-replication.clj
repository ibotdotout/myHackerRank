;; https://www.hackerrank.com/challenges/fp-list-replication

 (fn[num lst]
    (doseq [i lst]
        (dotimes [n num]
            (println i))))
