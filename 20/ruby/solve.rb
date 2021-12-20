require 'set'
require 'matrix'

data = File.open("../input.txt").readlines.map(&:chomp).map{|line| line.chars.map{|c| if c == "#" then 1 else 0 end}}
$algorithm = data[0]
$deltas = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]].map{|a| Vector.elements(a)}

def out_of_bound(vector, i_min, i_max, j_min, j_max)
    vector[0] < i_min || vector[0] > i_max || vector[1] < j_min || vector[1] > j_max
end

def enhance(bound_image)
    bound, image = bound_image
    i_min, i_max = image.map{|v| v[0]}.minmax
    j_min, j_max = image.map{|v| v[1]}.minmax
    new_image = Set[]

    (i_min-1..i_max+1).each{|i| (j_min-1..j_max+1).each{|j| 
        v = Vector[i,j]

        bin = $deltas.map{|d| ((image.include? (v + d)) || (bound && out_of_bound(v + d, i_min, i_max, j_min, j_max))) ? 1 : 0}.join
        index = bin.to_i(2) 

        if $algorithm[index] == 1 then
            new_image.add(v)
        end
    }}

    new_bound = if $algorithm[0] == 1 then !bound else false end

    [new_bound, new_image]
end

def n_enhance(n, image)
    (0..n-1).each{|_| image = enhance image}

    image
end

image = [false, data[2..].map.with_index.inject(Set[]){|c, entry|
    row, i = entry
    row.each_with_index{|v,j| if v == 1 then c.add(Vector[i,j]) end}
    c
}]

print "Task 1: ", (n_enhance(2, image))[1].count, "\n"
print "Task 2: ", (n_enhance(50, image))[1].count, "\n"
