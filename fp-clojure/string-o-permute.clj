; https://www.hackerrank.com/challenges/string-o-permute

(dotimes [t (Integer/parseInt (read-line))]
  (println (clojure.string/join (mapcat reverse (partition 2 (read-line)))))
)
