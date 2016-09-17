;; https://www.hackerrank.com/challenges/lambda-march-compute-the-perimeter-of-a-polygon

(def n (read))
(def perimeter 0)
(def points (repeatedly n #(vec [(read) (read)])))
(def points (conj points (last points)))

(defn distance [p1 p2]
   (let [dx (- (nth p1 0) (nth p2 0))
         dy (- (nth p1 1) (nth p2 1))]
        (Math/sqrt (+ (* dx dx) (* dy dy))))
)

(println
  (reduce +
    (map #(distance (nth %1 0) (nth %1 1))
      (map #(vec [(nth points %1) (nth points (+ %1 1))]) (range n))
    )
  )
)

;; short version

(defn distance [[x1 y1] [x2 y2]]
  (Math/hypot (- x1 x2) (- y1 y2))
)

(let [n (read)
      points (cycle (repeatedly n #(vec [(read) (read)])))
      lst (take n points)
      rst (rest points)]
     (println (reduce + (map distance lst rst)))
)
