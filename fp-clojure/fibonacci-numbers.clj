; https://www.hackerrank.com/challenges/functional-programming-warmups-in-recursion---fibonacci-numbers

(println (first (nth (iterate (fn[[a, b]] [b (+ a b)]) [0 1]) (- (read) 1))))
