

def time2sex(time)
    secs = [1, 60, 3600]
    time = time.split(":").reverse
    seconds = 0

    for i in 0..time.length-1
        seconds +=  secs[i] * time[i].to_i
    end

    return "=== " + seconds.to_s + " seconds ==="
end

if ARGV.length == 1
    puts time2sex(ARGV[0])
else
    puts "Please enter a command line arg"
    puts "HH:MM:SS"
    puts "EX:"
    puts "    time2sex 12:34:56"
end
