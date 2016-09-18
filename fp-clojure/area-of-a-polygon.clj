;; https://www.hackerrank.com/challenges/lambda-march-compute-the-area-of-a-polygon
;; http://www.mathopenref.com/coordpolygonarea.html

(defn calCross [[x1 y1] [x2 y2]]
  (- (* x1 y2) (* y1 x2))
)

(let [n (read)
      points (cycle (repeatedly n #(vec [(read) (read)])))
      lst (take n points)
      rst (rest points)]
     (println (float (/ (Math/abs (reduce + (map calCross lst rst))) 2)))
)
