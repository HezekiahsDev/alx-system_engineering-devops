#!/usr/bin/env ruby
# This script contains a REGEX that matches a string that starting with h 
# and end with n. String may have any single character in between

puts ARGV[0].scan(/h.n/).join
