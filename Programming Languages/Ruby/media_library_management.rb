require "json"

class MediaFile
  attr_accessor :name, :type

  def initialize(name, type)
    @name = name
    @type = type
  end

  def to_s
    "#{name}.#{type}"
  end
end

class MediaLibraryManagementSystem
  def initialize
    @media_files = []
  end

  def add_media(name, type)
    @media_files << MediaFile.new(name, type)
  end

  def view_media
    if @media_files.empty?
      puts "No media files available."
    else
      @media_files.each_with_index do |media, index|
        puts "#{index + 1}. #{media}"
      end
    end
  end

  def delete_media(index)
    if index >= 1 && index <= @media_files.size
      @media_files.delete_at(index - 1)
      puts "Media file #{index} deleted."
    else
      puts "Invalid media file number."
    end
  end

  def save_library
    data = @media_files.map { |media| { name: media.name, type: media.type } }
    File.write("media_library.json", JSON.pretty_generate(data))
  end

  def load_library
    if File.exist?("media_library.json")
      data = JSON.parse(File.read("media_library.json"))
      @media_files = data.map { |media| MediaFile.new(media["name"], media["type"]) }
    end
  end
end

system = MediaLibraryManagementSystem.new
system.load_library

loop do
  puts "\nMedia Library Management System"
  puts "1. Add Media File"
  puts "2. View Media Files"
  puts "3. Delete Media File"
  puts "4. Save and Exit"
  print "Choose an option: "
  choice = gets.chomp.to_i

  case choice
  when 1
    print "Enter media name: "
    name = gets.chomp
    print "Enter media type (jpg, gif, png, etc.): "
    type = gets.chomp
    system.add_media(name, type)
  when 2
    system.view_media
  when 3
    print "Enter media file number to delete: "
    index = gets.chomp.to_i
    system.delete_media(index)
  when 4
    system.save_library
    puts "Library saved. Exiting..."
    break
  else
    puts "Invalid option. Please try again."
  end
end
