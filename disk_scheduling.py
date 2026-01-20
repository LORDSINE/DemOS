"""
Disk Scheduling Algorithm Simulator Module

Implements and visualizes various disk scheduling algorithms:
- FCFS (First Come First Serve)
- SSTF (Shortest Seek Time First)
- SCAN (Elevator Algorithm)
- C-SCAN (Circular SCAN)
- LOOK
- C-LOOK (Circular LOOK)

Each algorithm includes:
- Disk head movement visualization
- Seek sequence display
- Total seek time calculation
- Step-by-step execution
"""

import tkinter as tk
from tkinter import ttk, messagebox


class DiskSchedulingModule:
    """Main module for Disk Scheduling algorithms."""
    
    def __init__(self, parent, back_callback):
        """
        Initialize the Disk Scheduling module.
        
        Args:
            parent: Parent Tkinter widget
            back_callback: Function to call when returning to home
        """
        self.parent = parent
        self.back_callback = back_callback
        self.requests = []
        self.seek_sequence = []
        self.total_seek_time = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        """Create the user interface for disk scheduling."""
        # Header
        header_frame = tk.Frame(self.parent, bg="#34495e", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        back_btn = tk.Button(
            header_frame,
            text="← Back to Home",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="white",
            command=self.back_callback,
            cursor="hand2",
            relief=tk.FLAT
        )
        back_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        title = tk.Label(
            header_frame,
            text="Disk Scheduling Algorithms",
            font=("Arial", 18, "bold"),
            bg="#34495e",
            fg="white"
        )
        title.pack(side=tk.LEFT, padx=20)
        
        # Main content area
        content_frame = tk.Frame(self.parent, bg="#ecf0f1")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Input and Controls
        left_panel = tk.Frame(content_frame, bg="white", relief=tk.RIDGE, borderwidth=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 5), pady=0)
        left_panel.config(width=350)
        left_panel.pack_propagate(False)
        
        # Algorithm selection
        algo_frame = tk.LabelFrame(left_panel, text="Select Algorithm",
                                   font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        algo_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.algorithm_var = tk.StringVar(value="FCFS")
        algorithms = [("FCFS", "FCFS"), ("SSTF", "SSTF"),
                     ("SCAN", "SCAN"), ("C-SCAN", "CSCAN"),
                     ("LOOK", "LOOK"), ("C-LOOK", "CLOOK")]
        
        for text, value in algorithms:
            rb = tk.Radiobutton(algo_frame, text=text, variable=self.algorithm_var,
                               value=value, bg="white", font=("Arial", 10))
            rb.pack(anchor=tk.W)
        
        # Disk parameters
        params_frame = tk.LabelFrame(left_panel, text="Disk Parameters",
                                     font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        params_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Initial head position
        head_frame = tk.Frame(params_frame, bg="white")
        head_frame.pack(fill=tk.X, pady=2)
        tk.Label(head_frame, text="Initial Head Pos:", width=15, anchor='w',
                bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        self.initial_head_var = tk.StringVar(value="50")
        tk.Entry(head_frame, textvariable=self.initial_head_var, width=10,
                font=("Arial", 9)).pack(side=tk.LEFT)
        
        # Disk size
        size_frame = tk.Frame(params_frame, bg="white")
        size_frame.pack(fill=tk.X, pady=2)
        tk.Label(size_frame, text="Disk Size:", width=15, anchor='w',
                bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        self.disk_size_var = tk.StringVar(value="200")
        tk.Entry(size_frame, textvariable=self.disk_size_var, width=10,
                font=("Arial", 9)).pack(side=tk.LEFT)
        
        # Direction (for SCAN/LOOK)
        dir_frame = tk.Frame(params_frame, bg="white")
        dir_frame.pack(fill=tk.X, pady=5)
        tk.Label(dir_frame, text="Direction (SCAN/LOOK):", bg="white",
                font=("Arial", 9)).pack(anchor=tk.W)
        
        self.direction_var = tk.StringVar(value="right")
        dir_buttons = tk.Frame(params_frame, bg="white")
        dir_buttons.pack(fill=tk.X)
        tk.Radiobutton(dir_buttons, text="Left", variable=self.direction_var,
                      value="left", bg="white", font=("Arial", 9)).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(dir_buttons, text="Right", variable=self.direction_var,
                      value="right", bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        
        # Request input
        request_frame = tk.LabelFrame(left_panel, text="Add Disk Request",
                                      font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        request_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Request position
        req_frame = tk.Frame(request_frame, bg="white")
        req_frame.pack(fill=tk.X, pady=2)
        tk.Label(req_frame, text="Track Number:", width=15, anchor='w',
                bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        self.request_var = tk.StringVar(value="82")
        tk.Entry(req_frame, textvariable=self.request_var, width=10,
                font=("Arial", 9)).pack(side=tk.LEFT)
        
        # Add request button
        tk.Button(request_frame, text="Add Request", command=self.add_request,
                 bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                 cursor="hand2").pack(pady=(10, 5))
        
        # Quick setup
        tk.Button(request_frame, text="Quick Setup (Example)", command=self.quick_setup,
                 bg="#16a085", fg="white", font=("Arial", 9),
                 cursor="hand2").pack(pady=(0, 0))
        
        # Requests list
        list_frame = tk.LabelFrame(left_panel, text="Request Queue",
                                   font=("Arial", 11, "bold"), bg="white", padx=5, pady=5)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Listbox for requests
        self.request_listbox = tk.Listbox(list_frame, font=("Arial", 10), height=10)
        self.request_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Control buttons
        btn_frame = tk.Frame(left_panel, bg="white")
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(btn_frame, text="Clear All", command=self.clear_requests,
                 bg="#e74c3c", fg="white", font=("Arial", 9, "bold")).pack(fill=tk.X, pady=2)
        tk.Button(btn_frame, text="Simulate", command=self.simulate,
                 bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(fill=tk.X, pady=2)
        tk.Button(btn_frame, text="Reset", command=self.reset_simulation,
                 bg="#95a5a6", fg="white", font=("Arial", 9, "bold")).pack(fill=tk.X, pady=2)
        
        # Right panel - Visualization
        right_panel = tk.Frame(content_frame, bg="white", relief=tk.RIDGE, borderwidth=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0), pady=0)
        
        # Canvas for disk head movement
        canvas_frame = tk.LabelFrame(right_panel, text="Disk Head Movement",
                                     font=("Arial", 12, "bold"), bg="white", padx=5, pady=5)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Results frame
        results_frame = tk.LabelFrame(right_panel, text="Results & Statistics",
                                      font=("Arial", 12, "bold"), bg="white", padx=5, pady=5)
        results_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.results_text = tk.Text(results_frame, height=10, font=("Courier", 9),
                                   bg="#f8f9fa", relief=tk.FLAT)
        self.results_text.pack(fill=tk.X, padx=5, pady=5)
    
    def add_request(self):
        """Add a disk request to the queue."""
        try:
            track = int(self.request_var.get())
            disk_size = int(self.disk_size_var.get())
            
            if track < 0 or track >= disk_size:
                messagebox.showerror("Error",
                                    f"Track number must be between 0 and {disk_size-1}")
                return
            
            self.requests.append(track)
            self.request_listbox.insert(tk.END, f"Track {track}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def quick_setup(self):
        """Quickly set up example disk requests."""
        self.clear_requests()
        # Classic example: requests at tracks 98, 183, 37, 122, 14, 124, 65, 67
        example_requests = [98, 183, 37, 122, 14, 124, 65, 67]
        
        for track in example_requests:
            self.requests.append(track)
            self.request_listbox.insert(tk.END, f"Track {track}")
    
    def clear_requests(self):
        """Clear all disk requests."""
        self.requests.clear()
        self.request_listbox.delete(0, tk.END)
        self.reset_simulation()
    
    def reset_simulation(self):
        """Reset the simulation state."""
        self.seek_sequence.clear()
        self.total_seek_time = 0
        self.canvas.delete("all")
        self.results_text.delete(1.0, tk.END)
    
    def simulate(self):
        """Run the selected disk scheduling algorithm."""
        if not self.requests:
            messagebox.showwarning("Warning", "Please add at least one disk request")
            return
        
        try:
            initial_head = int(self.initial_head_var.get())
            disk_size = int(self.disk_size_var.get())
            
            if initial_head < 0 or initial_head >= disk_size:
                messagebox.showerror("Error",
                                    f"Initial head position must be between 0 and {disk_size-1}")
                return
            
            self.reset_simulation()
            algorithm = self.algorithm_var.get()
            
            if algorithm == "FCFS":
                self.simulate_fcfs(initial_head)
            elif algorithm == "SSTF":
                self.simulate_sstf(initial_head)
            elif algorithm == "SCAN":
                self.simulate_scan(initial_head, disk_size)
            elif algorithm == "CSCAN":
                self.simulate_cscan(initial_head, disk_size)
            elif algorithm == "LOOK":
                self.simulate_look(initial_head)
            elif algorithm == "CLOOK":
                self.simulate_clook(initial_head)
            
            self.draw_visualization()
            self.display_results()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def simulate_fcfs(self, initial_head):
        """
        First Come First Serve (FCFS) Disk Scheduling.
        
        Logic:
        Process disk requests in the order they arrive.
        Simple but may result in high seek time.
        
        Args:
            initial_head: Starting position of disk head
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        
        for request in self.requests:
            # Move to requested track
            seek_distance = abs(request - current_position)
            self.total_seek_time += seek_distance
            current_position = request
            self.seek_sequence.append(current_position)
    
    def simulate_sstf(self, initial_head):
        """
        Shortest Seek Time First (SSTF) Disk Scheduling.
        
        Logic:
        Always service the request that is closest to the current head position.
        Greedy approach that minimizes seek time locally.
        
        Args:
            initial_head: Starting position of disk head
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        remaining_requests = self.requests.copy()
        
        while remaining_requests:
            # Find closest request
            closest = min(remaining_requests, key=lambda x: abs(x - current_position))
            
            # Move to closest request
            seek_distance = abs(closest - current_position)
            self.total_seek_time += seek_distance
            current_position = closest
            self.seek_sequence.append(current_position)
            
            remaining_requests.remove(closest)
    
    def simulate_scan(self, initial_head, disk_size):
        """
        SCAN (Elevator) Disk Scheduling Algorithm.
        
        Logic:
        Move in one direction servicing all requests until reaching the end,
        then reverse direction and service requests in the other direction.
        
        Args:
            initial_head: Starting position of disk head
            disk_size: Total number of tracks on disk
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        direction = self.direction_var.get()
        
        # Separate requests into left and right of current position
        left_requests = sorted([r for r in self.requests if r < current_position], reverse=True)
        right_requests = sorted([r for r in self.requests if r >= current_position])
        
        if direction == "right":
            # Service right side first
            for request in right_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
            
            # Go to end if there were requests on right
            if right_requests:
                seek_distance = abs((disk_size - 1) - current_position)
                self.total_seek_time += seek_distance
                current_position = disk_size - 1
                self.seek_sequence.append(current_position)
            
            # Service left side
            for request in left_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
        else:
            # Service left side first
            for request in left_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
            
            # Go to beginning if there were requests on left
            if left_requests:
                seek_distance = abs(0 - current_position)
                self.total_seek_time += seek_distance
                current_position = 0
                self.seek_sequence.append(current_position)
            
            # Service right side
            for request in right_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
    
    def simulate_cscan(self, initial_head, disk_size):
        """
        C-SCAN (Circular SCAN) Disk Scheduling Algorithm.
        
        Logic:
        Move in one direction servicing all requests until reaching the end,
        then jump back to the beginning and continue in the same direction.
        Provides more uniform wait time than SCAN.
        
        Args:
            initial_head: Starting position of disk head
            disk_size: Total number of tracks on disk
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        
        # Separate requests into left and right
        left_requests = sorted([r for r in self.requests if r < current_position])
        right_requests = sorted([r for r in self.requests if r >= current_position])
        
        # Always move right first in C-SCAN
        # Service right side
        for request in right_requests:
            seek_distance = abs(request - current_position)
            self.total_seek_time += seek_distance
            current_position = request
            self.seek_sequence.append(current_position)
        
        # Go to end if we serviced any right requests
        if right_requests:
            seek_distance = abs((disk_size - 1) - current_position)
            self.total_seek_time += seek_distance
            current_position = disk_size - 1
            self.seek_sequence.append(current_position)
            
            # Jump to beginning (count this as seek time)
            seek_distance = disk_size - 1
            self.total_seek_time += seek_distance
            current_position = 0
            self.seek_sequence.append(current_position)
        
        # Service left side (which is now in front)
        for request in left_requests:
            seek_distance = abs(request - current_position)
            self.total_seek_time += seek_distance
            current_position = request
            self.seek_sequence.append(current_position)
    
    def simulate_look(self, initial_head):
        """
        LOOK Disk Scheduling Algorithm.
        
        Logic:
        Similar to SCAN but only goes as far as the last request in each direction,
        not all the way to the end of the disk.
        
        Args:
            initial_head: Starting position of disk head
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        direction = self.direction_var.get()
        
        # Separate requests into left and right
        left_requests = sorted([r for r in self.requests if r < current_position], reverse=True)
        right_requests = sorted([r for r in self.requests if r >= current_position])
        
        if direction == "right":
            # Service right side
            for request in right_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
            
            # Service left side
            for request in left_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
        else:
            # Service left side
            for request in left_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
            
            # Service right side
            for request in right_requests:
                seek_distance = abs(request - current_position)
                self.total_seek_time += seek_distance
                current_position = request
                self.seek_sequence.append(current_position)
    
    def simulate_clook(self, initial_head):
        """
        C-LOOK (Circular LOOK) Disk Scheduling Algorithm.
        
        Logic:
        Similar to C-SCAN but only goes as far as the last request,
        then jumps back to the first request in the direction of movement.
        
        Args:
            initial_head: Starting position of disk head
        """
        self.seek_sequence = [initial_head]
        current_position = initial_head
        
        # Separate requests into left and right
        left_requests = sorted([r for r in self.requests if r < current_position])
        right_requests = sorted([r for r in self.requests if r >= current_position])
        
        # Service right side
        for request in right_requests:
            seek_distance = abs(request - current_position)
            self.total_seek_time += seek_distance
            current_position = request
            self.seek_sequence.append(current_position)
        
        # Jump to first request on left (if any)
        if left_requests and right_requests:
            # Jump from last right request to first left request
            first_left = left_requests[0]
            seek_distance = abs(first_left - current_position)
            self.total_seek_time += seek_distance
            current_position = first_left
            self.seek_sequence.append(current_position)
            left_requests = left_requests[1:]  # Remove first as we just serviced it
        
        # Service remaining left side
        for request in left_requests:
            seek_distance = abs(request - current_position)
            self.total_seek_time += seek_distance
            current_position = request
            self.seek_sequence.append(current_position)
    
    def draw_visualization(self):
        """Draw the disk head movement visualization."""
        self.canvas.delete("all")
        
        if not self.seek_sequence:
            return
        
        # Get canvas dimensions
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        if canvas_width <= 1:
            canvas_width = 800
        if canvas_height <= 1:
            canvas_height = 400
        
        # Drawing parameters
        margin_left = 60
        margin_right = 40
        margin_top = 60
        margin_bottom = 60
        
        graph_width = canvas_width - margin_left - margin_right
        graph_height = canvas_height - margin_top - margin_bottom
        
        # Title
        self.canvas.create_text(canvas_width // 2, 25,
                               text=f"Disk Head Movement - {self.algorithm_var.get()} Algorithm",
                               font=("Arial", 14, "bold"))
        
        # Calculate scales
        disk_size = int(self.disk_size_var.get())
        max_sequence = len(self.seek_sequence) - 1
        
        if max_sequence == 0:
            return
        
        x_scale = graph_width / max_sequence
        y_scale = graph_height / disk_size
        
        # Draw axes
        # Y-axis (track numbers)
        self.canvas.create_line(margin_left, margin_top,
                               margin_left, margin_top + graph_height,
                               width=2, arrow=tk.LAST)
        
        # X-axis (sequence)
        self.canvas.create_line(margin_left, margin_top + graph_height,
                               margin_left + graph_width, margin_top + graph_height,
                               width=2, arrow=tk.LAST)
        
        # Y-axis label
        self.canvas.create_text(margin_left - 30, margin_top - 20,
                               text="Track", font=("Arial", 10, "bold"))
        
        # X-axis label
        self.canvas.create_text(canvas_width // 2, canvas_height - 20,
                               text="Request Sequence", font=("Arial", 10, "bold"))
        
        # Draw grid lines and Y-axis labels
        num_grid_lines = 10
        grid_interval = disk_size / num_grid_lines
        
        for i in range(num_grid_lines + 1):
            track_num = int(i * grid_interval)
            y = margin_top + graph_height - (track_num * y_scale)
            
            # Grid line
            self.canvas.create_line(margin_left, y,
                                   margin_left + graph_width, y,
                                   fill="#e0e0e0", dash=(2, 2))
            
            # Label
            self.canvas.create_text(margin_left - 15, y,
                                   text=str(track_num),
                                   font=("Arial", 8))
        
        # Draw the seek sequence path
        points = []
        for i, track in enumerate(self.seek_sequence):
            x = margin_left + (i * x_scale)
            y = margin_top + graph_height - (track * y_scale)
            points.append((x, y))
        
        # Draw lines connecting points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            # Draw line
            self.canvas.create_line(x1, y1, x2, y2,
                                   fill="#3498db", width=2, arrow=tk.LAST)
        
        # Draw points and labels
        for i, (x, y) in enumerate(points):
            # Draw point
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                                   fill="#e74c3c" if i == 0 else "#2ecc71",
                                   outline="black", width=2)
            
            # Label with track number
            label = f"{self.seek_sequence[i]}"
            if i == 0:
                label = f"Start\n{self.seek_sequence[i]}"
            
            # Position label above or below point to avoid overlap
            label_y = y - 20 if i % 2 == 0 else y + 20
            self.canvas.create_text(x, label_y, text=label,
                                   font=("Arial", 8, "bold"))
    
    def display_results(self):
        """Display the results and statistics."""
        self.results_text.delete(1.0, tk.END)
        
        # Header
        self.results_text.insert(tk.END, f"{'='*60}\n")
        self.results_text.insert(tk.END, f" {self.algorithm_var.get()} Disk Scheduling Results\n")
        self.results_text.insert(tk.END, f"{'='*60}\n\n")
        
        # Display seek sequence
        self.results_text.insert(tk.END, "Seek Sequence:\n")
        sequence_str = " → ".join(str(track) for track in self.seek_sequence)
        
        # Word wrap for long sequences
        words = sequence_str.split(" → ")
        line = ""
        for i, word in enumerate(words):
            if len(line) + len(word) + 4 > 60:
                self.results_text.insert(tk.END, f"  {line}→\n")
                line = word
            else:
                if line:
                    line += " → " + word
                else:
                    line = word
        if line:
            self.results_text.insert(tk.END, f"  {line}\n")
        
        self.results_text.insert(tk.END, f"\n{'-'*60}\n")
        
        # Display statistics
        self.results_text.insert(tk.END, f"Initial Head Position:  {self.seek_sequence[0]}\n")
        self.results_text.insert(tk.END, f"Total Requests:         {len(self.requests)}\n")
        self.results_text.insert(tk.END, f"Total Seek Time:        {self.total_seek_time} tracks\n")
        
        if len(self.requests) > 0:
            avg_seek = self.total_seek_time / len(self.requests)
            self.results_text.insert(tk.END, f"Average Seek Time:      {avg_seek:.2f} tracks/request\n")
        
        self.results_text.insert(tk.END, f"{'='*60}\n")
        
        # Show individual movements
        self.results_text.insert(tk.END, f"\nDetailed Movements:\n")
        for i in range(len(self.seek_sequence) - 1):
            from_track = self.seek_sequence[i]
            to_track = self.seek_sequence[i + 1]
            distance = abs(to_track - from_track)
            
            if i == 0:
                self.results_text.insert(tk.END,
                                        f"  Start: {from_track} → {to_track} "
                                        f"(seek: {distance})\n")
            else:
                self.results_text.insert(tk.END,
                                        f"  {from_track} → {to_track} "
                                        f"(seek: {distance})\n")
