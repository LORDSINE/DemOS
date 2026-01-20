"""
File System Module - Interactive OS Simulation

This module simulates a real file system where users can:
- Create files with actual content
- Delete files
- View files
- See how files are allocated in disk blocks
- Watch memory allocation in real-time
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
import random


class File:
    """Represents a file in the system."""
    
    def __init__(self, name, size, content="", file_type="txt"):
        """
        Initialize a file.
        
        Args:
            name: File name
            size: Size in KB
            content: File content
            file_type: File extension
        """
        self.name = name
        self.size = size
        self.content = content
        self.file_type = file_type
        self.blocks = []  # Disk blocks allocated
        self.creation_time = time.strftime("%H:%M:%S")
        self.memory_address = None


class DiskBlock:
    """Represents a disk block."""
    
    def __init__(self, block_id, size=1):
        """
        Initialize a disk block.
        
        Args:
            block_id: Block identifier
            size: Block size (default 1 KB)
        """
        self.block_id = block_id
        self.size = size
        self.is_allocated = False
        self.file_name = None


class FileSystemModule:
    """Main module for file system simulation."""
    
    def __init__(self, parent, back_callback):
        """
        Initialize the File System module.
        
        Args:
            parent: Parent Tkinter widget
            back_callback: Function to call when returning to home
        """
        self.parent = parent
        self.back_callback = back_callback
        self.files = []
        self.disk_blocks = []
        self.total_disk_size = 100  # 100 KB total
        self.block_size = 1  # 1 KB per block
        
        # Initialize disk
        self.initialize_disk()
        self.setup_ui()
    
    def initialize_disk(self):
        """Initialize disk blocks."""
        num_blocks = self.total_disk_size // self.block_size
        for i in range(num_blocks):
            self.disk_blocks.append(DiskBlock(i, self.block_size))
    
    def setup_ui(self):
        """Create the user interface."""
        # Header
        header_frame = tk.Frame(self.parent, bg="#2c3e50", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        back_btn = tk.Button(
            header_frame,
            text="← Back to Home",
            font=("Arial", 11),
            bg="#34495e",
            fg="white",
            command=self.back_callback,
            cursor="hand2",
            relief=tk.FLAT
        )
        back_btn.pack(side=tk.LEFT, padx=10, pady=10)
        
        title = tk.Label(
            header_frame,
            text="File System Simulator - Live Memory Allocation",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title.pack(side=tk.LEFT, padx=20)
        
        # Main content
        content_frame = tk.Frame(self.parent, bg="#ecf0f1")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - File operations
        left_panel = tk.Frame(content_frame, bg="white", relief=tk.RIDGE, borderwidth=2)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 5), pady=0)
        left_panel.config(width=350)
        left_panel.pack_propagate(False)
        
        # System status
        status_frame = tk.LabelFrame(left_panel, text="System Status",
                                     font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.status_text = tk.Text(status_frame, height=5, font=("Courier", 9),
                                   bg="#f8f9fa", relief=tk.FLAT, state=tk.DISABLED)
        self.status_text.pack(fill=tk.X)
        self.update_system_status()
        
        # Create file section
        create_frame = tk.LabelFrame(left_panel, text="Create New File",
                                     font=("Arial", 11, "bold"), bg="white", padx=10, pady=10)
        create_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # File name
        name_frame = tk.Frame(create_frame, bg="white")
        name_frame.pack(fill=tk.X, pady=2)
        tk.Label(name_frame, text="File Name:", width=12, anchor='w',
                bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        self.file_name_var = tk.StringVar(value="document.txt")
        tk.Entry(name_frame, textvariable=self.file_name_var, width=15,
                font=("Arial", 9)).pack(side=tk.LEFT)
        
        # File size
        size_frame = tk.Frame(create_frame, bg="white")
        size_frame.pack(fill=tk.X, pady=2)
        tk.Label(size_frame, text="Size (KB):", width=12, anchor='w',
                bg="white", font=("Arial", 9)).pack(side=tk.LEFT)
        self.file_size_var = tk.StringVar(value="5")
        tk.Entry(size_frame, textvariable=self.file_size_var, width=15,
                font=("Arial", 9)).pack(side=tk.LEFT)
        
        # File content
        tk.Label(create_frame, text="File Content:", bg="white",
                font=("Arial", 9)).pack(anchor=tk.W, pady=(5, 0))
        self.file_content_text = tk.Text(create_frame, height=4, font=("Arial", 9))
        self.file_content_text.pack(fill=tk.X, pady=5)
        self.file_content_text.insert(1.0, "This is a sample file...")
        
        # Create button
        tk.Button(create_frame, text="Create File", command=self.create_file,
                 bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                 cursor="hand2").pack(pady=(5, 0))
        
        # File list
        list_frame = tk.LabelFrame(left_panel, text="Files in System",
                                   font=("Arial", 11, "bold"), bg="white", padx=5, pady=5)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Treeview for files
        columns = ("Name", "Size", "Blocks", "Time")
        self.file_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
        self.file_tree.heading("Name", text="File Name")
        self.file_tree.heading("Size", text="Size (KB)")
        self.file_tree.heading("Blocks", text="Blocks")
        self.file_tree.heading("Time", text="Created")
        
        self.file_tree.column("Name", width=120)
        self.file_tree.column("Size", width=60)
        self.file_tree.column("Blocks", width=60)
        self.file_tree.column("Time", width=60)
        
        self.file_tree.pack(fill=tk.BOTH, expand=True)
        self.file_tree.bind('<Double-Button-1>', self.view_file)
        
        # Control buttons
        btn_frame = tk.Frame(left_panel, bg="white")
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(btn_frame, text="View File", command=self.view_file,
                 bg="#3498db", fg="white", font=("Arial", 9, "bold")).pack(fill=tk.X, pady=2)
        tk.Button(btn_frame, text="Delete File", command=self.delete_file,
                 bg="#e74c3c", fg="white", font=("Arial", 9, "bold")).pack(fill=tk.X, pady=2)
        tk.Button(btn_frame, text="Format Disk", command=self.format_disk,
                 bg="#95a5a6", fg="white", font=("Arial", 9, "bold")).pack(fill=tk.X, pady=2)
        
        # Right panel - Visualization
        right_panel = tk.Frame(content_frame, bg="white", relief=tk.RIDGE, borderwidth=2)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0), pady=0)
        
        # Disk visualization
        disk_frame = tk.LabelFrame(right_panel, text="Disk Block Allocation Map",
                                   font=("Arial", 12, "bold"), bg="white", padx=5, pady=5)
        disk_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.disk_canvas = tk.Canvas(disk_frame, bg="white", highlightthickness=0)
        self.disk_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Activity log
        log_frame = tk.LabelFrame(right_panel, text="System Activity Log",
                                  font=("Arial", 12, "bold"), bg="white", padx=5, pady=5)
        log_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, font=("Courier", 8),
                                                  bg="#2c3e50", fg="#2ecc71", relief=tk.FLAT)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)
        self.log("System initialized. Disk size: {} KB".format(self.total_disk_size))
        self.log("Ready to create files...")
        
        # Draw initial disk
        self.draw_disk_visualization()
    
    def create_file(self):
        """Create a new file and allocate disk blocks."""
        try:
            file_name = self.file_name_var.get().strip()
            file_size = int(self.file_size_var.get())
            content = self.file_content_text.get(1.0, tk.END).strip()
            
            if not file_name:
                messagebox.showerror("Error", "File name cannot be empty")
                return
            
            if file_size <= 0:
                messagebox.showerror("Error", "File size must be positive")
                return
            
            # Check if file already exists
            if any(f.name == file_name for f in self.files):
                messagebox.showerror("Error", f"File '{file_name}' already exists")
                return
            
            # Check available space
            free_blocks = sum(1 for b in self.disk_blocks if not b.is_allocated)
            if file_size > free_blocks:
                messagebox.showerror("Disk Full", 
                                    f"Not enough space! Need {file_size} KB, available {free_blocks} KB")
                self.log(f"ERROR: Failed to create '{file_name}' - insufficient space")
                return
            
            # Allocate blocks
            allocated_blocks = []
            blocks_needed = file_size
            
            self.log(f"Creating file '{file_name}' ({file_size} KB)...")
            
            for block in self.disk_blocks:
                if not block.is_allocated and blocks_needed > 0:
                    block.is_allocated = True
                    block.file_name = file_name
                    allocated_blocks.append(block.block_id)
                    blocks_needed -= 1
                    self.log(f"  Allocated block {block.block_id} to '{file_name}'")
            
            # Create file object
            new_file = File(file_name, file_size, content)
            new_file.blocks = allocated_blocks
            self.files.append(new_file)
            
            # Update displays
            self.update_file_list()
            self.draw_disk_visualization()
            self.update_system_status()
            
            self.log(f"SUCCESS: File '{file_name}' created successfully!")
            self.log(f"  Blocks allocated: {allocated_blocks}")
            
            # Auto-increment file name
            if "." in file_name:
                base, ext = file_name.rsplit(".", 1)
                if base[-1].isdigit():
                    num = int(''.join(filter(str.isdigit, base)))
                    new_base = ''.join(filter(str.isalpha, base))
                    self.file_name_var.set(f"{new_base}{num+1}.{ext}")
                else:
                    self.file_name_var.set(f"{base}2.{ext}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def delete_file(self):
        """Delete selected file and free disk blocks."""
        selection = self.file_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a file to delete")
            return
        
        item = self.file_tree.item(selection[0])
        file_name = item['values'][0]
        
        # Find file
        file_obj = next((f for f in self.files if f.name == file_name), None)
        if not file_obj:
            return
        
        # Confirm deletion
        if not messagebox.askyesno("Confirm Delete", 
                                   f"Delete file '{file_name}'?\nThis will free {file_obj.size} KB"):
            return
        
        self.log(f"Deleting file '{file_name}'...")
        
        # Free blocks
        for block_id in file_obj.blocks:
            block = self.disk_blocks[block_id]
            block.is_allocated = False
            block.file_name = None
            self.log(f"  Freed block {block_id}")
        
        # Remove file
        self.files.remove(file_obj)
        
        # Update displays
        self.update_file_list()
        self.draw_disk_visualization()
        self.update_system_status()
        
        self.log(f"SUCCESS: File '{file_name}' deleted")
    
    def view_file(self, event=None):
        """View file contents."""
        selection = self.file_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a file to view")
            return
        
        item = self.file_tree.item(selection[0])
        file_name = item['values'][0]
        
        # Find file
        file_obj = next((f for f in self.files if f.name == file_name), None)
        if not file_obj:
            return
        
        # Create view window
        view_window = tk.Toplevel(self.parent)
        view_window.title(f"Viewing: {file_name}")
        view_window.geometry("500x400")
        view_window.configure(bg="white")
        
        # File info
        info_frame = tk.Frame(view_window, bg="#ecf0f1", padx=10, pady=10)
        info_frame.pack(fill=tk.X)
        
        tk.Label(info_frame, text=f"File: {file_obj.name}", 
                font=("Arial", 12, "bold"), bg="#ecf0f1").pack(anchor=tk.W)
        tk.Label(info_frame, text=f"Size: {file_obj.size} KB", 
                font=("Arial", 10), bg="#ecf0f1").pack(anchor=tk.W)
        tk.Label(info_frame, text=f"Created: {file_obj.creation_time}", 
                font=("Arial", 10), bg="#ecf0f1").pack(anchor=tk.W)
        tk.Label(info_frame, text=f"Disk Blocks: {file_obj.blocks}", 
                font=("Arial", 10), bg="#ecf0f1").pack(anchor=tk.W)
        
        # Content
        content_frame = tk.LabelFrame(view_window, text="File Content",
                                      font=("Arial", 11, "bold"), bg="white", padx=5, pady=5)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        content_text = scrolledtext.ScrolledText(content_frame, font=("Courier", 10), wrap=tk.WORD)
        content_text.pack(fill=tk.BOTH, expand=True)
        content_text.insert(1.0, file_obj.content)
        content_text.config(state=tk.DISABLED)
        
        # Close button
        tk.Button(view_window, text="Close", command=view_window.destroy,
                 bg="#95a5a6", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
    
    def format_disk(self):
        """Format disk - delete all files."""
        if not self.files:
            messagebox.showinfo("Info", "Disk is already empty")
            return
        
        if not messagebox.askyesno("Confirm Format", 
                                   "This will delete ALL files!\nAre you sure?"):
            return
        
        self.log("FORMATTING DISK...")
        
        # Free all blocks
        for block in self.disk_blocks:
            block.is_allocated = False
            block.file_name = None
        
        # Clear files
        self.files.clear()
        
        # Update displays
        self.update_file_list()
        self.draw_disk_visualization()
        self.update_system_status()
        
        self.log("SUCCESS: Disk formatted successfully")
        self.log("All files deleted. Disk is now empty.")
    
    def update_file_list(self):
        """Update the file list treeview."""
        for item in self.file_tree.get_children():
            self.file_tree.delete(item)
        
        for file_obj in self.files:
            blocks_str = f"{len(file_obj.blocks)}"
            self.file_tree.insert("", tk.END, 
                                 values=(file_obj.name, file_obj.size, 
                                        blocks_str, file_obj.creation_time))
    
    def draw_disk_visualization(self):
        """Draw disk block allocation visualization."""
        self.disk_canvas.delete("all")
        
        canvas_width = self.disk_canvas.winfo_width()
        canvas_height = self.disk_canvas.winfo_height()
        
        if canvas_width <= 1:
            canvas_width = 800
        if canvas_height <= 1:
            canvas_height = 400
        
        # Title
        self.disk_canvas.create_text(canvas_width // 2, 20,
                                     text="Disk Allocation Map (Each cell = 1 KB block)",
                                     font=("Arial", 12, "bold"))
        
        # Calculate grid
        blocks_per_row = 20
        total_blocks = len(self.disk_blocks)
        rows = (total_blocks + blocks_per_row - 1) // blocks_per_row
        
        cell_size = 25
        margin_x = 50
        margin_y = 50
        
        # Color palette for files
        file_colors = {}
        colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", 
                 "#1abc9c", "#e67e22", "#16a085", "#d35400", "#c0392b"]
        
        for i, file_obj in enumerate(self.files):
            file_colors[file_obj.name] = colors[i % len(colors)]
        
        # Draw blocks
        for i, block in enumerate(self.disk_blocks):
            row = i // blocks_per_row
            col = i % blocks_per_row
            
            x = margin_x + col * cell_size
            y = margin_y + row * cell_size
            
            # Color based on allocation
            if block.is_allocated:
                color = file_colors.get(block.file_name, "#95a5a6")
            else:
                color = "#ecf0f1"  # Free block
            
            # Draw block
            rect = self.disk_canvas.create_rectangle(x, y, x + cell_size - 2, y + cell_size - 2,
                                                     fill=color, outline="black", width=1)
            
            # Block number
            self.disk_canvas.create_text(x + cell_size // 2, y + cell_size // 2,
                                        text=str(i), font=("Arial", 7))
            
            # Tooltip on hover
            if block.is_allocated:
                self.disk_canvas.tag_bind(rect, '<Enter>', 
                    lambda e, b=block: self.show_block_info(e, b))
        
        # Legend
        legend_y = margin_y + rows * cell_size + 20
        
        # Free block
        self.disk_canvas.create_rectangle(margin_x, legend_y, 
                                         margin_x + 20, legend_y + 20,
                                         fill="#ecf0f1", outline="black")
        self.disk_canvas.create_text(margin_x + 30, legend_y + 10,
                                     text="Free Block", anchor=tk.W, font=("Arial", 9))
        
        # File blocks
        x_offset = margin_x + 150
        for file_name, color in file_colors.items():
            self.disk_canvas.create_rectangle(x_offset, legend_y,
                                             x_offset + 20, legend_y + 20,
                                             fill=color, outline="black")
            self.disk_canvas.create_text(x_offset + 30, legend_y + 10,
                                         text=file_name, anchor=tk.W, font=("Arial", 9))
            x_offset += 150
            if x_offset > canvas_width - 200:
                break
    
    def show_block_info(self, event, block):
        """Show block information on hover."""
        # Could implement tooltip here
        pass
    
    def update_system_status(self):
        """Update system status display."""
        total_blocks = len(self.disk_blocks)
        used_blocks = sum(1 for b in self.disk_blocks if b.is_allocated)
        free_blocks = total_blocks - used_blocks
        utilization = (used_blocks / total_blocks) * 100
        
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        
        status = f"Disk Size:    {self.total_disk_size} KB\n"
        status += f"Used Space:   {used_blocks} KB ({utilization:.1f}%)\n"
        status += f"Free Space:   {free_blocks} KB\n"
        status += f"Total Files:  {len(self.files)}\n"
        status += f"Fragmentation: {'Low' if free_blocks < 10 or used_blocks < 10 else 'Normal'}"
        
        self.status_text.insert(1.0, status)
        self.status_text.config(state=tk.DISABLED)
    
    def log(self, message):
        """Add message to activity log."""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
