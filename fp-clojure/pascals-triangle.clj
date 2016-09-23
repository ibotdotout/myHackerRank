; https://www.hackerrank.com/challenges/pascals-triangle

(use '[clojure.string :only (join)])

(defn factorial [n]
  (reduce * (range 1 (inc n)))
)

(defn pascal-triangle [n, r]
  (/ (factorial n) (* (factorial r) (factorial (- n r))))
)

(let [N (read)
      lst (range N)]
     (dotimes [n N]
       (println
         (join " " (map (partial pascal-triangle n) (take (inc n) lst)))
       )
      )
)
