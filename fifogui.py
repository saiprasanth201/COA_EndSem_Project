import tkinter as tk
from tkinter import messagebox, scrolledtext
from matplotlib import pyplot as plt

# Function to run FIFO algorithm
def run_fifo():
    try:
        frames = int(frame_entry.get())
        pages = list(map(int, pages_entry.get().split()))
    except:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    memory = []
    page_faults = 0
    steps = []

    # Clear previous memory display
    for widget in memory_frame.winfo_children():
        widget.destroy()

    # Run FIFO simulation
    for idx, page in enumerate(pages):
        fault = False
        if page not in memory:
            page_faults += 1
            fault = True
            if len(memory) == frames:
                memory.pop(0)
            memory.append(page)
        steps.append(memory.copy())

        # Display step in grid
        for f in range(frames):
            cell = tk.Label(memory_frame, text=memory[f] if f < len(memory) else "",
                            width=8, height=2,
                            bg="red" if fault and f == len(memory)-1 else "lightgreen",
                            relief="ridge", borderwidth=2)
            cell.grid(row=idx, column=f, padx=5, pady=2)

    # Display stats
    total_pages = len(pages)
    page_fault_rate = page_faults / total_pages
    stats_label.config(text=f"Total Page Faults: {page_faults} | Page Fault Rate: {page_fault_rate:.2f}")

    # Optional: plot working set
    visualize_working_set(steps, pages, frames)

# Function to plot working set
def visualize_working_set(steps, pages, frames):
    plt.figure(figsize=(10, frames))
    for i in range(frames):
        y = [i]*len(steps)
        x = list(range(len(steps)))
        vals = []
        for step in steps:
            if i < len(step):
                vals.append(step[i])
            else:
                vals.append(None)
        plt.plot(x, vals, marker='o', label=f'Frame {i+1}')
    plt.xticks(range(len(steps)), pages)
    plt.xlabel("Page Reference")
    plt.ylabel("Frame Content")
    plt.title("Working Set Visualization (FIFO)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Create main window
root = tk.Tk()
root.title("FIFO Page Replacement Simulator")
root.geometry("800x600")
root.config(bg="#f0f0f0")

# Input section
tk.Label(root, text="Number of Frames:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
frame_entry = tk.Entry(root, font=("Arial", 12))
frame_entry.pack(pady=5)

tk.Label(root, text="Page Reference String (space-separated):", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
pages_entry = tk.Entry(root, font=("Arial", 12), width=30)
pages_entry.pack(pady=5)

run_button = tk.Button(root, text="Run FIFO", font=("Arial", 12, "bold"), bg="#4caf50", fg="white",
                       command=run_fifo)
run_button.pack(pady=10)

# Memory display section
memory_frame = tk.Frame(root, bg="#f0f0f0")
memory_frame.pack(pady=10)

# Stats label
stats_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
stats_label.pack(pady=10)

root.mainloop()
