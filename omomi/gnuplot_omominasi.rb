require 'mizlab'
require 'bio'

seq = String.new

Bio::FlatFile.auto(ARGF) do |ff|
    ff.each_entry do |entry|
        seq += entry.seq.to_s
    end
end


mapping = { "a" => [1, 1], "t" => [-1, 1], "g" => [-1, -1], "c" => [1, -1] }
coordinate = Mizlab.calculate_coordinates(seq, mapping)

for element in 0..coordinate[0].size()-1 do
    puts "#{coordinate[0][element]} #{coordinate[1][element]}"
end