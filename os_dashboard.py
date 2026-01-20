"""
OS Dashboard - Real-time System Monitor

A comprehensive dashboard showing:
- System overview and statistics
- Running processes
- Memory usage graph
- Disk usage
- Real-time updates
"""

import tkinter as tk
from tkinter import ttk
import time


class OSDashboardModule:
    """Main dashboard for OS simulation."""
    
    def __init__(self, parent, back_callback):
        """
        Initialize the OS Dashboard.
        
        Args:
            parent: Parent Tkinter widget
            back_callback: Function to call when returning to home
        """
        self.parent = parent
        self.back_callback = back_callback
        self.update_interval = 2000  # Update every 2 seconds
        
        # Mock system data
        self.total_memory = 512
        self.used_memory = 180
        self.total_disk = 1024
        self.used_disk = 450
        self.cpu_usage = 45
        self.processes_running = 12
        
        self.setup_ui()
        self.start_auto_update()
    
    def setup_ui(self):
        """Create the dashboard UI."""
        # Header
        header_frame = tk.Frame(self.parent, bg="#8e44ad", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        back_btn = tk.Button(
            header_frame,
            text="← Back to Home",
            font=("Arial", 11),
            bg="#7d3c98",
            fg="white",
            command=self.back_callback,
            cursor="hand2",
            relief=tk.FLAT
        )
        back_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        title = tk.Label(
            header_frame,
            text="Operating System Dashboard - Real-time Monitor",
            font=("Arial", 18, "bold"),
            bg="#8e44ad",
            fg="white"
        )
        title.pack(side=tk.LEFT, padx=20)
        
        # Time label
        self.time_label = tk.Label(
            header_frame,
            text="",
            font=("Arial", 12),
            bg="#8e44ad",
            fg="white"
        )
        self.time_label.pack(side=tk.RIGHT, padx=20)
        
        # Main content
        content_frame = tk.Frame(self.parent, bg="#ecf0f1")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section - System metrics
        top_frame = tk.Frame(content_frame, bg="#ecf0f1")
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Metric cards
        metrics = [
            ("CPU Usage", "cpu", "#e74c3c"),
            ("Memory", "memory", "#3498db"),
            ("Disk", "disk", "#2ecc71"),
            ("Processes", "processes", "#f39c12")
        ]
        
        self.metric_widgets = {}
        for i, (title, key, color) in enumerate(metrics):
            card = self.create_metric_card(top_frame, title, "0%", color)
            card.grid(row=0, column=i, padx=5, sticky="ew")
            top_frame.grid_columnconfigure(i, weight=1)
            self.metric_widgets[key] = card
        
        # Middle section - Graphs
        middle_frame = tk.Frame(content_frame, bg="#ecf0f1")
        middle_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Left - Memory usage
        mem_frame = tk.LabelFrame(middle_frame, text="Memory Usage",
                                  font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        mem_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.mem_canvas = tk.Canvas(mem_frame, bg="white", height=200)
        self.mem_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Right - Disk usage
        disk_frame = tk.LabelFrame(middle_frame, text="Disk Usage",
                                   font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        disk_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.disk_canvas = tk.Canvas(disk_frame, bg="white", height=200)
        self.disk_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bottom section - Process list
        bottom_frame = tk.LabelFrame(content_frame, text="Running Processes",
                                     font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        bottom_frame.pack(fill=tk.BOTH, expand=True)
        
        # Process table
        columns = ("PID", "Name", "Memory", "CPU", "Status")
        self.process_tree = ttk.Treeview(bottom_frame, columns=columns,
                                        show="headings", height=8)
        
        for col in columns:
            self.process_tree.heading(col, text=col)
            self.process_tree.column(col, width=100)
        
        self.process_tree.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Status bar
        status_frame = tk.Frame(self.parent, bg="#34495e", height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="System Status: Running | Uptime: 00:00:00",
            font=("Arial", 9),
            bg="#34495e",
            fg="white",
            anchor=tk.W
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Initial update
        self.update_dashboard()
    
    def create_metric_card(self, parent, title, value, color):
        """Create a metric display card."""
        card_frame = tk.Frame(parent, bg=color, relief=tk.RAISED, borderwidth=2)
        card_frame.pack_propagate(False)
        card_frame.config(height=100)
        
        # Title
        title_label = tk.Label(card_frame, text=title, font=("Arial", 11, "bold"),
                              bg=color, fg="white")
        title_label.pack(pady=(15, 5))
        
        # Value
        value_label = tk.Label(card_frame, text=value, font=("Arial", 20, "bold"),
                              bg=color, fg="white")
        value_label.pack()
        
        # Store value label for updates
        card_frame.value_label = value_label
        
        return card_frame
    
    def update_dashboard(self):
        """Update all dashboard elements."""
        try:
            # Update time
            current_time = time.strftime("%H:%M:%S")
            self.time_label.config(text=current_time)
            
            # Simulate changing values (in real OS, these would be actual system values)
            import random
            self.cpu_usage = min(100, max(10, self.cpu_usage + random.randint(-10, 10)))
            self.used_memory = min(self.total_memory, 
                                  max(100, self.used_memory + random.randint(-20, 20)))
            self.used_disk = min(self.total_disk,
                                max(200, self.used_disk + random.randint(-10, 10)))
            
            # Update metric cards
            cpu_pct = self.cpu_usage
            mem_pct = (self.used_memory / self.total_memory) * 100
            disk_pct = (self.used_disk / self.total_disk) * 100
            
            self.metric_widgets['cpu'].value_label.config(text=f"{cpu_pct:.0f}%")
            self.metric_widgets['memory'].value_label.config(
                text=f"{self.used_memory}/{self.total_memory}MB")
            self.metric_widgets['disk'].value_label.config(
                text=f"{self.used_disk}/{self.total_disk}MB")
            self.metric_widgets['processes'].value_label.config(
                text=str(self.processes_running))
            
            # Update graphs
            self.draw_memory_graph()
            self.draw_disk_pie()
            
            # Update process list
            self.update_process_list()
            
            # Update status
            uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() % 86400))
            self.status_label.config(text=f"System Status: Running | Uptime: {uptime}")
            
        except (tk.TclError, AttributeError):
            # Widget destroyed or not available, stop updating
            pass
    
    def draw_memory_graph(self):
        """Draw memory usage bar chart."""
        self.mem_canvas.delete("all")
        
        width = self.mem_canvas.winfo_width()
        height = self.mem_canvas.winfo_height()
        
        if width <= 1:
            width = 400
        if height <= 1:
            height = 200
        
        # Draw bars
        margin = 40
        bar_width = (width - 2 * margin) / 4
        max_height = height - 60
        
        categories = [
            ("System", 80, "#34495e"),
            ("User", self.used_memory - 80, "#3498db"),
            ("Cache", 40, "#95a5a6"),
            ("Free", self.total_memory - self.used_memory, "#2ecc71")
        ]
        
        x = margin
        for label, value, color in categories:
            bar_height = (value / self.total_memory) * max_height
            y = height - 40 - bar_height
            
            # Bar
            self.mem_canvas.create_rectangle(x, y, x + bar_width - 5, height - 40,
                                           fill=color, outline="black", width=2)
            
            # Value
            self.mem_canvas.create_text(x + bar_width / 2, y - 10,
                                       text=f"{value}MB", font=("Arial", 9, "bold"))
            
            # Label
            self.mem_canvas.create_text(x + bar_width / 2, height - 25,
                                       text=label, font=("Arial", 9))
            
            x += bar_width
    
    def draw_disk_pie(self):
        """Draw disk usage pie chart."""
        self.disk_canvas.delete("all")
        
        width = self.disk_canvas.winfo_width()
        height = self.disk_canvas.winfo_height()
        
        if width <= 1:
            width = 400
        if height <= 1:
            height = 200
        
        # Center and radius
        cx = width / 2
        cy = height / 2
        radius = min(width, height) / 3
        
        # Calculate angles
        used_angle = (self.used_disk / self.total_disk) * 360
        
        # Draw pie slices
        # Used space (blue)
        self.draw_pie_slice(cx, cy, radius, 0, used_angle, "#3498db")
        
        # Free space (green)
        self.draw_pie_slice(cx, cy, radius, used_angle, 360, "#2ecc71")
        
        # Labels
        self.disk_canvas.create_text(cx, cy - radius - 30,
                                     text=f"Used: {self.used_disk}MB ({(self.used_disk/self.total_disk)*100:.1f}%)",
                                     font=("Arial", 10, "bold"))
        self.disk_canvas.create_text(cx, cy + radius + 30,
                                     text=f"Free: {self.total_disk - self.used_disk}MB",
                                     font=("Arial", 10))
    
    def draw_pie_slice(self, cx, cy, radius, start_angle, extent_angle, color):
        """Draw a pie chart slice."""
        x1 = cx - radius
        y1 = cy - radius
        x2 = cx + radius
        y2 = cy + radius
        
        self.disk_canvas.create_arc(x1, y1, x2, y2,
                                    start=start_angle, extent=extent_angle,
                                    fill=color, outline="black", width=2)
    
    def update_process_list(self):
        """Update the process list with mock data."""
        # Clear existing
        for item in self.process_tree.get_children():
            self.process_tree.delete(item)
        
        # Mock processes
        processes = [
            (1, "kernel", "64 MB", "0%", "Running"),
            (2, "init", "16 MB", "0%", "Running"),
            (3, "systemd", "32 MB", "1%", "Running"),
            (4, "chrome", "256 MB", "15%", "Running"),
            (5, "vscode", "180 MB", "8%", "Running"),
            (6, "python", "45 MB", "12%", "Running"),
            (7, "bash", "8 MB", "0%", "Sleeping"),
            (8, "ssh", "12 MB", "1%", "Running"),
        ]
        
        for process in processes:
            self.process_tree.insert("", tk.END, values=process)
    
    def start_auto_update(self):
        """Start automatic dashboard updates."""
        try:
            self.update_dashboard()
            self.parent.after(self.update_interval, self.start_auto_update)
        except tk.TclError:
            # Widget destroyed, stop updating
            pass
