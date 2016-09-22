; https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---gcd

(let [f (fn [x y] 
            (if (zero? y)
              x 
              (recur y (mod x y))))
      [m n] (map read-string (re-seq #"\d+" (read-line)))]
     (println (f m  n)))
