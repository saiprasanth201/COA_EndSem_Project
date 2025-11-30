# FIFO Page Replacement Simulator in Python

# Input number of frames
frames = int(input("Enter number of frames: "))

# Input page reference string (space-separated integers)
pages = list(map(int, input("Enter page reference string: ").split()))

memory = []          # Current pages in memory
page_faults = 0      # Count of page faults

print("\nStep-by-step Working Set Visualization:\n")
print("Page Reference | Memory Frames")

for page in pages:
    # Check if page is already in memory
    if page not in memory:
        page_faults += 1
        # If memory is full, remove the oldest page (FIFO)
        if len(memory) == frames:
            removed = memory.pop(0)
            print(f"{page:14} | Removed: {removed}", end=' ')
        else:
            print(f"{page:14} |", end=' ')
        # Add new page to memory
        memory.append(page)
    else:
        print(f"{page:14} |", end=' ')

    # Print current memory content
    print(memory)

# Calculate page fault rate
total_pages = len(pages)
page_fault_rate = page_faults / total_pages

print(f"\nTotal Page Faults: {page_faults}")
print(f"Page Fault Rate: {page_fault_rate:.2f}")
