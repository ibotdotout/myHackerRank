; https://www.hackerrank.com/challenges/string-compression

; timeout

(->> (read-line)
     (reduce #(if (contains? (set (last %1)) %2) 
       (conj (vec (butlast %1)) (conj (last %1) %2))
       (conj %1 [%2])) [])
     (mapcat #(if (> (count %1) 1) [(first %1) (count %1)] [(first %1)]))
     (apply str)
     (println)
)

; fine

(->> (read-line)
     (re-seq #"(\w)\1*")
     (map first)
     (mapcat #(if (> (count %1) 1) [(first %1) (count %1)] [(first %1)]))
     (apply str)
     (println)
)
