#!/usr/bin/env ruby
# This script contains regular expression matches a pattern

puts ARGV[0].scan(/hbt{2,5}n/).join
