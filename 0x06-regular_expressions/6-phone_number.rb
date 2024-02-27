#!/usr/bin/env ruby
# This script contains a REGEX that matches 10 digit phone number(s)

puts ARGV[0].scan(/^[0-9]{10}$/).join
