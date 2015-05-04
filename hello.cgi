#! /usr/bin/env ruby
require 'cgi'
cgi = CGI.new



#if there was non name passed in the query string
if cgi.params.empty?
honoriffics = ['Mr. President', 'Your Highness', 'Your Exaltedness']
greeting = honoriffics.sample
else
  greeting = cgi['name']
end

puts cgi.header
puts "
<!doctype html>
<html>
  <head>
  <title>Mind... BLOWN </title>
  </head>
  <body>
    #{greeting}
  </body>
</html>"
