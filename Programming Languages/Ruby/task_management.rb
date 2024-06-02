class Task
  attr_accessor :description, :completed

  def initialize(description)
    @description = description
    @completed = false
  end

  def complete!
    @completed = true
  end

  def to_s
    "#{description} - #{completed ? "Completed" : "Not Completed"}"
  end
end

class TaskManagementSystem
  def initialize
    @tasks = []
  end

  def add_task(description)
    @tasks << Task.new(description)
  end

  def view_tasks
    if @tasks.empty?
      puts "No tasks to display."
    else
      @tasks.each_with_index do |task, index|
        puts "#{index + 1}. #{task}"
      end
    end
  end

  def delete_task(index)
    if index >= 1 && index <= @tasks.size
      @tasks.delete_at(index - 1)
      puts "Task #{index} deleted."
    else
      puts "Invalid task number."
    end
  end

  def complete_task(index)
    if index >= 1 && index <= @tasks.size
      @tasks[index - 1].complete!
      puts "Task #{index} marked as completed."
    else
      puts "Invalid task number."
    end
  end
end

system = TaskManagementSystem.new

loop do
  puts "\nTask Management System"
  puts "1. Add Task"
  puts "2. View Tasks"
  puts "3. Delete Task"
  puts "4. Complete Task"
  puts "5. Exit"
  print "Choose an option: "
  choice = gets.chomp.to_i

  case choice
  when 1
    print "Enter task description: "
    description = gets.chomp
    system.add_task(description)
  when 2
    system.view_tasks
  when 3
    print "Enter task number to delete: "
    index = gets.chomp.to_i
    system.delete_task(index)
  when 4
    print "Enter task number to complete: "
    index = gets.chomp.to_i
    system.complete_task(index)
  when 5
    puts "Exiting..."
    break
  else
    puts "Invalid option. Please try again."
  end
end
