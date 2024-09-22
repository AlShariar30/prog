def main():
    print("Program starting.")
    
  
    num_tasks = 7
    total_minutes = 0
    
    print("Estimate how many minutes you spent on programming...")
    
    
    for i in range(1, num_tasks + 1):
        minutes = int(input(f"A1_T{i}: "))
        total_minutes += minutes
    
   
    average_minutes = total_minutes / num_tasks
    rounded_average = round(average_minutes)
    
    
    print(f"\nIn total you spent {total_minutes} minutes on programming.")
    print(f"Average per task was {average_minutes:.2f} min and same rounded to the nearest integer {rounded_average} min.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()
