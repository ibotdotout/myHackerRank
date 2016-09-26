; https://www.hackerrank.com/challenges/string-mingling

(let [p (read-line)
      q (read-line)]
      (println (clojure.string/join (interleave p q))))
