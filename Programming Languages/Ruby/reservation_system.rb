class Reservation
  attr_accessor :name, :time, :guests

  def initialize(name, time, guests)
    @name = name
    @time = time
    @guests = guests
  end

  def to_s
    "Reservation for #{@name} at #{@time} for #{@guests} guests."
  end
end

class ReservationSystem
  def initialize
    @reservations = []
  end

  def add_reservation(name, time, guests)
    @reservations << Reservation.new(name, time, guests)
  end

  def view_reservations
    if @reservations.empty?
      puts "No reservations found."
    else
      @reservations.each { |reservation| puts reservation }
    end
  end

  def cancel_reservation(name)
    @reservations.reject! { |reservation| reservation.name == name }
  end
end

system = ReservationSystem.new

loop do
  puts "\nRestaurant Reservation System"
  puts "1. Add Reservation"
  puts "2. View Reservations"
  puts "3. Cancel Reservation"
  puts "4. Exit"
  print "Choose an option: "
  choice = gets.chomp.to_i

  case choice
  when 1
    print "Enter name: "
    name = gets.chomp
    print "Enter time (HH:MM): "
    time = gets.chomp
    print "Enter number of guests: "
    guests = gets.chomp.to_i
    system.add_reservation(name, time, guests)
  when 2
    system.view_reservations
  when 3
    print "Enter name to cancel: "
    name = gets.chomp
    system.cancel_reservation(name)
  when 4
    puts "Exiting..."
    break
  else
    puts "Invalid option. Please try again."
  end
end
