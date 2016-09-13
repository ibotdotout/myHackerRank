;; https://www.hackerrank.com/challenges/fp-update-list

;; (fn[lst] (map #(max %1 (- %1)) lst))

(fn[lst] (map #(Math/abs %1) lst))
