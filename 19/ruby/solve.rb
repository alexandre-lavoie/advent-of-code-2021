require 'matrix'

axes = [1,-1].repeated_permutation(3).map{|v| Vector.elements(v)}.to_a
rotations = [0,1,2].permutation(3).map{|s| Matrix.columns(s.map{|r| v=[0,0,0]; v[r] = 1; v})}.to_a
$orientations = axes.product(rotations).map{|a, r| Matrix.diagonal(*a) * r}

def find_nearest(point, points)
    points.map{|tp| [tp, (point - tp).magnitude]}.min_by{|v| v[1]}
end

def distance_sum(points, reference)
    points.map{|tp| find_nearest(tp, reference)[1]}.sum
end

def find_orientation(points, reference)
    $orientations.map{|o| [o, distance_sum(points.map{|tp| o * tp}, reference)]}.min_by{|v| v[1]}[0]
end

def main
    point_lists = File.open("../input.t1.txt").read.split("--- scanner ").filter{|data| data.length > 0}.map{|data| data[6..].split("\n").map{|x| Vector.elements x.split(",").map{|y| y.to_i}}}

    reference = point_lists[0]
    point_lists = point_lists[1..]

    # Reorient points according to reference frame.
    point_lists = point_lists.zip(point_lists.map{|sp| find_orientation(sp, reference)}).map{|ps, o| ps.map{|v| o * v}}

    # I give up.
end

main